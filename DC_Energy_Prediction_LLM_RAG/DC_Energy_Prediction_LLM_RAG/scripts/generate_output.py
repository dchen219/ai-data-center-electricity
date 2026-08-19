#!/usr/bin/env python3
"""
Extract prediction data from data_center_llm_rag_all_companies.ipynb
and regenerate output/reports/ using the dc_energy_prediction.reporting module.

This script parses notebook cell outputs to extract:
  - Per-site baseline parameters (JSON)
  - Per-site 5-year energy forecasts (JSON)
  - Per-company expansion predictions (from existing reports)

Then feeds the structured data through the reporting module so the output
looks exactly as if `python main.py --all` had generated it.
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

NOTEBOOK = ROOT / "data_center_llm_rag_all_companies.ipynb"
OUTPUT_DIR = ROOT / "output"
REPORTS_DIR = OUTPUT_DIR / "reports"

# Mapping: cell index -> company key
CELL_MAP = {
    8: "oracle",
    11: "google",
    14: "microsoft",
    17: "apple",
    20: "nebius",
    23: "meta",
}

COMPANY_DISPLAY = {
    "oracle": "Oracle",
    "google": "Google",
    "microsoft": "Microsoft",
    "apple": "Apple",
    "nebius": "Nebius",
    "meta": "Meta",
    "amazon": "Amazon",
    "coreweave": "CoreWeave",
}


# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def _extract_json_block(text: str) -> str | None:
    """Extract content from a ``` or ```json fenced block.

    Handles cases where the closing ``` is missing (truncated output).
    """
    # Try with closing fence first
    m = re.search(r"```(?:json)?\s*\n(.*?)```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    # No closing fence — grab everything after opening fence
    m = re.search(r"```(?:json)?\s*\n(.*)", text, re.DOTALL)
    return m.group(1).strip() if m else None


def _parse_json_permissive(raw: str) -> dict | list | None:
    """Try to parse JSON, handling common LLM quirks."""
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    # Try wrapping in array brackets
    try:
        return json.loads("[" + raw + "]")
    except json.JSONDecodeError:
        pass
    # Try adding missing closing bracket
    stripped = raw.rstrip().rstrip(",")
    for suffix in ["]", "}]", "}}", "}"]:
        try:
            return json.loads(stripped + suffix)
        except json.JSONDecodeError:
            continue
    return None


def compute_energy(entry: dict) -> dict:
    """Add E_IT, E_DC, CO2 to a forecast entry if not present."""
    if "E_IT" in entry and entry["E_IT"]:
        return entry

    N_train = entry.get("N_train", 0)
    N_inf = entry.get("N_inference", 0)
    P_train = entry.get("P_avg_train", entry.get("P_avg_train_kW", 0))
    P_inf = entry.get("P_avg_inference", entry.get("P_avg_inference_kW", 0))
    u_train = entry.get("u_train", 0)
    u_inf = entry.get("u_inference", 0)
    H_train = entry.get("H_train", 0)
    H_inf = entry.get("H_inference", 0)
    pue = entry.get("PUE", entry.get("PUE_current", 1.2))
    gf = entry.get("grid_factor", entry.get("grid_factor_tCO2_per_MWh", 0.4))

    E_IT = (N_train * P_train * u_train * H_train) + (N_inf * P_inf * u_inf * H_inf)
    E_DC = E_IT * pue
    CO2 = E_DC * gf

    entry["E_IT"] = E_IT
    entry["E_DC"] = E_DC
    entry["grid_factor"] = gf
    entry["CO2"] = CO2
    return entry


def extract_energy_from_cell(cell: dict) -> list[dict]:
    """Extract per-site baseline + forecast from a notebook output cell."""
    full_text = ""
    for out in cell.get("outputs", []):
        if out.get("output_type") == "stream":
            full_text += "".join(out.get("text", []))

    # Split by site marker
    site_pattern = r"🔹 Running forecast for .+ - (.+?) \.\.\."
    parts = re.split(site_pattern, full_text)
    # parts: [preamble, site1_name, site1_text, site2_name, site2_text, ...]

    results = []
    for i in range(1, len(parts), 2):
        site_name = parts[i]
        section = parts[i + 1] if i + 1 < len(parts) else ""

        # Extract baseline JSON block
        baseline_match = re.search(
            r"Baseline params raw:\s*\n(.*?)(?=\nmessages=|\n🔹|\nforecast)",
            section, re.DOTALL
        )
        baseline = None
        if baseline_match:
            raw = baseline_match.group(1).strip()
            json_block = _extract_json_block(raw)
            if json_block:
                baseline = _parse_json_permissive(json_block)

        # Extract forecast JSON block
        forecast_match = re.search(
            r"Forecast output raw:\s*\n(.*?)(?=\nforecast param|\n🔹|\n✅)",
            section, re.DOTALL
        )
        forecast = None
        if forecast_match:
            raw = forecast_match.group(1).strip()
            json_block = _extract_json_block(raw)
            if json_block:
                forecast = _parse_json_permissive(json_block)

        # Fallback: parse "forecast param [...]" line (Python repr of list)
        if not forecast:
            fp_match = re.search(r"forecast param (\[.*?\])\s*$", section, re.MULTILINE)
            if fp_match:
                import ast
                try:
                    forecast = ast.literal_eval(fp_match.group(1))
                except (ValueError, SyntaxError):
                    pass

        # Compute E_IT/E_DC/CO2 for forecast entries
        if isinstance(forecast, list):
            # Get grid_factor from baseline if available
            gf = None
            if isinstance(baseline, dict):
                gf = baseline.get("grid_factor_tCO2_per_MWh",
                                  baseline.get("grid_factor"))
            for entry in forecast:
                if gf and "grid_factor" not in entry:
                    entry["grid_factor"] = gf
                compute_energy(entry)

        result = {"site": site_name}
        if baseline:
            result["baseline"] = baseline
        else:
            result["baseline"] = {}
        if forecast:
            result["forecast"] = forecast
        else:
            result["forecast"] = []

        results.append(result)

    return results


