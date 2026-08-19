"""Global settings and configuration for DC Energy Prediction."""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class Settings:
    """Global settings for the DC Energy Prediction system."""

    # OpenAI Configuration
    openai_api_key: str = field(default_factory=lambda: os.environ.get("OPENAI_API_KEY", ""))
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.3
    openai_max_tokens: int = 4000

    # Embedding Configuration
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Retriever Configuration
    retriever_search_type: str = "similarity"
    retriever_k: int = 20

    # Data Paths
    data_dir: Path = field(
        default_factory=lambda: Path(os.environ.get("DC_ENERGY_DATA_DIR", "./data"))
    )

    @property
    def faiss_db_dir(self) -> Path:
        """Path to FAISS vector databases directory."""
        return self.data_dir / "faiss_dbs"

    @property
    def documents_dir(self) -> Path:
        """Path to source documents directory."""
        return self.data_dir / "documents"

    @property
    def output_dir(self) -> Path:
        """Path to output directory for generated forecasts."""
        return self.data_dir / "output"

    @property
    def urls_dir(self) -> Path:
        """Path to collected URLs directory."""
        return self.data_dir / "collected_urls"

    @property
    def reports_dir(self) -> Path:
        """Path to generated reports directory."""
        return self.data_dir / "reports"

    def get_faiss_db_path(self, company_name: str) -> Path:
        """Get the FAISS DB path for a specific company."""
        db_name = f"{company_name.lower()}_faiss_db"
        return self.faiss_db_dir / db_name

    def get_documents_path(self, company_name: str) -> Path:
        """Get the documents path for a specific company."""
        folder_name = f"{company_name.lower()}_related"
        return self.documents_dir / folder_name

    def validate(self) -> None:
        """Validate that required settings are configured."""
        if not self.openai_api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable is not set. "
                "Please set it before running predictions."
            )

    def ensure_directories(self) -> None:
        """Create required directories if they don't exist."""
        self.faiss_db_dir.mkdir(parents=True, exist_ok=True)
        self.documents_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.urls_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)


# Global settings instance
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    """Get the global settings instance."""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


def configure_settings(**kwargs) -> Settings:
    """Configure global settings with custom values."""
    global _settings
    _settings = Settings(**kwargs)
    return _settings
