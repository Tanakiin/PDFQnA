import streamlit as st
from utils import extract_text_from_pdf, chunk_text
from embedder import embed_and_store
from retriever_chain import get_qa_chain
import os

st.set_page_config(page_title="PDF QnA", layout="centered")
st.title("PDF QnA")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    st.success("PDF Uploaded")
    file_path = os.path.join("data", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(file_path)
        chunks = chunk_text(text)
        embed_and_store(chunks)

    st.success("Text extracted and embedded successfully!")

    query = st.text_input("Ask a question about the PDF:")

    if query:
        with st.spinner("Thinking..."):
            qa = get_qa_chain()
            result = qa({"query": query})

        st.subheader("Answer:")
        st.write(result['result'])
