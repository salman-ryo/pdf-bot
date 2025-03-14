# document_loader.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema.document import Document

def load_file(path: str) -> list[Document]:
    try:
        loader = PyPDFLoader(path)
        return loader.load()
    except Exception as e:
        print(f"Error loading file {path}: {e}")
        return []
