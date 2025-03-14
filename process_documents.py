# process_documents.py
import os
from config import DATA_FOLDER
from document_loader import load_file
from text_splitter import split_documents
from database import add_to_chroma_db

def process_documents():
    all_docs = []
    # Process every PDF in the data folder
    for filename in os.listdir(DATA_FOLDER):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(DATA_FOLDER, filename)
            print(f"Processing {file_path} ...")
            docs = load_file(file_path)
            all_docs.extend(docs)
    if all_docs:
        chunks = split_documents(all_docs)
        add_to_chroma_db(chunks)
        print("Database created/updated successfully!")
    else:
        print("No PDF documents found in the data folder.")
