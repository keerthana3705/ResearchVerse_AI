from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def clean_text(text):
    """
    Clean the extracted text while preserving paragraph breaks.
    """

    # Remove multiple blank lines
    text = re.sub(r"\n+", "\n", text)

    # Remove extra spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text


def split_text(text, chunk_size=500, overlap=100):
    """
    Split text into overlapping chunks.
    """

    text = clean_text(text)

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_embeddings(chunks):
    """
    Convert text chunks into embeddings.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    return embeddings


def search(query, chunks, embeddings, top_k=3):
    """
    Search the most relevant chunks.
    """

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for index in top_indices:

        results.append(
            {
                "text": chunks[index],
                "score": float(similarities[index])
            }
        )

    return results


def get_pdf_statistics(text, chunks):
    """
    Return statistics about the PDF.
    """

    return {
        "Words": len(text.split()),
        "Characters": len(text),
        "Chunks": len(chunks)
    }