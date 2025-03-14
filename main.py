# main.py
import os
import sys
import time
import sys
from config import CHROMA_PATH
from process_documents import process_documents
from database import query_db
from llm_handler import generate_answer

def main(question: str):
    update_db = False

    # Check if Chroma DB exists and is not empty
    if not os.path.exists(CHROMA_PATH) or not os.listdir(CHROMA_PATH):
        print("Chroma DB not found or empty. Processing PDF documents...")
        update_db = True
    else:
        user_input = input("Did the documents change/update or is this the first time running this script? (y/n) [n]: ") or "n"
        if user_input.lower() == "y":
            update_db = True
        elif user_input.lower() == "n":
            update_db = False
        else:
            print("Invalid input. Using default option: no update.")
            update_db = False

    if update_db:
        process_documents()
    else:
        if not os.path.exists(CHROMA_PATH) or not os.listdir(CHROMA_PATH):
            print("Error: Chroma DB does not exist. Please process the documents first.")
            sys.exit(1)
        else:
            print("Using existing Chroma DB. Skipping document processing.")

    start_time = time.time()
    print("Processing started at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))

    context = query_db(question)
    answer = generate_answer(question, context)
    print("\nAnswer:", answer)

    end_time = time.time()
    print("Processing finished at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print("Total processing time: {:.2f} seconds".format(end_time - start_time))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = input("Query>> ")
    main(question)
