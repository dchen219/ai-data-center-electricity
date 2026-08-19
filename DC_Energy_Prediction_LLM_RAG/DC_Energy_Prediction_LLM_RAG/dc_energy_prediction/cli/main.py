"""CLI entry point for DC Energy Prediction."""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

from dc_energy_prediction.config.companies import (
    get_company,
    get_all_companies,
    list_company_names,
)
from dc_energy_prediction.config.settings import get_settings


def cmd_list(_args: argparse.Namespace) -> int:
    """List all configured companies and their data centers."""
    companies = get_all_companies()

    print("Configured Companies and Data Centers:")
    print("=" * 60)

    for company in companies:
        print(f"\n{company.name}")
        print(f"  FAISS DB: {company.faiss_db_name}")
        print(f"  Documents folder: {company.pdf_folder}")
        print(f"  Data centers ({len(company.data_centers)}):")
        for dc in company.data_centers:
            print(f"    - {dc.site_name}")

    return 0


def cmd_build_db(args: argparse.Namespace) -> int:
    """Build or update a FAISS database."""
    from dc_energy_prediction.data.document_loader import (
        load_pdf_documents,
        load_csv_documents,
        chunk_documents,
    )
    from dc_energy_prediction.data.vector_store import VectorStoreManager

    company = get_company(args.company)
    if company is None:
        print(f"Error: Unknown company '{args.company}'")
        print(f"Available companies: {', '.join(list_company_names())}")
        return 1

    settings = get_settings()
    verbose = args.verbose

    # Load documents
    all_docs = []

    # Load PDFs from company folder
    pdf_folder = settings.get_documents_path(company.name)
    if pdf_folder.exists():
        if verbose:
            print(f"Loading PDFs from {pdf_folder}...")
        try:
            pdf_docs = load_pdf_documents(pdf_folder, verbose=verbose)
            all_docs.extend(pdf_docs)
        except ImportError as e:
            print(f"Warning: Could not load PDFs - {e}")
    else:
        if verbose:
            print(f"PDF folder not found: {pdf_folder}")

    # Load CSV if specified
    if args.csv:
        csv_path = Path(args.csv)
        if csv_path.exists():
            if verbose:
                print(f"Loading CSV from {csv_path}...")
            csv_docs = load_csv_documents(csv_path, verbose=verbose)
            all_docs.extend(csv_docs)
        else:
            print(f"Warning: CSV file not found: {csv_path}")

    if not all_docs:
        print("Error: No documents found to process")
        return 1

    # Chunk documents
    chunks = chunk_documents(all_docs, verbose=verbose)

    # Create or update vector store
    manager = VectorStoreManager()

    if args.append and manager.exists(company.faiss_db_name):
        if verbose:
            print(f"Appending to existing database: {company.faiss_db_name}")
        manager.add_documents(company.faiss_db_name, chunks, verbose=verbose)
    else:
        if verbose:
            print(f"Creating new database: {company.faiss_db_name}")
        manager.create(chunks, company.faiss_db_name, verbose=verbose)

    print(f"Successfully built FAISS database for {company.name}")
    return 0


def cmd_forecast(args: argparse.Namespace) -> int:
    """Run energy forecasts."""
    from dc_energy_prediction.prediction.forecast import run_forecasts_for_company

    settings = get_settings()

    try:
        settings.validate()
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    year = args.year
    horizon = args.horizon
    verbose = args.verbose
    output_path = args.output

    if args.company.lower() == "all":
        # Run for all companies
        all_results = []
        for company in get_all_companies():
            if verbose:
                print(f"\n{'='*60}")
                print(f"Processing {company.name}...")
                print("=" * 60)

            try:
                result = run_forecasts_for_company(
                    company,
                    year=year,
                    horizon=horizon,
                    verbose=verbose,
                )
                all_results.append(result)
            except FileNotFoundError as e:
                print(f"Skipping {company.name}: {e}")
                continue

        final_md = "\n\n".join(all_results)
    else:
        company = get_company(args.company)
        if company is None:
            print(f"Error: Unknown company '{args.company}'")
            print(f"Available companies: {', '.join(list_company_names())}")
            return 1

        try:
            final_md = run_forecasts_for_company(
                company,
                year=year,
                horizon=horizon,
                verbose=verbose,
            )
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1

    # Output results
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(final_md)
        print(f"Results saved to {output_path}")
    else:
        print(final_md)

    return 0


def cmd_expansion(args: argparse.Namespace) -> int:
    """Predict expansion locations."""
    from dc_energy_prediction.prediction.expansion import ExpansionPredictor

    settings = get_settings()

    try:
        settings.validate()
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    threshold = args.threshold
    verbose = args.verbose

    if args.company.lower() == "all":
        # Run for all companies
        for company in get_all_companies():
            if verbose:
                print(f"\n{'='*60}")
                print(f"Processing {company.name}...")
                print("=" * 60)

            try:
                predictor = ExpansionPredictor(company, verbose=verbose)
                predictions = predictor.predict_expansion_locations(
                    probability_threshold=threshold,
                )
                print(predictor.format_predictions_markdown(predictions))
            except FileNotFoundError as e:
                print(f"Skipping {company.name}: {e}")
                continue
    else:
        company = get_company(args.company)
        if company is None:
            print(f"Error: Unknown company '{args.company}'")
            print(f"Available companies: {', '.join(list_company_names())}")
            return 1

        try:
            predictor = ExpansionPredictor(company, verbose=verbose)
            predictions = predictor.predict_expansion_locations(
                probability_threshold=threshold,
            )

            if args.json:
                print(json.dumps(predictions, indent=2))
            else:
                print(predictor.format_predictions_markdown(predictions))

        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1

    return 0


def main(argv: Optional[list] = None) -> int:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="dc_energy_prediction",
        description="Data Center Energy Prediction using LLM + RAG",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("list", help="List configured companies")
    list_parser.set_defaults(func=cmd_list)

    # Build-db command
    build_parser = subparsers.add_parser("build-db", help="Build FAISS database")
    build_parser.add_argument(
        "company",
        help="Company name",
    )
    build_parser.add_argument(
        "--csv",
        help="Path to CSV file to include",
    )
    build_parser.add_argument(
        "--append",
        action="store_true",
        help="Append to existing database instead of replacing",
    )
    build_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print verbose output",
    )
    build_parser.set_defaults(func=cmd_build_db)

    # Forecast command
    forecast_parser = subparsers.add_parser("forecast", help="Run energy forecasts")
    forecast_parser.add_argument(
        "company",
        help="Company name or 'all' for all companies",
    )
    forecast_parser.add_argument(
        "--year",
        type=int,
        default=2025,
        help="Baseline year (default: 2025)",
    )
    forecast_parser.add_argument(
        "--horizon",
        type=int,
        default=5,
        help="Forecast horizon in years (default: 5)",
    )
    forecast_parser.add_argument(
        "-o", "--output",
        help="Output file path for markdown results",
    )
    forecast_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print verbose output",
    )
    forecast_parser.set_defaults(func=cmd_forecast)

    # Expansion command
    expansion_parser = subparsers.add_parser(
        "expansion",
        help="Predict expansion locations",
    )
    expansion_parser.add_argument(
        "company",
        help="Company name or 'all' for all companies",
    )
    expansion_parser.add_argument(
        "--threshold",
        type=float,
        default=0.0,
        help="Minimum probability threshold (default: 0.0)",
    )
    expansion_parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON instead of markdown",
    )
    expansion_parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print verbose output",
    )
    expansion_parser.set_defaults(func=cmd_expansion)

    # Parse arguments
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
