from utils import extract_text_from_pdf, chunk_text
from embedder import embed_and_store
from retriever_chain import get_qa_chain

text = extract_text_from_pdf("data/test3e.pdf")
chunks = chunk_text(text)
embeddings = embed_and_store(chunks)
print(embeddings)

qa = get_qa_chain()

query = "What is the main topic of the document?"
result = qa({"query": query})

print("Answer:", result['result'])
print("\nSources")
for doc in result['source_documents']:
    print("-", doc.metadata.get("source", "From chunk"))