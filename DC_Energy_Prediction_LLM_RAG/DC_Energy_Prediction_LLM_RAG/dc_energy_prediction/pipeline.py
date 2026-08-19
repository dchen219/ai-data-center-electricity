"""
Five-phase pipeline orchestrator.

Phase 1 — URL Collection
Phase 2 — Document Ingestion & FAISS Vectorization
Phase 3 — RAG-Based Energy Forecasting
Phase 4 — Expansion Location Prediction
Phase 5 — Report Generation
"""

import logging
import os
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional

from dc_energy_prediction.config.companies import COMPANIES, get_company
from dc_energy_prediction.utils.shutdown import is_shutdown

log = logging.getLogger("dc_energy")


def run_pipeline(
    company_keys: List[str],
    output_dir: Path,
    skip_collect: bool = False,
    collect_only: bool = False,
    max_urls_per_source: int = 200,
    max_docs_per_company: int = 50,
    current_year: int = 2025,
    forecast_horizon: int = 5,
    verbose: bool = False,
) -> None:
    """Run the full end-to-end pipeline.

    Args:
        company_keys: List of company keys (e.g. ["oracle", "google"]).
        output_dir: Root output directory.
        skip_collect: Skip Phase 1 (URL collection).
        collect_only: Stop after Phase 1.
        max_urls_per_source: Max URLs per (source, query) pair.
        max_docs_per_company: Max documents to fetch per company for FAISS.
        current_year: Baseline year for forecasts.
        forecast_horizon: Number of years to forecast.
        verbose: Enable verbose output.
    """
    output_dir = Path(output_dir)
    urls_dir = output_dir / "collected_urls"
    faiss_dir = output_dir / "faiss_dbs"
    docs_dir = output_dir / "documents"
    reports_dir = output_dir / "reports"
    for d in [urls_dir, faiss_dir, docs_dir, reports_dir]:
        d.mkdir(parents=True, exist_ok=True)

    company_names = [COMPANIES[k].name for k in company_keys]

    # ── Phase 1: URL Collection ──────────────────────────────────────────
    if not skip_collect:
        log.info("=" * 60)
        log.info("PHASE 1 — URL Collection")
        log.info("=" * 60)
        try:
            from dc_url_collector import URLCollector

            collector = URLCollector(
                output_dir=urls_dir,
                max_per_source=max_urls_per_source,
                delay=1.0,
                shutdown_check=is_shutdown,
            )
            try:
                total_urls = collector.run_all(company_names)
                log.info("Phase 1 complete: %d URLs collected", total_urls)
            finally:
                collector.close()
        except ImportError:
            log.warning(
                "dc_url_collector not available — skipping URL collection"
            )
        except Exception as exc:
            log.error("Phase 1 error: %s", exc)
            log.info("Continuing with available data …")

        if collect_only:
            log.info("--collect-only specified — stopping after Phase 1")
            return

    if is_shutdown():
        log.warning("Shutdown — exiting")
        return

    # ── Phase 2: Document Ingestion & Vectorization ──────────────────────
    log.info("=" * 60)
    log.info("PHASE 2 — Document Ingestion & FAISS Vectorization")
    log.info("=" * 60)

    from dc_energy_prediction.data.ingestion import ingest_documents_for_company

    for ck in company_keys:
        if is_shutdown():
            break
        company = get_company(ck)
        if company is None:
            log.warning("Unknown company '%s' — skipping", ck)
            continue
        try:
            ingest_documents_for_company(
                company=company,
                urls_dir=urls_dir,
                docs_dir=docs_dir,
                faiss_dir=faiss_dir,
                max_docs=max_docs_per_company,
                verbose=verbose,
                shutdown_check=is_shutdown,
            )
        except Exception as exc:
            log.error("Ingestion failed for %s: %s", ck, exc)
            if verbose:
                log.debug(traceback.format_exc())

    if is_shutdown():
        log.warning("Shutdown — exiting")
        return

    # Validate OpenAI key
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        log.error("OPENAI_API_KEY not set — cannot run prediction phases")
        return

    # ── Phase 3: Energy Forecasting ──────────────────────────────────────
    log.info("=" * 60)
    log.info("PHASE 3 — RAG-Based Energy Forecasting")
    log.info("=" * 60)

    from dc_energy_prediction.prediction.forecast import EnergyForecaster

    all_energy: Dict[str, List[Dict[str, Any]]] = {}

    for ck in company_keys:
        if is_shutdown():
            break
        company = get_company(ck)
        if company is None:
            continue

        db_path = faiss_dir / company.faiss_db_name
        if not (db_path / "index.faiss").exists():
            log.warning("No FAISS DB for %s — skipping forecast", ck)
            continue

        site_results: List[Dict[str, Any]] = []
        try:
            forecaster = EnergyForecaster(company, verbose=verbose)
            for dc in company.data_centers:
                if is_shutdown():
                    break
                log.info("  Forecasting %s — %s …", company.name, dc.site_name)
                try:
                    baseline, forecast = forecaster.run_full_forecast(
                        dc.site_name, current_year, forecast_horizon
                    )
                    site_results.append({
                        "site": dc.site_name,
                        "baseline": baseline,
                        "forecast": forecast,
                    })
                    log.info(
                        "    Done — %d forecast years", len(forecast)
                        if isinstance(forecast, list) else 0
                    )
                except Exception as exc:
                    log.error("    Failed %s: %s", dc.site_name, exc)
                    site_results.append({
                        "site": dc.site_name,
                        "error": str(exc),
                    })
        except Exception as exc:
            log.error("Forecast setup failed for %s: %s", ck, exc)

        all_energy[ck] = site_results

    if is_shutdown():
        log.warning("Shutdown — exiting")
        return

    # ── Phase 4: Expansion Prediction ────────────────────────────────────
    log.info("=" * 60)
    log.info("PHASE 4 — Expansion Location Prediction")
    log.info("=" * 60)

    from dc_energy_prediction.prediction.expansion import ExpansionPredictor

    all_expansion: Dict[str, List[Dict[str, Any]]] = {}

    for ck in company_keys:
        if is_shutdown():
            break
        company = get_company(ck)
        if company is None:
            continue

        db_path = faiss_dir / company.faiss_db_name
        if not (db_path / "index.faiss").exists():
            log.warning("No FAISS DB for %s — skipping expansion", ck)
            continue

        try:
            predictor = ExpansionPredictor(company, verbose=verbose)
            predictions = predictor.predict_expansion_locations(
                years_ahead=forecast_horizon
            )
            all_expansion[ck] = predictions
            log.info(
                "  %s: %d expansion locations predicted",
                company.name, len(predictions),
            )
        except Exception as exc:
            log.error("Expansion failed for %s: %s", ck, exc)
            all_expansion[ck] = []

    # ── Phase 5: Report Generation ───────────────────────────────────────
    log.info("=" * 60)
    log.info("PHASE 5 — Report Generation")
    log.info("=" * 60)

    from dc_energy_prediction.reporting import (
        write_combined_report,
        write_energy_report,
        write_expansion_report,
    )
    from dc_energy_prediction.reporting.combined_report import write_raw_json

    company_display = {ck: COMPANIES[ck].name for ck in company_keys}

    for ck in company_keys:
        company = get_company(ck)
        if company is None:
            continue

        if ck in all_energy and all_energy[ck]:
            write_energy_report(
                company.name, all_energy[ck], reports_dir,
                current_year, forecast_horizon,
            )

        if ck in all_expansion and all_expansion[ck]:
            write_expansion_report(
                company.name, all_expansion[ck], reports_dir,
            )

    write_combined_report(
        all_energy, all_expansion, company_display,
        reports_dir, current_year, forecast_horizon,
    )
    write_raw_json(
        all_energy, all_expansion, company_keys,
        reports_dir, current_year, forecast_horizon,
    )

    log.info("=" * 60)
    log.info("Pipeline complete.  Reports → %s", reports_dir)
    log.info("=" * 60)
