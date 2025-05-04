from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_qa_chain(path="faiss_index"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are an intelligent assistant. Use the following context to answer the question accurately.\n
        Context: {context} \n
        Question: {question} \n
        Answer:
        """)

    llm = ChatOpenAI(model="o4-mini-2025-04-16")
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True)

    return qa_chain