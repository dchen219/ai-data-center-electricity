#!/usr/bin/env python3
"""
Core URLCollector class.

Provides checkpoint/resume, streaming CSV output, HTTP helpers with
exponential-backoff retry, URL deduplication, and orchestration of all
source modules under ``dc_url_collector.sources``.
"""

import csv
import json
import logging
import os
import time
from datetime import datetime
from typing import Callable, Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse

import requests

from dc_url_collector.config import (
    COMPANY_DOMAINS,
    ENERGY_KEYWORDS,
    LOCATION_KEYWORDS,
    YEAR_RANGE,
)

logger = logging.getLogger(__name__)

# ── Request headers ────────────────────────────────────────────────────────
_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.5",
}

# Domains we always skip
_SKIP_DOMAINS = frozenset(
    [
        "twitter.com",
        "x.com",
        "facebook.com",
        "linkedin.com",
        "instagram.com",
        "youtube.com",
        "tiktok.com",
        "pinterest.com",
        "reddit.com",
        "quora.com",
    ]
)

CSV_FIELDS = ["url", "company", "query", "source", "collected_at"]


class URLCollector:
    """Orchestrates URL collection from every configured source."""

    # ── construction ──────────────────────────────────────────────────────
    def __init__(
        self,
        output_dir: str = "collected_urls",
        max_per_source: int = 200,
        request_timeout: int = 30,
        delay: float = 1.0,
        shutdown_check: Optional[Callable[[], bool]] = None,
    ):
        self.output_dir = output_dir
        self.max_per_source = max_per_source
        self.request_timeout = request_timeout
        self.delay = delay

        self._shutdown_check = shutdown_check
        self._done: bool = False

        # URL deduplication (normalised URLs)
        self._seen: Set[str] = set()

        # Streaming CSV writers keyed by source name
        self._writers: Dict[str, Tuple[object, csv.DictWriter]] = {}

        # Checkpoint bookkeeping
        self._checkpoint_path = os.path.join(output_dir, ".checkpoint.json")
        self._completed_tasks: Set[str] = set()

        os.makedirs(output_dir, exist_ok=True)
        self._load_checkpoint()

    # ── graceful shutdown ─────────────────────────────────────────────────
    def _should_stop(self) -> bool:
        """Return *True* when the collector should stop ASAP."""
        if self._done:
            return True
        if self._shutdown_check is not None and self._shutdown_check():
            self._done = True
            return True
        return False

    # ── checkpoint / resume ───────────────────────────────────────────────
    def _load_checkpoint(self) -> None:
        if os.path.exists(self._checkpoint_path):
            try:
                with open(self._checkpoint_path, "r", encoding="utf-8") as fh:
                    data = json.load(fh)
                self._completed_tasks = set(data.get("completed_tasks", []))
                self._seen = set(data.get("seen_urls", []))
                logger.info(
                    "Resumed checkpoint: %d tasks done, %d URLs seen",
                    len(self._completed_tasks),
                    len(self._seen),
                )
            except (json.JSONDecodeError, OSError) as exc:
                logger.warning("Could not load checkpoint, starting fresh: %s", exc)

    def _save_checkpoint(self) -> None:
        tmp = self._checkpoint_path + ".tmp"
        try:
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump(
                    {
                        "completed_tasks": sorted(self._completed_tasks),
                        "seen_urls": sorted(self._seen),
                        "saved_at": datetime.now().isoformat(),
                    },
                    fh,
                )
            os.replace(tmp, self._checkpoint_path)
        except OSError as exc:
            logger.warning("Failed to save checkpoint: %s", exc)

    def _task_key(self, source: str, label: str) -> str:
        """Return a deterministic key for a (source, label) pair."""
        return f"{source}::{label}"

    def _mark_done(self, task_key: str) -> None:
        self._completed_tasks.add(task_key)
        self._save_checkpoint()

    def _is_task_done(self, task_key: str) -> bool:
        return task_key in self._completed_tasks

    # ── streaming CSV writer ──────────────────────────────────────────────
    def _get_writer(self, source_name: str) -> csv.DictWriter:
        """Return (and lazily create) a DictWriter for *source_name*."""
        if source_name not in self._writers:
            path = os.path.join(self.output_dir, f"{source_name}.csv")
            fh = open(path, "a", newline="", encoding="utf-8")  # noqa: SIM115
            writer = csv.DictWriter(
                fh, fieldnames=CSV_FIELDS, quoting=csv.QUOTE_ALL
            )
            if fh.tell() == 0:
                writer.writeheader()
            self._writers[source_name] = (fh, writer)
        return self._writers[source_name][1]

    def _write_url(
        self,
        url: str,
        company: str,
        query: str,
        source: str,
    ) -> bool:
        """Deduplicate and append a URL row.  Returns *True* if written."""
        if not url or not url.startswith(("http://", "https://")):
            return False

        parsed = urlparse(url)
        if any(d in parsed.netloc for d in _SKIP_DOMAINS):
            return False

        # Normalise for dedup
        norm = f"{parsed.netloc.lower()}{parsed.path.rstrip('/')}"
        if norm in self._seen:
            return False
        self._seen.add(norm)

        writer = self._get_writer(source)
        writer.writerow(
            {
                "url": url,
                "company": company,
                "query": query,
                "source": source,
                "collected_at": datetime.now().isoformat(),
            }
        )
        return True

    def _flush_all(self) -> None:
        for fh, _ in self._writers.values():
            try:
                fh.flush()
            except OSError:
                pass

    def close(self) -> None:
        """Flush and close every open CSV handle, then save checkpoint."""
        for fh, _ in self._writers.values():
            try:
                fh.close()
            except OSError:
                pass
        self._writers.clear()
        self._save_checkpoint()

    # ── HTTP helper ───────────────────────────────────────────────────────
    def _get(
        self,
        url: str,
        *,
        headers: Optional[dict] = None,
        timeout: Optional[int] = None,
        max_retries: int = 3,
    ) -> Optional[requests.Response]:
        """GET *url* with exponential-backoff retry.

        Returns the :class:`~requests.Response` on success or ``None``
        after exhausting retries.
        """
        hdrs = dict(_HEADERS)
        if headers:
            hdrs.update(headers)
        tout = timeout or self.request_timeout

        for attempt in range(1, max_retries + 1):
            try:
                resp = requests.get(url, headers=hdrs, timeout=tout)
                if resp.status_code == 200:
                    return resp
                # Treat 429 / 5xx as retryable
                if resp.status_code in (429, 500, 502, 503, 504):
                    wait = 2 ** attempt
                    logger.debug(
                        "HTTP %d for %s, retry %d/%d in %ds",
                        resp.status_code,
                        url,
                        attempt,
                        max_retries,
                        wait,
                    )
                    time.sleep(wait)
                    continue
                # Non-retryable error
                return None
            except requests.RequestException as exc:
                wait = 2 ** attempt
                logger.debug(
                    "Request error for %s (%s), retry %d/%d in %ds",
                    url,
                    exc,
                    attempt,
                    max_retries,
                    wait,
                )
                time.sleep(wait)

        return None

    # ── query builder ─────────────────────────────────────────────────────
    def _build_queries(
        self,
        companies: List[str],
    ) -> List[Tuple[str, str]]:
        """Return a list of ``(query_string, company)`` pairs.

        Combines each company name with energy keywords, location keywords,
        and year range.
        """
        pairs: list[Tuple[str, str]] = []
        for company in companies:
            for kw in ENERGY_KEYWORDS:
                pairs.append((f"{company} {kw}", company))
            for loc in LOCATION_KEYWORDS:
                pairs.append((f"{company} data center {loc}", company))
            for year in YEAR_RANGE:
                pairs.append(
                    (f"{company} data center energy {year}", company)
                )
        return pairs

    # ── merge helper ──────────────────────────────────────────────────────
    def merge_all(self, final_filename: str = "all_urls_merged.csv") -> str:
        """Merge every CSV in *output_dir* into one deduplicated file.

        Returns the path to the merged file.
        """
        seen: set[str] = set()
        rows: list[dict] = []

        for name in sorted(os.listdir(self.output_dir)):
            if not name.endswith(".csv") or name == final_filename:
                continue
            path = os.path.join(self.output_dir, name)
            try:
                with open(path, "r", newline="", encoding="utf-8") as fh:
                    reader = csv.DictReader(fh)
                    for row in reader:
                        url = row.get("url", "")
                        if url and url not in seen:
                            seen.add(url)
                            rows.append(row)
            except OSError as exc:
                logger.warning("Skipping %s: %s", path, exc)

        out_path = os.path.join(self.output_dir, final_filename)
        with open(out_path, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=CSV_FIELDS, quoting=csv.QUOTE_ALL
            )
            writer.writeheader()
            writer.writerows(rows)

        logger.info("Merged %d unique URLs into %s", len(rows), out_path)
        return out_path

    # ── orchestrator ──────────────────────────────────────────────────────
    def run_all(self, companies: Optional[List[str]] = None) -> None:
        """Run every source collector sequentially.

        *companies* defaults to all keys in
        :data:`~dc_url_collector.config.COMPANY_DOMAINS`.
        """
        if companies is None:
            companies = list(COMPANY_DOMAINS.keys())

        logger.info(
            "Starting collection for companies: %s", ", ".join(companies)
        )

        # Import source modules lazily so partial installs still work.
        from dc_url_collector.sources import (  # noqa: F401  (side-effects)
            duckduckgo,
            bing,
            academic,
            news,
            common_crawl,
            wayback,
            company_pages,
        )

        source_modules = [
            ("duckduckgo", duckduckgo),
            ("bing", bing),
            ("academic", academic),
            ("news", news),
            ("common_crawl", common_crawl),
            ("wayback", wayback),
            ("company_pages", company_pages),
        ]

        for name, mod in source_modules:
            if self._should_stop():
                logger.info("Shutdown requested, stopping before %s", name)
                break
            logger.info("Running source: %s", name)
            try:
                count = mod.collect(self, companies)
                logger.info("Source %s collected %d URLs", name, count)
            except Exception:
                logger.exception("Source %s failed", name)
            self._flush_all()

        self.close()
        logger.info(
            "Collection finished. %d unique URLs across all sources.",
            len(self._seen),
        )
