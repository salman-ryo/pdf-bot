# ollama_embeddings.py
import requests
from typing import List
from langchain.embeddings.base import Embeddings

class OllamaEmbeddings(Embeddings):
    def __init__(self, model_name="mxbai-embed-large:latest", base_url="http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url

    def embed_query(self, text: str) -> List[float]:
        return self._embed_texts([text])[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embed_texts(texts)

    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        endpoint = f"{self.base_url}/v1/embeddings"
        payload = {
            "model": self.model_name,
            "input": texts,
            "encoding_format": "float"  # Ensure float format for compatibility
        }
        
        try:
            response = requests.post(endpoint, json=payload)
            response.raise_for_status()
            return [item["embedding"] for item in response.json()["data"]]
        except Exception as e:
            raise RuntimeError(f"Failed to get embeddings: {str(e)}")