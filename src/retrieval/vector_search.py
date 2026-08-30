from search_strategy import BaseRetrievalStrategy


class VectorRetrievalStrategy(BaseRetrievalStrategy):
    def __init__(self, chroma_collection):
        self.collection = chroma_collection

    def retrieval_context(self, query, limit = 3) -> str:
        results = self.collection.query(query_texts=[query], n_results=limit)
        return "\n".join(results['documents'][0])