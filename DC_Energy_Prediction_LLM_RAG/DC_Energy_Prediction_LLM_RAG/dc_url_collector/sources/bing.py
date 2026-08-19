"""
Bing free web-search source.

Scrapes Bing search result pages with BeautifulSoup.
"""

import logging
import time
from typing import TYPE_CHECKING, List
from urllib.parse import quote_plus

from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from dc_url_collector.collector import URLCollector

logger = logging.getLogger(__name__)


def _search_bing(
    collector: "URLCollector",
    query: str,
    company: str,
) -> int:
    """Scrape a single Bing SERP.  Returns count of URLs written."""
    count = 0
    url = f"https://www.bing.com/search?q={quote_plus(query)}&count=50"
    resp = collector._get(url)
    if resp is None:
        return 0

    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        for item in soup.select("li.b_algo"):
            link = item.select_one("h2 a")
            if link:
                href = link.get("href", "")
                if href.startswith("http"):
                    if collector._write_url(href, company, query, "bing"):
                        count += 1
                    continue

            # Fallback: reconstruct from <cite>
            cite = item.select_one("cite")
            if cite:
                cite_text = cite.get_text().strip()
                reconstructed = (
                    cite_text.replace(" \u203a ", "/")
                    .replace("\u203a ", "/")
                    .replace(" \u203a", "/")
                )
                if not reconstructed.startswith(("http://", "https://")):
                    reconstructed = "https://" + reconstructed
                if collector._write_url(
                    reconstructed, company, query, "bing"
                ):
                    count += 1
    except Exception as exc:
        logger.debug("Bing parse error for '%s': %s", query, exc)

    return count


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Scrape Bing for every (keyword x company) query.

    Returns total number of URLs written.
    """
    queries = collector._build_queries(companies)
    total = 0

    for query, company in queries:
        if collector._should_stop():
            break

        task = collector._task_key("bing", query)
        if collector._is_task_done(task):
            continue

        try:
            n = _search_bing(collector, query, company)
            total += n
        except Exception as exc:
            logger.warning("Bing query failed ('%s'): %s", query, exc)

        collector._mark_done(task)
        time.sleep(collector.delay)

    logger.info("Bing: collected %d URLs", total)
    return total
