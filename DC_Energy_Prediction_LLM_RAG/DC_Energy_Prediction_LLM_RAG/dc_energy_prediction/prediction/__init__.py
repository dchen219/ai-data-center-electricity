"""Energy prediction and forecasting modules."""

# Lazy imports to avoid requiring all dependencies for basic operations
def __getattr__(name):
    if name == "compute_energy_with_rag_pue":
        from dc_energy_prediction.prediction.energy import compute_energy_with_rag_pue
        return compute_energy_with_rag_pue
    elif name == "EnergyForecaster":
        from dc_energy_prediction.prediction.forecast import EnergyForecaster
        return EnergyForecaster
    elif name == "run_forecasts_for_company":
        from dc_energy_prediction.prediction.forecast import run_forecasts_for_company
        return run_forecasts_for_company
    elif name == "ExpansionPredictor":
        from dc_energy_prediction.prediction.expansion import ExpansionPredictor
        return ExpansionPredictor
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "compute_energy_with_rag_pue",
    "EnergyForecaster",
    "run_forecasts_for_company",
    "ExpansionPredictor",
]
