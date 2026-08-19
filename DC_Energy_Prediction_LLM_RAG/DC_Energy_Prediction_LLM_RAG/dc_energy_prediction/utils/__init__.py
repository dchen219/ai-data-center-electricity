"""Utility functions for DC Energy Prediction."""

# Lazy imports to avoid requiring pandas for basic operations
def __getattr__(name):
    if name == "get_soup":
        from dc_energy_prediction.utils.scraping import get_soup
        return get_soup
    elif name == "scrape_locations":
        from dc_energy_prediction.utils.scraping import scrape_locations
        return scrape_locations
    elif name == "extract_json_from_text":
        from dc_energy_prediction.utils.json_utils import extract_json_from_text
        return extract_json_from_text
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    "get_soup",
    "scrape_locations",
    "extract_json_from_text",
]
