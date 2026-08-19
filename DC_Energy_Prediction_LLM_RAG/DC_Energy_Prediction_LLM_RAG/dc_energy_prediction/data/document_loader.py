"""Document loading utilities for PDF and CSV files."""

import glob
from pathlib import Path
from typing import List, Optional, Union

from langchain_core.documents import Document

# Lazy imports to avoid triggering broken numba/sentence_transformers chain
_RecursiveCharacterTextSplitter = None
_CSVLoader = None


def _get_text_splitter_class():
    global _RecursiveCharacterTextSplitter
    if _RecursiveCharacterTextSplitter is None:
        # Import from submodule directly to avoid langchain_text_splitters.__init__
        # which triggers sentence_transformers and its broken dependency chain
        from langchain_text_splitters.character import RecursiveCharacterTextSplitter
        _RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter
    return _RecursiveCharacterTextSplitter


def _get_csv_loader_class():
    global _CSVLoader
    if _CSVLoader is None:
        from langchain_community.document_loaders import CSVLoader
        _CSVLoader = CSVLoader
    return _CSVLoader

# Optional docling import
try:
    from langchain_docling import DoclingLoader
    from langchain_docling.loader import ExportType

    DOCLING_AVAILABLE = True
except ImportError:
    DOCLING_AVAILABLE = False


def load_pdf_documents(
    folder_path: Union[str, Path],
    recursive: bool = True,
    verbose: bool = False,
) -> List[Document]:
    """
    Load PDF documents from a folder using DoclingLoader.

    Args:
        folder_path: Path to the folder containing PDFs
        recursive: Whether to search subdirectories
        verbose: Whether to print progress

    Returns:
        List of loaded Document objects

    Raises:
        ImportError: If docling is not installed
    """
    if not DOCLING_AVAILABLE:
        raise ImportError(
            "docling is required for PDF loading. "
            "Install it with: pip install langchain-docling docling"
        )

    folder_path = Path(folder_path)
    pattern = f"{folder_path}/**/*.pdf" if recursive else f"{folder_path}/*.pdf"
    pdf_files = glob.glob(pattern, recursive=recursive)

    all_docs: List[Document] = []
    successful_files = 0

    for pdf_file in pdf_files:
        try:
            if verbose:
                print(f"Loading: {pdf_file}")

            loader = DoclingLoader(file_path=pdf_file, export_type=ExportType.MARKDOWN)
            docs = loader.load()
            all_docs.extend(docs)
            successful_files += 1

            if verbose:
                print(f"  Successfully loaded {len(docs)} documents")

        except Exception as e:
            if verbose:
                print(f"  Failed to load {pdf_file}: {str(e)}")

    if verbose:
        print(f"\n--- Document Loading Summary ---")
        print(f"Total PDF files found: {len(pdf_files)}")
        print(f"Successfully loaded files: {successful_files}")
        print(f"Total documents loaded: {len(all_docs)}")

    return all_docs


def load_csv_documents(
    file_path: Union[str, Path],
    source_column: Optional[str] = None,
    verbose: bool = False,
) -> List[Document]:
    """
    Load documents from a CSV file.

    Args:
        file_path: Path to the CSV file
        source_column: Optional column to use as document source
        verbose: Whether to print progress

    Returns:
        List of loaded Document objects
    """
    file_path = Path(file_path)

    if verbose:
        print(f"Loading CSV: {file_path}")

    kwargs = {}
    if source_column:
        kwargs["source_column"] = source_column

    CSVLoader = _get_csv_loader_class()
    loader = CSVLoader(str(file_path), **kwargs)
    docs = loader.load()

    if verbose:
        print(f"  Loaded {len(docs)} documents from CSV")

    return docs


def chunk_documents(
    documents: List[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    verbose: bool = False,
) -> List[Document]:
    """
    Split documents into smaller chunks for embedding.

    Args:
        documents: List of documents to chunk
        chunk_size: Maximum size of each chunk
        chunk_overlap: Overlap between consecutive chunks
        verbose: Whether to print progress

    Returns:
        List of chunked Document objects
    """
    if verbose:
        print(f"Chunking {len(documents)} documents...")

    RecursiveCharacterTextSplitter = _get_text_splitter_class()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = text_splitter.split_documents(documents)

    if verbose:
        print(f"  Created {len(chunks)} chunks")

    return chunks
