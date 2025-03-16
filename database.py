# database.py
from ollama_embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.schema.document import Document
from config import CHROMA_PATH, EMBEDDING_MODEL, BASE_URL

def add_to_chroma_db(chunks: list[Document]):
    # Initialize embeddings using the model from config
    embeddings = OllamaEmbeddings(model_name=EMBEDDING_MODEL,base_url=BASE_URL)
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    print(f"Added {len(chunks)} chunks to Chroma DB")

def query_db(question: str) -> str:
    # Initialize embeddings using the model from config
    embeddings = OllamaEmbeddings(model_name=EMBEDDING_MODEL,base_url=BASE_URL)
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )
    results = db.similarity_search_with_relevance_scores(question, k=3)
    context_text = "\n\n".join([doc.page_content for doc, _ in results])
    return context_text
