# retrieval/retriever.py

def get_retriever(vectorstore):
    """
    Convert vector store into a retriever
    """
    # k=5 means we retrieve the top 5 most similar documents
    return vectorstore.as_retriever(search_kwargs={"k": 5})

def retrieve_documents(retriever, query):
    """
    Retrieve relevant documents for the query
    """
    return retriever.invoke(query)