"""
DuckDuckGo search source.

Uses the ``duckduckgo_search`` library (DDGS) when available, falling back
to scraping the HTML-lite endpoint.
"""

import logging
import time
from typing import TYPE_CHECKING, List
from urllib.parse import parse_qs, quote_plus, unquote

from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from dc_url_collector.collector import URLCollector

logger = logging.getLogger(__name__)

# Try to import the DDGS library; gracefully degrade if missing.
try:
    from duckduckgo_search import DDGS

    _DDGS_AVAILABLE = True
except ImportError:
    _DDGS_AVAILABLE = False
    logger.info("duckduckgo_search not installed; will use HTML fallback")


def _search_ddgs(
    collector: "URLCollector",
    query: str,
    company: str,
    max_results: int,
) -> int:
    """Search via the DDGS library.  Returns number of URLs written."""
    count = 0
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            for result in results:
                url = result.get("href", "")
                if collector._write_url(url, company, query, "duckduckgo"):
                    count += 1
    except Exception as exc:
        logger.debug("DDGS library error for '%s': %s", query, exc)
    return count


def _search_html(
    collector: "URLCollector",
    query: str,
    company: str,
    max_results: int,
) -> int:
    """Fallback: scrape DuckDuckGo's HTML-lite interface."""
    count = 0
    search_url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
    resp = collector._get(search_url)
    if resp is None:
        return 0

    try:
        soup = BeautifulSoup(resp.text, "html.parser")
        for result in soup.select(".result"):
            link = result.select_one(".result__a")
            if not link:
                continue
            href = link.get("href", "")

            # Extract real URL from the tracking redirect
            if "uddg=" in href and "?" in href:
                params = parse_qs(href.split("?", 1)[1])
                if "uddg" in params:
                    href = unquote(params["uddg"][0])
            if not href.startswith("http"):
                continue

            if collector._write_url(href, company, query, "duckduckgo"):
                count += 1
                if count >= max_results:
                    break
    except Exception as exc:
        logger.debug("DuckDuckGo HTML parse error for '%s': %s", query, exc)

    return count


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Search DuckDuckGo for every (keyword x company) query.

    Returns total number of URLs written.
    """
    queries = collector._build_queries(companies)
    total = 0

    for query, company in queries:
        if collector._should_stop():
            break

        task = collector._task_key("duckduckgo", query)
        if collector._is_task_done(task):
            continue

        try:
            if _DDGS_AVAILABLE:
                n = _search_ddgs(
                    collector, query, company, collector.max_per_source
                )
            else:
                n = _search_html(
                    collector, query, company, collector.max_per_source
                )
            total += n
        except Exception as exc:
            logger.warning("DuckDuckGo query failed ('%s'): %s", query, exc)

        collector._mark_done(task)
        time.sleep(collector.delay)

    logger.info("DuckDuckGo: collected %d URLs", total)
    return total
