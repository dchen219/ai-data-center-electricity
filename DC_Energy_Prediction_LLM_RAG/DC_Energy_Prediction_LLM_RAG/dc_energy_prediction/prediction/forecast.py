"""Energy forecasting orchestration."""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

from dc_energy_prediction.config.companies import CompanyConfig, get_company
from dc_energy_prediction.prediction.energy import compute_energy_with_rag_pue, extract_grid_factor
from dc_energy_prediction.rag.chains import RAGChainBuilder
from dc_energy_prediction.utils.json_utils import extract_json_from_text


class EnergyForecaster:
    """Orchestrates energy forecasting for data centers using RAG."""

    def __init__(
        self,
        company: Union[str, CompanyConfig],
        verbose: bool = False,
    ):
        """
        Initialize the EnergyForecaster.

        Args:
            company: Company name or CompanyConfig object
            verbose: Whether to print progress
        """
        if isinstance(company, str):
            config = get_company(company)
            if config is None:
                raise ValueError(f"Unknown company: {company}")
            self.company = config
        else:
            self.company = company

        self.verbose = verbose
        self._chain_builder: Optional[RAGChainBuilder] = None

    @property
    def chain_builder(self) -> RAGChainBuilder:
        """Get or create the chain builder."""
        if self._chain_builder is None:
            self._chain_builder = RAGChainBuilder(
                db_name=self.company.faiss_db_name,
                verbose=self.verbose,
            )
        return self._chain_builder

    def extract_baseline_params(
        self,
        site_name: str,
        year: int,
    ) -> Dict[str, Any]:
        """
        Extract baseline parameters for a data center site.

        Args:
            site_name: Name of the data center site
            year: Year for baseline extraction

        Returns:
            Dictionary of baseline parameters
        """
        chain = self.chain_builder.build_baseline_chain()

        if self.verbose:
            print(f"Extracting baseline parameters for {self.company.name} - {site_name}...")

        result = chain.invoke({
            "company_name": self.company.name,
            "site_name": site_name,
            "current_year": year,
        })

        if self.verbose:
            print(f"Baseline params raw:\n{result}")

        try:
            params = json.loads(extract_json_from_text(result))
        except Exception as e:
            if self.verbose:
                print(f"Failed to parse baseline params: {e}")
            params = {}

        return params

    def forecast_future_params(
        self,
        site_name: str,
        baseline_params: Dict[str, Any],
        year: int,
        horizon: int,
    ) -> List[Dict[str, Any]]:
        """
        Forecast future parameters based on baseline.

        Args:
            site_name: Name of the data center site
            baseline_params: Baseline parameters from extraction
            year: Starting year
            horizon: Number of years to forecast

        Returns:
            List of forecasted parameter dictionaries
        """
        chain = self.chain_builder.build_forecast_chain()

        if self.verbose:
            print(f"Forecasting {horizon} years for {self.company.name} - {site_name}...")

        result = chain.invoke({
            "param_json": json.dumps(baseline_params),
            "company_name": self.company.name,
            "site_name": site_name,
            "current_year": year,
            "forecast_horizon": horizon,
        })

        if self.verbose:
            print(f"Forecast output raw:\n{result}")

        try:
            forecast_params = json.loads(extract_json_from_text(result))
        except Exception as e:
            if self.verbose:
                print(f"JSON parse error in forecast: {e}")
            forecast_params = []

        return forecast_params

    def run_full_forecast(
        self,
        site_name: str,
        year: int,
        horizon: int,
    ) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Run full forecasting pipeline for a site.

        Args:
            site_name: Name of the data center site
            year: Current year for baseline
            horizon: Number of years to forecast

        Returns:
            Tuple of (baseline_params, forecast_results)
        """
        # Step 1: Extract baseline parameters
        params = self.extract_baseline_params(site_name, year)

        # Step 2: Forecast future parameters
        forecast_params = self.forecast_future_params(site_name, params, year, horizon)

        # Step 3: Compute energy with PUE
        grid_factor = extract_grid_factor(params)

        if self.verbose:
            print(f"Grid factor: {grid_factor}")

        if isinstance(forecast_params, list):
            forecast_results = compute_energy_with_rag_pue(forecast_params, grid_factor)
        else:
            forecast_results = forecast_params

        return params, forecast_results


def run_forecasts_for_company(
    company: Union[str, CompanyConfig],
    year: int = 2025,
    horizon: int = 5,
    output_path: Optional[Union[str, Path]] = None,
    verbose: bool = False,
) -> str:
    """
    Run forecasts for all data centers of a company.

    Args:
        company: Company name or CompanyConfig
        year: Current year for baseline
        horizon: Number of years to forecast
        output_path: Optional path to save markdown results
        verbose: Whether to print progress

    Returns:
        Markdown string with all results
    """
    if isinstance(company, str):
        config = get_company(company)
        if config is None:
            raise ValueError(f"Unknown company: {company}")
    else:
        config = company

    forecaster = EnergyForecaster(config, verbose=verbose)
    all_results_md = []

    for dc in config.data_centers:
        if verbose:
            print(f"\nRunning forecast for {dc.company_name} - {dc.site_name}...")

        try:
            params, forecast_results = forecaster.run_full_forecast(
                dc.site_name,
                year,
                horizon,
            )

            forecast_results_json = json.dumps(forecast_results, indent=2)

            md_section = f"# {dc.company_name} - {dc.site_name}\n\n"
            md_section += f"## Baseline Parameters ({year})\n```json\n{json.dumps(params, indent=2)}\n```\n\n"
            md_section += f"## Forecast Results ({year+1} - {year+horizon})\n```json\n{forecast_results_json}\n```\n"

            all_results_md.append(md_section)

        except Exception as e:
            if verbose:
                print(f"Failed to forecast {dc.site_name}: {e}")
            md_section = f"# {dc.company_name} - {dc.site_name}\n\n"
            md_section += f"**Error:** {str(e)}\n"
            all_results_md.append(md_section)

    final_md = "\n\n".join(all_results_md)

    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(final_md)

        if verbose:
            print(f"\nForecasts written to {output_path}")

    return final_md
