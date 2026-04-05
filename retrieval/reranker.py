# retrieval/reranker.py

from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(self, model_name="cross-encoder/ms-marco-MiniLM-L-6-v2"):
        """
        Cross-encoder model for reranking
        """
        self.model = CrossEncoder(model_name)

    def rerank(self, query, documents, top_n=3):
        """
        Rerank retrieved documents based on relevance

        Args:
            query: user query
            documents: list of Document objects
            top_n: number of final documents

        Returns:
            top_n reranked documents
        """

        pairs = [(query, doc.page_content) for doc in documents]

        scores = self.model.predict(pairs)

        # Attach scores
        scored_docs = list(zip(documents, scores))

        # Sort by score descending
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        # Return top_n documents
        top_docs = [doc for doc, score in scored_docs[:top_n]]

        return top_docs