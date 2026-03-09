import os
from dotenv import load_dotenv
from src.document_loader import DocumentLoader
from src.text_splitter import RecursiveCharacterTextSplitter
from src.embedding import embedding
from src.vector_store import VectorStore
from src.retreiver import Retriever
from src.llm import load_google_genai_model

load_dotenv()
API_KEY = os.getenv("API_KEY")

if __name__ == "__main__":
	loader = DocumentLoader()
	docs = loader.load_pdfs()
	print("num docs:", len(docs))

	splitter = RecursiveCharacterTextSplitter()
	all_text = "\n\n".join(doc.page_content for doc in docs)
	chunks = splitter.split_text(all_text)
	print("num chunks:", len(chunks))

	emb_class = embedding()
	embedding_model = emb_class.huggingface_embeddings()

	if embedding_model:
		vs = VectorStore()
		db = vs.create_vector_store(chunks, embedding_model)
		print("vector store created")
		db.save_local("faiss_index")
		print("vector store saved to faiss_index")

		retriever = Retriever(db)
		question = "What is the document about"
		results_sim, results_mmr = retriever.search_both(question, k=3)

		print("similarity results:", results_sim)
		print("mmr results:", results_mmr)

		llm = load_google_genai_model()
		if llm:
			context = "\n\n".join(doc.page_content for doc in results_mmr)
			prompt = f"Use the context to answer.\n\nContext:\n{context}\n\nQuestion: {question}"
			answer = llm.invoke(prompt)
			print("LLM answer:", answer)