import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


load_dotenv()

def embed_and_store(chunks, path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(chunks, embeddings)
    db.save_local(path)
    print(f"Stored {len(chunks)} chunks in FAISS index at {path}")

def load_vector_store(path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(path, embeddings)