from langchain_community.vectorstores import FAISS

class VectorStore:
    def create_vector_store(self,texts, embeddings):
        try:
            vector_store = FAISS.from_texts(texts=texts, embedding=embeddings)
            return vector_store
        except Exception as e:
            print("Error creating vector store" , e)