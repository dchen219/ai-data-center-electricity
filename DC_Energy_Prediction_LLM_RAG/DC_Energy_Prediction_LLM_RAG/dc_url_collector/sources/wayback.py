"""
Internet Archive Wayback Machine CDX source.

Queries the Wayback CDX API for historical snapshots of company
data-center pages.
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

# Path prefixes known to hold data-center content, keyed by company.
_COMPANY_PATHS: dict[str, list[str]] = {
    "Oracle": [
        "oracle.com/cloud/data-centers",
        "oracle.com/corporate/sustainability",
    ],
    "Google": [
        "google.com/about/datacenters",
        "sustainability.google",
        "cloud.google.com/about/locations",
    ],
    "Microsoft": [
        "azure.microsoft.com/en-us/global-infrastructure",
        "news.microsoft.com",
    ],
    "Apple": [
        "apple.com/environment",
    ],
    "Meta": [
        "datacenters.fb.com",
        "sustainability.fb.com",
    ],
    "Amazon": [
        "aws.amazon.com/about-aws/global-infrastructure",
        "sustainability.aboutamazon.com",
    ],
    "Nebius": [
        "nebius.com",
    ],
    "CoreWeave": [
        "coreweave.com",
    ],
}

# Also scrape known DC-industry news sites for historical articles
_INDUSTRY_DOMAINS = [
    "datacenterknowledge.com",
    "datacenterdynamics.com",
]


def _fetch_cdx(
    collector: "URLCollector",
    url_prefix: str,
    limit: int = 20000,
) -> list[str]:
    """Query the Wayback CDX API and return unique original URLs."""
    cdx_url = (
        f"http://web.archive.org/cdx/search/cdx"
        f"?url={quote(url_prefix)}*"
        f"&output=json&collapse=urlkey&limit={limit}"
        f"&filter=statuscode:200"
    )
    resp = collector._get(cdx_url, timeout=120)
    if resp is None:
        return []

    urls: list[str] = []
    try:
        data = json.loads(resp.text)
        # First row is the header: ["urlkey","timestamp","original",...]
        if len(data) > 1:
            for row in data[1:]:
                if len(row) >= 3 and row[2].startswith("http"):
                    urls.append(row[2])
    except (json.JSONDecodeError, TypeError):
        # Try line-based format
        for line in resp.text.strip().splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[2].startswith("http"):
                urls.append(parts[2])
    return urls


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Query Wayback Machine CDX API for historical snapshots.

    Returns total number of URLs written.
    """
    total = 0

    # Company-specific paths
    for company in companies:
        paths = _COMPANY_PATHS.get(company, [])
        for path in paths:
            if collector._should_stop():
                break

            task = collector._task_key("wayback", path)
            if collector._is_task_done(task):
                continue

            try:
                urls = _fetch_cdx(collector, path)
                for url in urls:
                    if collector._write_url(
                        url, company, f"wayback:{path}", "wayback"
                    ):
                        total += 1
            except Exception as exc:
                logger.warning(
                    "Wayback query failed (%s): %s", path, exc
                )

            collector._mark_done(task)
            time.sleep(collector.delay)

    # Industry news domains (attributed to "Various")
    for domain in _INDUSTRY_DOMAINS:
        if collector._should_stop():
            break

        task = collector._task_key("wayback", domain)
        if collector._is_task_done(task):
            continue

        try:
            urls = _fetch_cdx(collector, domain)
            for url in urls:
                if collector._write_url(
                    url, "Various", f"wayback:{domain}", "wayback"
                ):
                    total += 1
        except Exception as exc:
            logger.warning(
                "Wayback industry query failed (%s): %s", domain, exc
            )

        collector._mark_done(task)
        time.sleep(collector.delay)

    logger.info("Wayback: collected %d URLs", total)
    return total
