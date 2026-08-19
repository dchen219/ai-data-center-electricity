"""
Industry news site source.

Scrapes datacenterdynamics.com and datacenterknowledge.com search pages.
"""

import logging
import time
from typing import TYPE_CHECKING, List
from urllib.parse import quote_plus, urljoin

from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from dc_url_collector.collector import URLCollector

logger = logging.getLogger(__name__)

# Sites to scrape with their search-URL templates.
_NEWS_SITES = [
    {
        "name": "datacenterdynamics",
        "base": "https://www.datacenterdynamics.com",
        "search_tpl": "https://www.datacenterdynamics.com/en/search/?q={q}",
    },
    {
        "name": "datacenterknowledge",
        "base": "https://www.datacenterknowledge.com",
        "search_tpl": "https://www.datacenterknowledge.com/search?q={q}",
    },
]


def _scrape_site(
    collector: "URLCollector",
    site: dict,
    query: str,
    company: str,
) -> int:
    """Scrape a single search page on a news site."""
    count = 0
    search_url = site["search_tpl"].format(q=quote_plus(query))
    resp = collector._get(search_url)
    if resp is None:
        return 0

    company_lower = company.lower()
    base = site["base"]

    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]

            # Make absolute
            if href.startswith("/"):
                href = urljoin(base, href)

            # Only keep links on the same site that look like articles
            if not href.startswith(base):
                continue
            path_lower = href.lower()
            if not any(
                seg in path_lower
                for seg in ("/article", "/news", "/feature", "/20")
            ):
                continue

            link_text = link.get_text().lower()
            if company_lower in path_lower or company_lower in link_text:
                if collector._write_url(
                    href, company, query, site["name"]
                ):
                    count += 1
    except Exception as exc:
        logger.debug(
            "News parse error for %s ('%s'): %s", site["name"], query, exc
        )

    return count


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Scrape industry news sites for company-related articles.

    Returns total number of URLs written.
    """
    total = 0

    for company in companies:
        for site in _NEWS_SITES:
            if collector._should_stop():
                break

            # Build a handful of targeted queries per company
            search_terms = [
                f"{company} data center",
                f"{company} data center energy",
                f"{company} data center expansion",
            ]

            for term in search_terms:
                if collector._should_stop():
                    break

                task = collector._task_key(
                    f"news_{site['name']}", term
                )
                if collector._is_task_done(task):
                    continue

                try:
                    n = _scrape_site(collector, site, term, company)
                    total += n
                except Exception as exc:
                    logger.warning(
                        "News scrape failed (%s, '%s'): %s",
                        site["name"],
                        term,
                        exc,
                    )

                collector._mark_done(task)
                time.sleep(collector.delay)

    logger.info("News: collected %d URLs", total)
    return total
