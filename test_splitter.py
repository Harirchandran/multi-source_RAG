from ingestion.loader import load_documents
from ingestion.splitter import split_documents

docs = load_documents(
    "https://docs.smith.langchain.com/",
    "web"
)

chunks = split_documents(docs)

print(f"Original docs: {len(docs)}")
print(f"Chunks: {len(chunks)}")

print("\nSample chunk:\n")
print(chunks[0].page_content[:300])