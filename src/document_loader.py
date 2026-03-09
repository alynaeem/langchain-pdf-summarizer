import glob
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

class DocumentLoader:
    def __init__(self, directory_path: str = "data"):
        self.directory_path = directory_path

    def load_pdfs(self) -> List[Document]:
        
        try:
            documents = []
            pdf_files = glob.glob(f"{self.directory_path}/*.pdf")
            for pdf_file in pdf_files:
                loader = PyPDFLoader(pdf_file)
                documents.extend(loader.load())
            
            print("documents loaded")
            return documents
            
        except Exception as e:
            print(f"Error loading PDFs: {e}")
            return []