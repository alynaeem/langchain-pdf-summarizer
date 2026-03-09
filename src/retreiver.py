class Retriever:
    def __init__(self, vector_store, mode="mmr"):
        self.vector_store = vector_store
        self.mode = mode

    def similarity_search(self, query, k=3):
        return self.vector_store.similarity_search(query, k=k)

    def mmr_search(self, query, k=3):
        return self.vector_store.max_marginal_relevance_search(query, k=k)

    def search_both(self, query, k=3):
        sim = self.similarity_search(query, k=k)
        mmr = self.mmr_search(query, k=k)
        return sim, mmr