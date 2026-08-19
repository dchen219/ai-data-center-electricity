#!/usr/bin/env python3
"""
Data Center Energy Prediction Pipeline (LLM + RAG)
===================================================

End-to-end pipeline for predicting data center energy consumption and
expansion locations for major cloud companies using LLM with RAG.

Pipeline Phases:
    Phase 1 — URL Collection      (dc_url_collector)
    Phase 2 — Document Ingestion   (dc_energy_prediction.data.ingestion)
    Phase 3 — Energy Forecasting   (dc_energy_prediction.prediction.forecast)
    Phase 4 — Expansion Prediction (dc_energy_prediction.prediction.expansion)
    Phase 5 — Report Generation    (dc_energy_prediction.reporting)

Usage:
    python main.py --all                         # Full pipeline
    python main.py --company oracle              # Single company
    python main.py --all --skip-collect          # Skip URL collection
    python main.py --all --collect-only          # URL collection only
    python main.py --all --max-urls-per-source 500
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from dc_energy_prediction.config.companies import COMPANIES
from dc_energy_prediction.pipeline import run_pipeline
from dc_energy_prediction.utils.shutdown import install_signal_handlers

LOG_FMT = "%(asctime)s | %(levelname)-7s | %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FMT)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Data Center Energy Prediction Pipeline (LLM + RAG)",
    )
    parser.add_argument("--company", "-c",
                        help="Company key (e.g. 'oracle') or 'all'")
    parser.add_argument("--all", action="store_true",
                        help="Run for all companies")
    parser.add_argument("--output-dir", "-o", default="./output",
                        help="Output directory (default: ./output)")
    parser.add_argument("--skip-collect", action="store_true",
                        help="Skip URL collection phase")
    parser.add_argument("--collect-only", action="store_true",
                        help="Only run URL collection, then stop")
    parser.add_argument("--max-urls-per-source", type=int, default=200,
                        help="Max URLs per (source, query) pair")
    parser.add_argument("--max-docs", type=int, default=50,
                        help="Max documents to fetch per company for FAISS")
    parser.add_argument("--year", type=int, default=2025,
                        help="Baseline year (default: 2025)")
    parser.add_argument("--horizon", type=int, default=5,
                        help="Forecast horizon in years (default: 5)")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    # Resolve company keys
    if args.all or (args.company and args.company.lower() == "all"):
        company_keys = list(COMPANIES.keys())
    elif args.company:
        ck = args.company.lower()
        if ck not in COMPANIES:
            print(f"Unknown company '{args.company}'. "
                  f"Available: {', '.join(COMPANIES.keys())}")
            return 1
        company_keys = [ck]
    else:
        parser.print_help()
        return 0

    install_signal_handlers()

    run_pipeline(
        company_keys=company_keys,
        output_dir=Path(args.output_dir),
        skip_collect=args.skip_collect,
        collect_only=args.collect_only,
        max_urls_per_source=args.max_urls_per_source,
        max_docs_per_company=args.max_docs,
        current_year=args.year,
        forecast_horizon=args.horizon,
        verbose=args.verbose,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
