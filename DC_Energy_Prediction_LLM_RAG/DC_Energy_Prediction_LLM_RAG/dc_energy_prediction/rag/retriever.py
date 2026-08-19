"""RAG retriever utilities."""

import json
from typing import Any, Dict, List, Optional, Union

from langchain_core.documents import Document

from dc_energy_prediction.data.vector_store import VectorStoreManager
from dc_energy_prediction.config.settings import get_settings


class RAGRetriever:
    """Retriever for RAG-based queries against vector stores."""

    def __init__(
        self,
        db_name: str,
        search_type: str = "similarity",
        k: int = 20,
    ):
        """
        Initialize the RAGRetriever.

        Args:
            db_name: Name of the FAISS database to use
            search_type: Type of search (similarity, mmr, etc.)
            k: Number of documents to retrieve
        """
        self.db_name = db_name
        self.search_type = search_type
        self.k = k
        self._vector_store_manager = VectorStoreManager()
        self._retriever = None

    @property
    def retriever(self):
        """Get or create the retriever instance."""
        if self._retriever is None:
            self._retriever = self._vector_store_manager.get_retriever(
                self.db_name,
                search_type=self.search_type,
                k=self.k,
            )
        return self._retriever

    def retrieve(self, query: str) -> List[Document]:
        """
        Retrieve relevant documents for a query.

        Args:
            query: The query string

        Returns:
            List of relevant documents
        """
        return self.retriever.invoke(query)

    def retrieve_for_baseline(
        self,
        company_name: str,
        site_name: str,
        year: int,
    ) -> List[Document]:
        """
        Retrieve documents for baseline parameter extraction.

        Args:
            company_name: Company name
            site_name: Data center site name
            year: Year of interest

        Returns:
            List of relevant documents
        """
        query = f"{company_name} {site_name} {year} data center energy PUE N_train N_inference"
        return self.retrieve(query)

    def retrieve_for_forecast(
        self,
        company_name: str,
        site_name: str,
    ) -> List[Document]:
        """
        Retrieve documents for forecasting.

        Args:
            company_name: Company name
            site_name: Data center site name

        Returns:
            List of relevant documents
        """
        query = f"{company_name} {site_name} data center energy historical trends PUE utilization IT infrastructure"
        return self.retrieve(query)

    def retrieve_for_expansion(
        self,
        company_name: str,
    ) -> List[Document]:
        """
        Retrieve documents for expansion prediction.

        Args:
            company_name: Company name

        Returns:
            List of relevant documents
        """
        query = f"{company_name} data center expansion plans infrastructure investment locations growth"
        return self.retrieve(query)


def format_docs(docs: Any) -> str:
    """
    Format documents into a single string for LLM context.

    Args:
        docs: Documents to format (can be list of Documents, str, or dict)

    Returns:
        Formatted string
    """
    if isinstance(docs, str):
        return docs
    elif isinstance(docs, list):
        return "\n\n".join(
            [getattr(doc, "page_content", str(doc)) for doc in docs]
        )
    elif isinstance(docs, dict):
        return json.dumps(docs, indent=2)
    else:
        return str(docs)
