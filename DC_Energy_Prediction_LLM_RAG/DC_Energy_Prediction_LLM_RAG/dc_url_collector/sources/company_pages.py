"""
Company sustainability / IR page scraper.

Follows links on known official company pages and records those whose
path contains data-center-related keywords.
"""

import logging
import time
from typing import TYPE_CHECKING, List
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from dc_url_collector.config import COMPANY_SUSTAINABILITY_PAGES

if TYPE_CHECKING:
    from dc_url_collector.collector import URLCollector

logger = logging.getLogger(__name__)

# Path fragments that signal relevant content
_RELEVANT_KEYWORDS = [
    "data-center",
    "datacenter",
    "data_center",
    "energy",
    "sustainability",
    "environment",
    "infrastructure",
    "power",
    "renewable",
    "climate",
    "carbon",
    "cooling",
    "region",
    "location",
]


def _scrape_page(
    collector: "URLCollector",
    page_url: str,
    company: str,
) -> int:
    """Fetch *page_url* and harvest outgoing links that look DC-related."""
    count = 0
    resp = collector._get(page_url)
    if resp is None:
        return 0

    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        parsed_base = urlparse(page_url)
        base_origin = f"{parsed_base.scheme}://{parsed_base.netloc}"

        for link in soup.find_all("a", href=True):
            href = link["href"]

            # Make absolute
            if href.startswith("/"):
                href = urljoin(base_origin, href)
            elif not href.startswith("http"):
                continue

            href_lower = href.lower()
            if any(kw in href_lower for kw in _RELEVANT_KEYWORDS):
                if collector._write_url(
                    href, company, f"company_page:{page_url}", "company_pages"
                ):
                    count += 1
    except Exception as exc:
        logger.debug(
            "Company page parse error (%s): %s", page_url, exc
        )

    return count


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Scrape official company sustainability/IR pages.

    Returns total number of URLs written.
    """
    total = 0

    for company in companies:
        pages = COMPANY_SUSTAINABILITY_PAGES.get(company, [])
        for page_url in pages:
            if collector._should_stop():
                break

            task = collector._task_key("company_pages", page_url)
            if collector._is_task_done(task):
                continue

            try:
                n = _scrape_page(collector, page_url, company)
                total += n
            except Exception as exc:
                logger.warning(
                    "Company page scrape failed (%s): %s", page_url, exc
                )

            collector._mark_done(task)
            time.sleep(collector.delay)

    logger.info("Company pages: collected %d URLs", total)
    return total
