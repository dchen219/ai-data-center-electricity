"""Expansion location prediction report generation."""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def write_expansion_report(
    company_name: str,
    predictions: list[dict],
    output_dir: Path,
) -> Path:
    """Write a Markdown expansion-location prediction report for a single company.

    Args:
        company_name: Display name of the company (e.g. "Google").
        predictions: Ranked list of expansion predictions.  Each dict contains:
            - "location_name" (str)
            - "estimated_probability" (float, 0.0–1.0)
            - "key_factors" (str)
            - "notes" (str)
        output_dir: Directory where the report file will be written.

    Returns:
        Path to the written report file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    company_key = company_name.lower().replace(" ", "_")
    report_path = output_dir / f"{company_key}_expansion.md"

    lines: list[str] = []
    lines.append(f"# {company_name} — Expansion Location Predictions")
    lines.append("")

    for idx, pred in enumerate(predictions, start=1):
        location = pred.get("location_name", "Unknown")
        probability = pred.get("estimated_probability", 0.0)
        factors = pred.get("key_factors", "N/A")
        notes = pred.get("notes", "N/A")

        lines.append(f"## {idx}. {location}")
        lines.append(f"**Probability:** {probability:.0%}")
        lines.append(f"**Key Factors:** {factors}")
        lines.append(f"**Notes:** {notes}")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Expansion report written to %s", report_path)
    return report_path
