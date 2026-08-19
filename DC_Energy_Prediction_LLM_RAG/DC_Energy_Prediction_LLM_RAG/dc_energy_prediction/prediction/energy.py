"""Energy consumption calculation functions."""

from typing import Any, Dict, List


def compute_energy_with_rag_pue(
    forecast_params: List[Dict[str, Any]],
    grid_factor: float,
) -> List[Dict[str, Any]]:
    """
    Compute energy consumption and CO2 emissions from forecasted parameters.

    This function calculates:
    - E_IT: IT energy consumption (from training and inference workloads)
    - E_DC: Total data center energy (IT energy * PUE)
    - CO2: Carbon dioxide emissions (E_DC * grid factor)

    The formula:
    E_IT = (N_train * P_avg_train * u_train * H_train) + (N_inference * P_avg_inference * u_inference * H_inference)
    E_DC = E_IT * PUE
    CO2 = E_DC * grid_factor

    Args:
        forecast_params: List of parameter dictionaries, each containing:
            - N_train: Number of training accelerators
            - N_inference: Number of inference accelerators
            - P_avg_train: Average power per training accelerator (kW)
            - P_avg_inference: Average power per inference accelerator (kW)
            - u_train: Training utilization rate (0-1)
            - u_inference: Inference utilization rate (0-1)
            - H_train: Training hours per year
            - H_inference: Inference hours per year
            - PUE: Power Usage Effectiveness
        grid_factor: Grid emission factor in tCO2 per MWh

    Returns:
        List of dictionaries with original params plus computed values:
            - E_IT: IT energy consumption (kWh)
            - E_DC: Total data center energy (kWh)
            - grid_factor: The grid emission factor used
            - CO2: CO2 emissions (tonnes)
    """
    results = []

    for p in forecast_params:
        # Calculate IT energy for training and inference
        e_train = p["N_train"] * p["P_avg_train"] * p["u_train"] * p["H_train"]
        e_inference = p["N_inference"] * p["P_avg_inference"] * p["u_inference"] * p["H_inference"]
        e_it = e_train + e_inference

        # Calculate total data center energy using PUE
        e_dc = e_it * p["PUE"]

        # Calculate CO2 emissions
        co2 = e_dc * grid_factor

        results.append({
            **p,
            "E_IT": e_it,
            "E_DC": e_dc,
            "grid_factor": grid_factor,
            "CO2": co2,
            "notes": p.get("notes", ""),
        })

    return results


def extract_grid_factor(params: Dict[str, Any], default: float = 0.43) -> float:
    """
    Extract grid factor from parameters, handling various formats.

    Args:
        params: Parameter dictionary
        default: Default grid factor if not found

    Returns:
        Grid factor value
    """
    grid_factor_field = params.get("grid_factor_tCO2_per_MWh", default)

    if isinstance(grid_factor_field, dict):
        return grid_factor_field.get("value", default)
    elif isinstance(grid_factor_field, (int, float)):
        return grid_factor_field
    else:
        return default
