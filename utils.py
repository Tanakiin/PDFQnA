import fitz

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    full_text = ""

    for page in doc:
        text = page.get_text()
        text = text.replace("\n", " ").strip()
        full_text += text + "\n\n"

    return full_text.strip()

def chunk_text(text, size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start += size - overlap

    return chunks