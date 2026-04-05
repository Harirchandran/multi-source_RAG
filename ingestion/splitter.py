# ingestion/splitter.py

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size=500, chunk_overlap=100):
    """
    Splits documents into smaller chunks.

    Args:
        documents: List of LangChain Document objects
        chunk_size: max characters per chunk
        chunk_overlap: overlapping characters between chunks

    Returns:
        List of chunked Document objects
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(documents)
    return chunks