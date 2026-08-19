"""Combined multi-company report and raw JSON export."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def write_combined_report(
    all_energy: dict[str, list[dict]],
    all_expansion: dict[str, list[dict]],
    company_names: dict[str, str],
    output_dir: Path,
    current_year: int = 2025,
    forecast_horizon: int = 5,
) -> Path:
    """Write a combined Markdown report covering all companies.

    Args:
        all_energy: Mapping of company key -> list of site result dicts
            (same format as *site_results* in :func:`write_energy_report`).
        all_expansion: Mapping of company key -> list of expansion prediction
            dicts (same format as *predictions* in :func:`write_expansion_report`).
        company_names: Mapping of company key -> display name.
        output_dir: Directory where the report file will be written.
        current_year: The base year for the forecast (default 2025).
        forecast_horizon: Number of years to forecast beyond *current_year*.

    Returns:
        Path to the written report file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "all_companies_forecast.md"
    end_year = current_year + forecast_horizon

    lines: list[str] = []
    lines.append("# All Companies — Data Center Energy Forecast & Expansion Predictions")
    lines.append("")

    for company_key, display_name in company_names.items():
        lines.append(f"---")
        lines.append(f"# {display_name}")
        lines.append("")

        # Energy forecasts
        site_results = all_energy.get(company_key, [])
        if site_results:
            lines.append(f"## Energy Forecast")
            lines.append("")
            for site_result in site_results:
                site_name = site_result.get("site", "Unknown Site")
                lines.append(f"### {display_name} — {site_name}")
                lines.append("")

                if "error" in site_result:
                    lines.append(f"**Error:** {site_result['error']}")
                    lines.append("")
                    continue

                baseline = site_result.get("baseline", {})
                lines.append(f"#### Baseline Parameters ({current_year})")
                lines.append("```json")
                lines.append(json.dumps(baseline, indent=2))
                lines.append("```")
                lines.append("")

                forecast = site_result.get("forecast", [])
                lines.append(f"#### Forecast Results ({current_year + 1} – {end_year})")
                lines.append("```json")
                lines.append(json.dumps(forecast, indent=2))
                lines.append("```")
                lines.append("")

        # Expansion predictions
        predictions = all_expansion.get(company_key, [])
        if predictions:
            lines.append(f"## Expansion Location Predictions")
            lines.append("")
            for idx, pred in enumerate(predictions, start=1):
                location = pred.get("location_name", "Unknown")
                probability = pred.get("estimated_probability", 0.0)
                factors = pred.get("key_factors", "N/A")
                notes = pred.get("notes", "N/A")

                lines.append(f"### {idx}. {location}")
                lines.append(f"**Probability:** {probability:.0%}")
                lines.append(f"**Key Factors:** {factors}")
                lines.append(f"**Notes:** {notes}")
                lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Combined report written to %s", report_path)
    return report_path


def write_raw_json(
    all_energy: dict,
    all_expansion: dict,
    company_keys: list[str],
    output_dir: Path,
    current_year: int = 2025,
    forecast_horizon: int = 5,
) -> Path:
    """Write a raw JSON export of all prediction results.

    Args:
        all_energy: Mapping of company key -> list of site result dicts.
        all_expansion: Mapping of company key -> list of expansion prediction dicts.
        company_keys: Ordered list of company keys to include.
        output_dir: Directory where the JSON file will be written.
        current_year: The base year for the forecast (default 2025).
        forecast_horizon: Number of years to forecast beyond *current_year*.

    Returns:
        Path to the written JSON file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "all_results.json"

    payload = {
        "energy_forecasts": {
            key: all_energy.get(key, []) for key in company_keys
        },
        "expansion_predictions": {
            key: all_expansion.get(key, []) for key in company_keys
        },
        "metadata": {
            "current_year": current_year,
            "forecast_horizon": forecast_horizon,
            "companies": company_keys,
        },
    }

    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    logger.info("Raw JSON written to %s", json_path)
    return json_path
