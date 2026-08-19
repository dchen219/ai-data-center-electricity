"""Document ingestion pipeline: URL fetching, parsing, and FAISS vectorization."""

import csv
import logging
import re
from pathlib import Path
from typing import Callable, List, Optional

from langchain_core.documents import Document

from dc_energy_prediction.config.companies import CompanyConfig
from dc_energy_prediction.data.document_loader import chunk_documents, load_pdf_documents
from dc_energy_prediction.data.vector_store import VectorStoreManager

logger = logging.getLogger(__name__)

_USER_AGENT = (
    "Mozilla/5.0 (compatible; DCEnergyBot/1.0; "
    "+https://github.com/dc-energy-prediction)"
)


def fetch_and_parse_url(url: str, timeout: int = 20) -> Optional[str]:
    """
    Fetch a URL and extract readable text content from its HTML.

    Args:
        url: The URL to fetch.
        timeout: Request timeout in seconds.

    Returns:
        Extracted text if longer than 100 characters, otherwise None.
    """
    try:
        import requests
        from bs4 import BeautifulSoup

        response = requests.get(
            url, timeout=timeout, headers={"User-Agent": _USER_AGENT}
        )
        response.raise_for_status()

        # Prefer lxml parser for speed; fall back to html.parser
        try:
            soup = BeautifulSoup(response.text, "lxml")
        except Exception:
            soup = BeautifulSoup(response.text, "html.parser")

        # Remove non-content elements
        for tag in soup.find_all(["nav", "footer", "script", "style"]):
            tag.decompose()

        # Extract paragraphs from the most specific content container available
        container = soup.find("main") or soup.find("article") or soup.find("body")
        if container is None:
            return None

        paragraphs = container.find_all("p")
        text = "\n".join(p.get_text(strip=True) for p in paragraphs)

        if len(text) > 100:
            return text
        return None

    except Exception:
        logger.debug("Failed to fetch or parse URL: %s", url, exc_info=True)
        return None


def _load_txt_documents(folder: Path) -> List[Document]:
    """Load all .txt files in *folder* as LangChain Documents."""
    docs: List[Document] = []
    if not folder.is_dir():
        return docs
    for txt_path in sorted(folder.glob("*.txt")):
        try:
            content = txt_path.read_text(encoding="utf-8", errors="replace")
            if content.strip():
                docs.append(
                    Document(
                        page_content=content,
                        metadata={"source": str(txt_path)},
                    )
                )
        except Exception:
            logger.warning("Could not read %s", txt_path, exc_info=True)
    return docs


def _read_urls_from_csv(csv_path: Path) -> List[str]:
    """Read URLs from a single-column (or first-column) CSV file."""
    urls: List[str] = []
    if not csv_path.is_file():
        return urls
    with open(csv_path, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        for row in reader:
            if not row:
                continue
            candidate = row[0].strip()
            if candidate.startswith("http"):
                urls.append(candidate)
    return urls


def _safe_filename(url: str) -> str:
    """Derive a filesystem-safe filename from a URL."""
    name = re.sub(r"[^a-zA-Z0-9]", "_", url)
    # Truncate to a reasonable length and add .txt extension
    return name[:120] + ".txt"


def ingest_documents_for_company(
    company: CompanyConfig,
    urls_dir: Path,
    docs_dir: Path,
    faiss_dir: Path,
    max_docs: int = 50,
    verbose: bool = False,
    shutdown_check: Optional[Callable[[], bool]] = None,
) -> bool:
    """
    End-to-end ingestion for a single company: load local docs, fetch URLs,
    chunk everything, and build a FAISS vector store.

    Args:
        company: CompanyConfig describing the target company.
        urls_dir: Directory containing ``<company_key>_urls.csv`` files.
        docs_dir: Directory where per-company document folders live and
            where fetched URL text is saved for reproducibility.
        faiss_dir: Base directory for FAISS databases.
        max_docs: Maximum number of URLs to fetch.
        verbose: Enable verbose logging.
        shutdown_check: Optional callable that returns True when the caller
            wants to abort early. Checked between URL fetches.

    Returns:
        True if the FAISS store was created successfully, False if no
        documents were found.
    """
    company_key = company.name.lower()
    company_docs_dir = Path(docs_dir) / company.pdf_folder
    all_documents: List[Document] = []

    # --- 1. Load existing .txt files ---
    txt_docs = _load_txt_documents(company_docs_dir)
    if txt_docs:
        logger.info(
            "Loaded %d existing .txt document(s) for %s", len(txt_docs), company.name
        )
        all_documents.extend(txt_docs)

    # --- 2. Load existing .pdf files (requires docling) ---
    try:
        pdf_docs = load_pdf_documents(company_docs_dir, verbose=verbose)
        if pdf_docs:
            logger.info(
                "Loaded %d PDF document(s) for %s", len(pdf_docs), company.name
            )
            all_documents.extend(pdf_docs)
    except ImportError:
        logger.info(
            "docling not installed; skipping PDF loading for %s", company.name
        )

    # --- 3. Fetch URLs and save fetched text ---
    urls_path = Path(urls_dir) / f"{company_key}_urls.csv"
    urls = _read_urls_from_csv(urls_path)
    if urls:
        logger.info("Found %d URL(s) for %s in %s", len(urls), company.name, urls_path)
        fetched = 0
        company_docs_dir.mkdir(parents=True, exist_ok=True)

        for url in urls:
            if fetched >= max_docs:
                break

            if shutdown_check is not None and shutdown_check():
                logger.info("Shutdown requested; stopping URL fetches for %s", company.name)
                break

            text = fetch_and_parse_url(url)
            if text is None:
                logger.debug("No usable content from %s", url)
                continue

            # Persist fetched text for reproducibility
            out_path = company_docs_dir / _safe_filename(url)
            try:
                out_path.write_text(text, encoding="utf-8")
            except Exception:
                logger.warning("Could not save fetched text to %s", out_path, exc_info=True)

            all_documents.append(
                Document(page_content=text, metadata={"source": url})
            )
            fetched += 1

        logger.info("Fetched %d URL document(s) for %s", fetched, company.name)
    else:
        logger.debug("No URL CSV found or no URLs for %s at %s", company.name, urls_path)

    # --- 4. Bail out if nothing was collected ---
    if not all_documents:
        logger.warning("No documents found for %s; skipping FAISS creation", company.name)
        return False

    # --- 5. Chunk documents ---
    chunks = chunk_documents(all_documents, verbose=verbose)
    if not chunks:
        logger.warning("Chunking produced no output for %s", company.name)
        return False

    logger.info("Produced %d chunk(s) for %s", len(chunks), company.name)

    # --- 6. Build FAISS vector store ---
    vs_manager = VectorStoreManager(base_path=faiss_dir)
    vs_manager.create(chunks, company.faiss_db_name, verbose=verbose)

    logger.info(
        "FAISS store '%s' created for %s at %s",
        company.faiss_db_name,
        company.name,
        faiss_dir,
    )
    return True
