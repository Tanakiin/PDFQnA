import streamlit as st
from utils import extract_text_from_pdf, chunk_text
from embedder import embed_and_store
from retriever_chain import get_qa_chain
import streamlit as st
st.set_page_config(page_title="PDF QnA", layout="centered")

from streamlit_cookies_manager import EncryptedCookieManager
import os
import time

cookie_password = st.secrets["COOKIE_PASSWORD"]
cookies = EncryptedCookieManager(
    prefix="pdfqna_",
    password=cookie_password,
)

if not cookies.ready():
    st.stop()

MAX_REQUESTS = 20

request_count = int(cookies.get("request_count") or 0)

if request_count >= MAX_REQUESTS:
    st.error("You've reached the 20-question limit.")
    st.stop()

st.info(f"💬 Questions used: {request_count} / {MAX_REQUESTS}")

st.title("PDF QnA")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file and uploaded_file.size > 2 * 1024 * 1024:
    st.error("File too large. Max allowed size is 2MB.")
    st.stop()

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

    if "last_query_time" not in st.session_state:
        st.session_state.last_query_time = 0

    if query:
        current_time = time.time()
        if current_time - st.session_state.last_query_time < 15:
            st.warning("Please wait a few seconds between questions.")
            st.stop()
        st.session_state.last_query_time = current_time

    if query:
        with st.spinner("Thinking..."):
            qa = get_qa_chain()
            result = qa({"query": query})

        request_count += 1
        cookies["request_count"] = str(request_count)
        cookies.save()


        st.subheader("Answer:")
        st.write(result['result'])
