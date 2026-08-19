"""
Common Crawl CDX index source.

Queries the Common Crawl index API for URLs matching company domains.
"""

import json
import logging
import time
from typing import TYPE_CHECKING, List
from urllib.parse import quote

from dc_url_collector.config import COMPANY_DOMAINS

if TYPE_CHECKING:
    from dc_url_collector.collector import URLCollector

logger = logging.getLogger(__name__)

# Recent Common Crawl index IDs to query
_CC_INDEXES = [
    "CC-MAIN-2024-51",
    "CC-MAIN-2024-46",
    "CC-MAIN-2024-42",
    "CC-MAIN-2024-38",
    "CC-MAIN-2024-33",
    "CC-MAIN-2024-30",
    "CC-MAIN-2023-50",
    "CC-MAIN-2023-40",
    "CC-MAIN-2023-23",
    "CC-MAIN-2022-49",
    "CC-MAIN-2022-40",
    "CC-MAIN-2022-27",
]

# URL path fragments that indicate data-center relevance
_DC_PATH_KEYWORDS = [
    "data-center",
    "datacenter",
    "data_center",
    "infrastructure",
    "sustainability",
    "renewable",
    "cloud",
    "server",
    "colocation",
    "hyperscale",
    "energy",
    "power",
]


def _fetch_index(
    collector: "URLCollector",
    domain: str,
    index: str,
    limit: int = 10000,
) -> list[str]:
    """Query a single CC index for *domain* and return matching URLs."""
    api_url = (
        f"http://index.commoncrawl.org/{index}-index"
        f"?url={quote(domain)}"
        f"&matchType=domain&output=json&limit={limit}"
    )
    resp = collector._get(api_url, timeout=120)
    if resp is None:
        return []

    urls: list[str] = []
    for line in resp.text.strip().splitlines():
        if not line:
            continue
        try:
            data = json.loads(line)
            u = data.get("url", "")
            if u and u.startswith("http"):
                urls.append(u)
        except json.JSONDecodeError:
            pass
    return urls


def _is_dc_related(url: str) -> bool:
    low = url.lower()
    return any(kw in low for kw in _DC_PATH_KEYWORDS)


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Query Common Crawl CDX indexes for company domain URLs.

    Returns total number of URLs written.
    """
    total = 0

    for company in companies:
        domain = COMPANY_DOMAINS.get(company)
        if not domain:
            continue

        for index in _CC_INDEXES:
            if collector._should_stop():
                break

            task = collector._task_key("common_crawl", f"{domain}@{index}")
            if collector._is_task_done(task):
                continue

            try:
                raw_urls = _fetch_index(collector, domain, index)
                for url in raw_urls:
                    if _is_dc_related(url):
                        if collector._write_url(
                            url,
                            company,
                            f"cc:{domain}",
                            "common_crawl",
                        ):
                            total += 1
            except Exception as exc:
                logger.warning(
                    "Common Crawl query failed (%s, %s): %s",
                    domain,
                    index,
                    exc,
                )

            collector._mark_done(task)
            time.sleep(collector.delay)

    logger.info("Common Crawl: collected %d URLs", total)
    return total
