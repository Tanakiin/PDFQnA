# PDFQnA

Ask My Docs is a lightweight AI-powered Q&A app that lets you upload a PDF and ask natural language questions about its contents. It uses semantic search and large language models to return context-aware answers based on your documents.

🔴 [PDFQnA Live App](https://tanakiin-pdfqna-app-yjxxoi.streamlit.app/)

---

## Features

- Upload and parse any PDF
- Semantic chunking of text for context preservation
- Fast vector search using FAISS
- Real-time question answering using OpenAI's GPT models
- Simple, clean Streamlit interface

---

## Tech Stack

| Component       | Tool                             |
|----------------|----------------------------------|
| Language Model  | OpenAI GPT-3.5-turbo (swappable) |
| Embeddings      | OpenAI `text-embedding-ada-002`  |
| Vector Store    | FAISS                            |
| Framework       | LangChain                        |
| UI              | Streamlit                        |
| PDF Parsing     | PyMuPDF (`fitz`)                 |

---

## Quick Start

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/ask-my-docs.git
cd ask-my-docs
```

2. **Set up a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI key:**

Create a `.env` file and add:

```
OPENAI_API_KEY=your-openai-api-key-here
```

5. **Run the app:**

```bash
streamlit run app.py
```

---

## Environment Variables

| Variable          | Description                          |
|------------------|--------------------------------------|
| `OPENAI_API_KEY` | Your OpenAI API key (not committed)  |

---

## Future Additions

- LoRA fine-tuned local model support
- Multi-document support and indexing
- Conversational memory features
- Deployment via Streamlit Cloud or HuggingFace Spaces


