"""
Academic paper sources: arXiv API and Semantic Scholar API.
"""

import logging
import time
from typing import TYPE_CHECKING, List
from urllib.parse import quote_plus
from xml.etree import ElementTree

if TYPE_CHECKING:
    from dc_url_collector.collector import URLCollector

logger = logging.getLogger(__name__)

_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _search_arxiv(
    collector: "URLCollector",
    query: str,
    company: str,
    max_results: int = 50,
) -> int:
    """Query the arXiv API and record paper URLs."""
    count = 0
    api_url = (
        f"http://export.arxiv.org/api/query?"
        f"search_query=all:{quote_plus(query)}"
        f"&start=0&max_results={max_results}"
    )
    resp = collector._get(api_url, timeout=60)
    if resp is None:
        return 0

    try:
        root = ElementTree.fromstring(resp.content)
        for entry in root.findall("atom:entry", _ARXIV_NS):
            link_el = entry.find(
                "atom:link[@type='text/html']", _ARXIV_NS
            )
            if link_el is None:
                # Fallback to the first <id> which is the abs URL
                id_el = entry.find("atom:id", _ARXIV_NS)
                if id_el is not None and id_el.text:
                    url = id_el.text.strip()
                else:
                    continue
            else:
                url = link_el.get("href", "")

            if url and collector._write_url(url, company, query, "arxiv"):
                count += 1
    except ElementTree.ParseError as exc:
        logger.debug("arXiv XML parse error for '%s': %s", query, exc)

    return count


def _search_semantic_scholar(
    collector: "URLCollector",
    query: str,
    company: str,
    max_results: int = 50,
) -> int:
    """Query the Semantic Scholar API."""
    count = 0
    api_url = (
        f"https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={quote_plus(query)}&limit={max_results}"
        f"&fields=url,externalIds"
    )
    resp = collector._get(api_url, timeout=60)
    if resp is None:
        return 0

    try:
        data = resp.json()
        for paper in data.get("data", []):
            url = paper.get("url", "")
            if url and collector._write_url(
                url, company, query, "semantic_scholar"
            ):
                count += 1

            # Also record DOI-based URL if available
            ext = paper.get("externalIds") or {}
            doi = ext.get("DOI")
            if doi:
                doi_url = f"https://doi.org/{doi}"
                if collector._write_url(
                    doi_url, company, query, "semantic_scholar"
                ):
                    count += 1
    except Exception as exc:
        logger.debug(
            "Semantic Scholar parse error for '%s': %s", query, exc
        )

    return count


# ── public entry point ────────────────────────────────────────────────────
def collect(collector: "URLCollector", companies: List[str]) -> int:
    """Search arXiv and Semantic Scholar for academic papers.

    Returns total number of URLs written.
    """
    queries = collector._build_queries(companies)
    total = 0

    for query, company in queries:
        if collector._should_stop():
            break

        task_arxiv = collector._task_key("arxiv", query)
        if not collector._is_task_done(task_arxiv):
            try:
                total += _search_arxiv(collector, query, company)
            except Exception as exc:
                logger.warning("arXiv query failed ('%s'): %s", query, exc)
            collector._mark_done(task_arxiv)
            time.sleep(collector.delay)

        if collector._should_stop():
            break

        task_ss = collector._task_key("semantic_scholar", query)
        if not collector._is_task_done(task_ss):
            try:
                total += _search_semantic_scholar(collector, query, company)
            except Exception as exc:
                logger.warning(
                    "Semantic Scholar query failed ('%s'): %s", query, exc
                )
            collector._mark_done(task_ss)
            time.sleep(collector.delay)

    logger.info("Academic: collected %d URLs", total)
    return total
