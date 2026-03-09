from langchain_huggingface import HuggingFaceEmbeddings

class embedding:

    def huggingface_embeddings(self):

        try:
            return HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        except Exception as e:
            print(f"Error loading model: {e}")
            return None