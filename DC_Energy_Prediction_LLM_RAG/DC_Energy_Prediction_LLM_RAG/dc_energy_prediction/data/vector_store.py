"""FAISS vector store management."""

from pathlib import Path
from typing import List, Optional, Union

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from dc_energy_prediction.config.settings import get_settings


def _create_embeddings(model_name: str):
    """Create embeddings instance, falling back to OpenAI if HuggingFace fails."""
    try:
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=model_name)
    except Exception:
        # Fall back to OpenAI embeddings when HuggingFace/sentence-transformers
        # has dependency issues (e.g., broken numba, sklearn incompatibility)
        import os
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=os.environ.get("OPENAI_API_KEY", ""),
        )


class VectorStoreManager:
    """Manager for FAISS vector store operations."""

    def __init__(
        self,
        embedding_model: Optional[str] = None,
        base_path: Optional[Union[str, Path]] = None,
    ):
        """
        Initialize the VectorStoreManager.

        Args:
            embedding_model: HuggingFace embedding model name
            base_path: Base path for FAISS databases
        """
        settings = get_settings()
        self.embedding_model = embedding_model or settings.embedding_model
        self.base_path = Path(base_path) if base_path else settings.faiss_db_dir
        self._embeddings = None

    @property
    def embeddings(self):
        """Get or create the embeddings instance."""
        if self._embeddings is None:
            self._embeddings = _create_embeddings(self.embedding_model)
        return self._embeddings

    def _get_db_path(self, db_name: str) -> Path:
        """Get the full path for a database."""
        return self.base_path / db_name

    def exists(self, db_name: str) -> bool:
        """
        Check if a FAISS database exists.

        Args:
            db_name: Name of the database

        Returns:
            True if the database exists
        """
        db_path = self._get_db_path(db_name)
        return db_path.exists() and (db_path / "index.faiss").exists()

    def load(self, db_name: str) -> FAISS:
        """
        Load an existing FAISS database.

        Args:
            db_name: Name of the database to load

        Returns:
            Loaded FAISS vector store

        Raises:
            FileNotFoundError: If the database doesn't exist
        """
        db_path = self._get_db_path(db_name)

        if not self.exists(db_name):
            raise FileNotFoundError(f"FAISS database not found at {db_path}")

        return FAISS.load_local(
            folder_path=str(db_path),
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True,
        )

    def create(
        self,
        documents: List[Document],
        db_name: str,
        verbose: bool = False,
    ) -> FAISS:
        """
        Create a new FAISS database from documents.

        Args:
            documents: List of documents to embed
            db_name: Name for the new database
            verbose: Whether to print progress

        Returns:
            Created FAISS vector store
        """
        if verbose:
            print(f"Creating embeddings for {len(documents)} documents...")

        db_path = self._get_db_path(db_name)
        db_path.mkdir(parents=True, exist_ok=True)

        vector_db = FAISS.from_documents(documents, self.embeddings)

        if verbose:
            print(f"Saving FAISS database to {db_path}...")

        vector_db.save_local(str(db_path))

        if verbose:
            print(f"FAISS database created successfully at {db_path}")

        return vector_db

    def add_documents(
        self,
        db_name: str,
        documents: List[Document],
        verbose: bool = False,
    ) -> FAISS:
        """
        Add documents to an existing FAISS database.

        Args:
            db_name: Name of the database to update
            documents: Documents to add
            verbose: Whether to print progress

        Returns:
            Updated FAISS vector store
        """
        db_path = self._get_db_path(db_name)

        if self.exists(db_name):
            if verbose:
                print(f"Loading existing FAISS database from {db_path}...")
            vector_db = self.load(db_name)

            if verbose:
                print(f"Adding {len(documents)} documents...")
            vector_db.add_documents(documents)
        else:
            if verbose:
                print(f"Creating new FAISS database at {db_path}...")
            vector_db = FAISS.from_documents(documents, self.embeddings)

        if verbose:
            print(f"Saving updated FAISS database...")
        vector_db.save_local(str(db_path))

        if verbose:
            print(f"FAISS database updated successfully")

        return vector_db

    def get_retriever(
        self,
        db_name: str,
        search_type: str = "similarity",
        k: int = 20,
    ):
        """
        Get a retriever for a FAISS database.

        Args:
            db_name: Name of the database
            search_type: Type of search (similarity, mmr, etc.)
            k: Number of documents to retrieve

        Returns:
            Configured retriever
        """
        vector_db = self.load(db_name)
        return vector_db.as_retriever(
            search_type=search_type,
            search_kwargs={"k": k},
        )
