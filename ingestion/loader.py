# ingestion/loader.py

from langchain_community.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader
)


def load_from_web(url: str):
    loader = WebBaseLoader(url)
    documents = loader.load()
    return documents


def load_from_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def load_from_text(file_path: str):
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents


def load_documents(source: str, source_type: str):
    """
    Unified loader function

    Args:
        source: URL or file path
        source_type: "web", "pdf", "text"

    Returns:
        List of Document objects
    """

    if source_type == "web":
        return load_from_web(source)

    elif source_type == "pdf":
        return load_from_pdf(source)

    elif source_type == "text":
        return load_from_text(source)

    else:
        raise ValueError(f"Unsupported source_type: {source_type}")