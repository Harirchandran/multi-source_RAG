# utils/helpers.py

def format_docs(documents):
    """
    Convert list of docs into single string
    """
    return "\n\n".join([doc.page_content for doc in documents])


def print_docs(documents, limit=200):
    """
    Debug print documents
    """
    for i, doc in enumerate(documents):
        print(f"\n--- Doc {i+1} ---")
        print(doc.page_content[:limit])