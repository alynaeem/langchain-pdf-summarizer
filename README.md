# LangChain PDF Summarizer

A modular Retrieval-Augmented Generation (RAG) pipeline built with **LangChain** that loads PDF documents, splits and embeds them, stores them in a FAISS vector store, and answers questions using **Google Gemini** as the LLM.

---

## 🚀 Features

- 📄 **PDF Loading** – Automatically loads all PDFs from the `data/` directory
- ✂️ **Text Splitting** – Recursively splits text into manageable chunks
- 🔍 **Embeddings** – Uses HuggingFace sentence-transformers for local embeddings
- 🗄️ **Vector Store** – FAISS-powered similarity search with MMR support
- 🤖 **LLM Integration** – Google Gemini (via `langchain-google-genai`)
- 🔄 **RAG Pipeline** – Context-aware answers from your documents

---

## 📁 Project Structure

```
langchain-pdf-summarizer/
├── main.py                  # Entry point – runs the full RAG pipeline
├── requirement.txt          # Python dependencies
├── .env                     # API keys (not committed – see .gitignore)
├── .gitignore
├── data/                    # Place your PDF files here
├── faiss_index/             # Auto-generated FAISS index (local only)
└── src/
    ├── document_loader.py   # Loads PDFs using LangChain's PyPDFLoader
    ├── text_splitter.py     # Splits documents into chunks
    ├── embedding.py         # HuggingFace embeddings setup
    ├── vector_store.py      # FAISS vector store creation
    ├── retreiver.py         # Similarity & MMR retrieval
    └── llm.py               # Google Gemini LLM loader
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/alynaeem/langchain-pdf-summarizer.git
cd langchain-pdf-summarizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 5. Add your PDFs

Place any PDF files you want to query in the `data/` directory.

### 6. Run the pipeline

```bash
python main.py
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [LangChain](https://langchain.com) | RAG framework |
| [Google Gemini](https://ai.google.dev) | LLM for answering questions |
| [HuggingFace Transformers](https://huggingface.co) | Embedding model |
| [FAISS](https://faiss.ai) | Vector similarity search |
| [PyPDF](https://pypdf.readthedocs.io) | PDF text extraction |

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