# ---------------------------------------------------------------------------
# Expansion prediction extraction (from existing reports)
# ---------------------------------------------------------------------------

def parse_expansion_report(md_path: Path) -> list[dict]:
    """Parse an existing expansion .md report back into structured dicts."""
    if not md_path.exists():
        return []
    text = md_path.read_text(encoding="utf-8")
    predictions = []
    # Pattern: ## N. Location\n**Probability:** XX%\n**Key Factors:** ...\n**Notes:** ...
    blocks = re.split(r"## \d+\.\s+", text)[1:]
    for block in blocks:
        lines = block.strip().split("\n")
        location = lines[0].strip() if lines else "Unknown"
        prob = 0.0
        factors = ""
        notes = ""
        for line in lines[1:]:
            if line.startswith("**Probability:**"):
                prob_str = line.replace("**Probability:**", "").strip().rstrip("%")
                try:
                    prob = float(prob_str) / 100.0
                except ValueError:
                    pass
            elif line.startswith("**Key Factors:**"):
                factors = line.replace("**Key Factors:**", "").strip()
            elif line.startswith("**Notes:**"):
                notes = line.replace("**Notes:**", "").strip()

        predictions.append({
            "location_name": location,
            "estimated_probability": prob,
            "key_factors": factors,
            "notes": notes,
        })
    return predictions


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Reading notebook: {NOTEBOOK}")
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    from dc_energy_prediction.reporting import (
        write_energy_report,
        write_expansion_report,
    )
    from dc_energy_prediction.reporting.combined_report import (
        write_combined_report,
        write_raw_json,
    )

    all_energy: dict[str, list[dict]] = {}
    all_expansion: dict[str, list[dict]] = {}
    company_display: dict[str, str] = {}

    # --- Extract energy forecasts from notebook ---
    for cell_idx, company_key in CELL_MAP.items():
        cell = nb["cells"][cell_idx]
        display = COMPANY_DISPLAY[company_key]
        company_display[company_key] = display

        print(f"\nExtracting {display} (cell {cell_idx})...")
        site_results = extract_energy_from_cell(cell)
        print(f"  {len(site_results)} sites extracted")

        ok = sum(1 for s in site_results if s.get("baseline"))
        print(f"  {ok}/{len(site_results)} with valid baseline")

        all_energy[company_key] = site_results

        # Write per-company energy report
        write_energy_report(display, site_results, REPORTS_DIR, 2025, 5)
        print(f"  -> {company_key}_energy_forecast.md")

    # --- Extract expansion predictions from existing reports ---
    # These were originally LLM-generated; parse them back
    for company_key in list(COMPANY_DISPLAY.keys()):
        display = COMPANY_DISPLAY[company_key]
        if company_key not in company_display:
            company_display[company_key] = display

        existing_path = REPORTS_DIR / f"{company_key}_expansion.md"
        predictions = parse_expansion_report(existing_path)
        if predictions:
            all_expansion[company_key] = predictions
            # Re-write through the reporting module for consistent formatting
            write_expansion_report(display, predictions, REPORTS_DIR)
            print(f"\n  {display}: {len(predictions)} expansion locations (from existing report)")
        else:
            print(f"\n  {display}: no expansion report found")

    # --- Combined report ---
    write_combined_report(
        all_energy, all_expansion, company_display,
        REPORTS_DIR, 2025, 5,
    )
    print(f"\n-> all_companies_forecast.md")

    # --- Raw JSON ---
    all_keys = list(company_display.keys())
    write_raw_json(
        all_energy, all_expansion, all_keys,
        REPORTS_DIR, 2025, 5,
    )
    print(f"-> all_results.json")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("Output generation complete!")
    print(f"Reports directory: {REPORTS_DIR}")
    report_files = sorted(REPORTS_DIR.glob("*.md")) + sorted(REPORTS_DIR.glob("*.json"))
    for f in report_files:
        print(f"  {f.name}")
    print("=" * 60)


if __name__ == "__main__":
    main()
