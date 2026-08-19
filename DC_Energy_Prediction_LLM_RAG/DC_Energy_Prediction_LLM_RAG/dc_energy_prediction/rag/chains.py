"""LangChain chain builders for RAG operations."""

from typing import Any, Callable, Dict, Optional

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAI

from dc_energy_prediction.config.settings import get_settings
from dc_energy_prediction.rag.prompts import (
    BASELINE_EXTRACTION_PROMPT,
    FORECAST_PROMPT,
    EXPANSION_PREDICTION_PROMPT,
)
from dc_energy_prediction.rag.retriever import RAGRetriever, format_docs


class RAGChainBuilder:
    """Builder for RAG chains using LangChain."""

    def __init__(
        self,
        db_name: str,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        verbose: bool = False,
    ):
        """
        Initialize the RAGChainBuilder.

        Args:
            db_name: Name of the FAISS database
            model: OpenAI model name
            temperature: Model temperature
            max_tokens: Maximum tokens for response
            verbose: Whether to print debug information
        """
        settings = get_settings()
        settings.validate()

        self.db_name = db_name
        self.model = model or settings.openai_model
        self.temperature = temperature if temperature is not None else settings.openai_temperature
        self.max_tokens = max_tokens or settings.openai_max_tokens
        self.verbose = verbose

        self._llm = None
        self._retriever = None

    @property
    def llm(self) -> OpenAI:
        """Get or create the LLM instance."""
        if self._llm is None:
            self._llm = OpenAI(
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
        return self._llm

    @property
    def retriever(self) -> RAGRetriever:
        """Get or create the retriever instance."""
        if self._retriever is None:
            self._retriever = RAGRetriever(self.db_name)
        return self._retriever

    def _debug_prompt(self, input_data: Any) -> Any:
        """Debug callback to print prompts."""
        if self.verbose:
            print("--- Final prompt going into LLM ---")
            print(input_data)
            print("-----------------------------------")
        return input_data

    def build_baseline_chain(self):
        """
        Build a chain for extracting baseline parameters.

        Returns:
            Configured LangChain runnable
        """
        def get_context(inputs: Dict[str, Any]) -> str:
            docs = self.retriever.retrieve_for_baseline(
                inputs["company_name"],
                inputs["site_name"],
                inputs["current_year"],
            )
            return format_docs(docs)

        chain = (
            RunnableParallel({
                "context": get_context,
                "company_name": lambda x: x["company_name"],
                "site_name": lambda x: x["site_name"],
                "current_year": lambda x: x["current_year"],
            })
            | BASELINE_EXTRACTION_PROMPT
            | self._debug_prompt
            | self.llm
            | StrOutputParser()
        )

        return chain

    def build_forecast_chain(self):
        """
        Build a chain for generating forecasts.

        Returns:
            Configured LangChain runnable
        """
        def get_context(inputs: Dict[str, Any]) -> str:
            docs = self.retriever.retrieve_for_forecast(
                inputs["company_name"],
                inputs["site_name"],
            )
            return format_docs(docs)

        chain = (
            RunnableParallel({
                "context": get_context,
                "param_json": lambda x: x["param_json"],
                "company_name": lambda x: x["company_name"],
                "site_name": lambda x: x["site_name"],
                "current_year": lambda x: x["current_year"],
                "forecast_horizon": lambda x: x["forecast_horizon"],
            })
            | FORECAST_PROMPT
            | self._debug_prompt
            | self.llm
            | StrOutputParser()
        )

        return chain

    def build_expansion_chain(self):
        """
        Build a chain for predicting expansion locations.

        Returns:
            Configured LangChain runnable
        """
        def get_context(inputs: Dict[str, Any]) -> str:
            docs = self.retriever.retrieve_for_expansion(inputs["company_name"])
            return format_docs(docs)

        chain = (
            RunnableParallel({
                "context": get_context,
                "company_name": lambda x: x["company_name"],
                "question": lambda x: x["question"],
            })
            | EXPANSION_PREDICTION_PROMPT
            | self._debug_prompt
            | self.llm
            | StrOutputParser()
        )

        return chain
