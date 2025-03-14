# llm_handler.py
from langchain_ollama import OllamaLLM
from config import CHAT_MODEL

def generate_answer(question: str, context: str) -> str:
    # Use the chat model specified in the config
    llm = OllamaLLM(model=CHAT_MODEL)
    prompt = f"""Context: {context}

Question: {question}

Answer the question based on the context above. Be detailed and thorough."""
    response = llm.invoke(prompt)
    return response
