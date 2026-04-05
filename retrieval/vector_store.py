# retrieval/vector_store.py

from langchain_community.vectorstores import FAISS
import os


def create_vector_store(documents, embedding_model):
    """
    Create FAISS vector store from documents
    """
    vectorstore = FAISS.from_documents(documents, embedding_model)
    return vectorstore


def save_vector_store(vectorstore, path="index"):
    """
    Save FAISS index to disk
    """
    vectorstore.save_local(path)


def load_vector_store(embedding_model, path="index"):
    """
    Load FAISS index from disk
    """
    if not os.path.exists(path):
        raise ValueError("Vector store not found. Create it first.")

    vectorstore = FAISS.load_local(path, embedding_model, allow_dangerous_deserialization=True)
    return vectorstore