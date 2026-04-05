# main.py

from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from ingestion.embedder import get_ollama_embeddings, get_huggingface_embeddings
from retrieval.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)
from retrieval.retriever import get_retriever, retrieve_documents
from retrieval.reranker import Reranker
from generation.llm import get_llm, generate_answer
from generation.prompt import get_prompt
import os
import json
import shutil

INDEX_PATH = "index"
SOURCES_PATH = "sources.json"


def check_index_exists():
    """Returns True if the index exists, False otherwise."""
    return os.path.exists(INDEX_PATH)


def get_sources():
    """Returns a list of tracked sources."""
    if os.path.exists(SOURCES_PATH):
        try:
            with open(SOURCES_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def delete_index():
    """Deletes the vector store and the sources audit log."""
    if os.path.exists(INDEX_PATH):
        shutil.rmtree(INDEX_PATH)
    if os.path.exists(SOURCES_PATH):
        os.remove(SOURCES_PATH)
    print("Index and sources deleted.")


def add_source_to_index(source_path, source_type, source_name=None):
    """
    Dynamically loads a new source, chunks it, and appends it to the FAISS index.
    Records the custom `source_name` in sources.json.
    """
    if source_name is None:
        source_name = source_path

    print(f"Adding new {source_type} source: {source_name}")
    docs = load_documents(source_path, source_type)
    chunks = split_documents(docs)

    if not chunks:
        raise ValueError(f"Could not extract any readable text from '{source_name}'. If it is a PDF, it might be an image-only document.")

    # embedding_model = get_ollama_embeddings()
    embedding_model = get_huggingface_embeddings()

    if os.path.exists(INDEX_PATH):
        vectorstore = load_vector_store(embedding_model, INDEX_PATH)
        vectorstore.add_documents(chunks)
        print("Merged new vectors into existing index.")
    else:
        vectorstore = create_vector_store(chunks, embedding_model)
        print("Created new vector index.")

    save_vector_store(vectorstore, INDEX_PATH)
    
    # Save to sources.json
    sources = get_sources()
    sources.append({"name": source_name, "type": source_type})
    with open(SOURCES_PATH, "w", encoding="utf-8") as f:
        json.dump(sources, f, indent=4)
        
    print("Successfully saved vector index and metadata.")


def build_index():
    """
    Step 1: Load → Split → Embed → Store
    Runs only if index doesn't exist
    """

    print("Building vector store...")

    from config.settings import DATA_SOURCES

    docs = []

    for source in DATA_SOURCES:
     docs.extend(
        load_documents(source["path"], source["type"])
     )

    chunks = split_documents(docs)

    embedding_model = get_ollama_embeddings()

    vectorstore = create_vector_store(chunks, embedding_model)

    save_vector_store(vectorstore, INDEX_PATH)

    print("Index created and saved.")


def load_or_create_index():
    """
    Load existing index or create new one
    """

    # embedding_model = get_ollama_embeddings()
    embedding_model = get_huggingface_embeddings()

    if os.path.exists(INDEX_PATH):
        print("Loading existing index...")
        return load_vector_store(embedding_model, INDEX_PATH)

    else:
        build_index()
        return load_vector_store(embedding_model, INDEX_PATH)


def run_query(query):
    """
    Full RAG pipeline
    """

    # Load vector store
    vectorstore = load_or_create_index()

    # Retriever
    retriever = get_retriever(vectorstore)
    retrieved_docs = retrieve_documents(retriever, query)

    # Reranker
    reranker = Reranker()
    final_docs = reranker.rerank(query, retrieved_docs)

    # LLM + Prompt
    llm = get_llm()
    prompt = get_prompt()

    answer = generate_answer(llm, prompt, final_docs, query)

    return answer, final_docs


if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or 'exit'): ")

        if query.lower() == "exit":
            break

        answer, docs = run_query(query)

        print("\nAnswer:\n")
        print(answer)

        print("\nSources:\n")
        for i, doc in enumerate(docs):
            print(f"--- Source {i+1} ---")
            print(doc.page_content[:200])
            print()