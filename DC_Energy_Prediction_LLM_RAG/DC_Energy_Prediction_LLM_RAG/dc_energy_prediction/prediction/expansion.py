"""Expansion location prediction."""

import json
from typing import Any, Dict, List, Optional, Union

from dc_energy_prediction.config.companies import CompanyConfig, get_company
from dc_energy_prediction.rag.chains import RAGChainBuilder
from dc_energy_prediction.utils.json_utils import extract_json_from_text


class ExpansionPredictor:
    """Predicts data center expansion locations using RAG."""

    def __init__(
        self,
        company: Union[str, CompanyConfig],
        verbose: bool = False,
    ):
        """
        Initialize the ExpansionPredictor.

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

    def predict_expansion_locations(
        self,
        probability_threshold: float = 0.0,
        years_ahead: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Predict expansion locations for the company.

        Args:
            probability_threshold: Minimum probability to include in results
            years_ahead: Time horizon for predictions

        Returns:
            List of predicted locations with probabilities and factors
        """
        chain = self.chain_builder.build_expansion_chain()

        question = (
            f"Predict the top potential locations where {self.company.name} will likely "
            f"build new data centers by {2025 + years_ahead}. "
            "Do not just list country, please list out the city as well."
        )

        if self.verbose:
            print(f"Predicting expansion locations for {self.company.name}...")

        result = chain.invoke({
            "company_name": self.company.name,
            "question": question,
        })

        if self.verbose:
            print(f"Expansion prediction raw:\n{result}")

        try:
            predictions = json.loads(extract_json_from_text(result))
        except Exception as e:
            if self.verbose:
                print(f"Failed to parse expansion predictions: {e}")
            return []

        # Ensure we have a list
        if isinstance(predictions, dict):
            predictions = [predictions]

        # Filter by threshold
        if probability_threshold > 0:
            predictions = [
                p for p in predictions
                if p.get("estimated_probability", 0) >= probability_threshold
            ]

        return predictions

    def format_predictions_markdown(
        self,
        predictions: List[Dict[str, Any]],
    ) -> str:
        """
        Format predictions as markdown.

        Args:
            predictions: List of prediction dictionaries

        Returns:
            Formatted markdown string
        """
        lines = [f"# {self.company.name} - Expansion Location Predictions\n"]

        for i, pred in enumerate(predictions, 1):
            location = pred.get("location_name", "Unknown")
            probability = pred.get("estimated_probability", 0)
            factors = pred.get("key_factors", "N/A")
            notes = pred.get("notes", "")

            lines.append(f"## {i}. {location}")
            lines.append(f"**Probability:** {probability:.0%}")
            lines.append(f"**Key Factors:** {factors}")
            if notes:
                lines.append(f"**Notes:** {notes}")
            lines.append("")

        return "\n".join(lines)


def predict_expansion_for_company(
    company: Union[str, CompanyConfig],
    probability_threshold: float = 0.0,
    years_ahead: int = 5,
    verbose: bool = False,
) -> List[Dict[str, Any]]:
    """
    Convenience function to predict expansion locations.

    Args:
        company: Company name or CompanyConfig
        probability_threshold: Minimum probability to include
        years_ahead: Time horizon for predictions
        verbose: Whether to print progress

    Returns:
        List of predicted locations
    """
    predictor = ExpansionPredictor(company, verbose=verbose)
    return predictor.predict_expansion_locations(
        probability_threshold=probability_threshold,
        years_ahead=years_ahead,
    )
