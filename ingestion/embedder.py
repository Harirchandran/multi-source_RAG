# ingestion/embedder.py

from langchain_community.embeddings import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings


def get_ollama_embeddings(model_name="nomic-embed-text"):
    """
    Local embedding model using Ollama
    """
    return OllamaEmbeddings(model=model_name)


def get_openai_embeddings():
    """
    Cloud embedding model (better quality, requires API key)
    """
    return OpenAIEmbeddings()


def embed_documents(documents, embedding_model):
    """
    Convert documents into embeddings

    Args:
        documents: list of Document objects
        embedding_model: embedding instance

    Returns:
        vectorstore-ready embeddings (handled later)
    """

    texts = [doc.page_content for doc in documents]

    embeddings = embedding_model.embed_documents(texts)

    return embeddings