"""
DC Energy Prediction - AI-powered data center energy consumption prediction system.

This package uses LLM with RAG (Retrieval-Augmented Generation) to analyze and predict
energy forecasts and expansion locations for major cloud companies.
"""

__version__ = "0.1.0"

# Lazy imports to avoid requiring all dependencies for basic operations
def __getattr__(name):
    if name == "get_company":
        from dc_energy_prediction.config.companies import get_company
        return get_company
    elif name == "get_all_companies":
        from dc_energy_prediction.config.companies import get_all_companies
        return get_all_companies
    elif name == "VectorStoreManager":
        from dc_energy_prediction.data.vector_store import VectorStoreManager
        return VectorStoreManager
    elif name == "EnergyForecaster":
        from dc_energy_prediction.prediction.forecast import EnergyForecaster
        return EnergyForecaster
    elif name == "ExpansionPredictor":
        from dc_energy_prediction.prediction.expansion import ExpansionPredictor
        return ExpansionPredictor
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "get_company",
    "get_all_companies",
    "VectorStoreManager",
    "EnergyForecaster",
    "ExpansionPredictor",
]
