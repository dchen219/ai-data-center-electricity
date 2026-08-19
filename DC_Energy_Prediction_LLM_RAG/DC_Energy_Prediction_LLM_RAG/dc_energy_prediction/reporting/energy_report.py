"""Energy forecast report generation."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def write_energy_report(
    company_name: str,
    site_results: list[dict],
    output_dir: Path,
    current_year: int = 2025,
    forecast_horizon: int = 5,
) -> Path:
    """Write a Markdown energy forecast report for a single company.

    Args:
        company_name: Display name of the company (e.g. "Oracle").
        site_results: List of per-site result dicts.  Each dict must contain:
            - "site" (str): site / location name
            - "baseline" (dict): baseline parameters for *current_year*
            - "forecast" (list[dict]): yearly forecast entries
            Alternatively a dict may contain an "error" (str) key to signal
            that the prediction for that site failed.
        output_dir: Directory where the report file will be written.
        current_year: The base year for the forecast (default 2025).
        forecast_horizon: Number of years to forecast beyond *current_year*.

    Returns:
        Path to the written report file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    company_key = company_name.lower().replace(" ", "_")
    report_path = output_dir / f"{company_key}_energy_forecast.md"

    end_year = current_year + forecast_horizon

    lines: list[str] = []
    lines.append(f"# {company_name} — Data Center Energy Forecast")
    lines.append("")

    for site_result in site_results:
        site_name = site_result.get("site", "Unknown Site")
        lines.append(f"## {company_name} — {site_name}")
        lines.append("")

        if "error" in site_result:
            lines.append(f"**Error:** {site_result['error']}")
            lines.append("")
            continue

        # Baseline section
        baseline = site_result.get("baseline", {})
        lines.append(f"### Baseline Parameters ({current_year})")
        lines.append("```json")
        lines.append(json.dumps(baseline, indent=2))
        lines.append("```")
        lines.append("")

        # Forecast section
        forecast = site_result.get("forecast", [])
        lines.append(f"### Forecast Results ({current_year + 1} – {end_year})")
        lines.append("```json")
        lines.append(json.dumps(forecast, indent=2))
        lines.append("```")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Energy report written to %s", report_path)
    return report_path
