import streamlit as st
import tempfile
from utils import (
    extract_text_from_pdf,
    split_text,
    create_embeddings,
    search,
    get_pdf_statistics
)

st.set_page_config(
    page_title="ResearchVerse AI",
    page_icon="📚",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("📚 ResearchVerse AI")
st.markdown("### AI-Powered Research Paper Question Answering System")
st.write("Upload a research paper and ask questions about it.")

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📄 Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file:

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    # Process PDF
    with st.spinner("Processing PDF..."):

        text = extract_text_from_pdf(pdf_path)

        chunks = split_text(text)

        embeddings = create_embeddings(chunks)

        stats = get_pdf_statistics(text, chunks)

    st.sidebar.success("✅ PDF Processed Successfully!")

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 PDF Statistics")

    st.sidebar.metric("Words", stats["Words"])

    st.sidebar.metric("Characters", stats["Characters"])

    st.sidebar.metric("Chunks", stats["Chunks"])

    st.sidebar.markdown("---")

    st.sidebar.write("**Uploaded File**")

    st.sidebar.info(uploaded_file.name)

    st.markdown("---")

    question = st.text_input(
        "💬 Ask a Question"
    )

    if st.button("🔍 Search"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Searching..."):

                results = search(
                    question,
                    chunks,
                    embeddings,
                    top_k=3
                )

            st.success("Answer Found!")

            st.subheader("📖 Best Answer")

            st.write(results[0]["text"])

            confidence = round(results[0]["score"] * 100, 2)

            st.progress(min(results[0]["score"], 1.0))

            st.write(f"**Confidence Score:** {confidence}%")

            st.markdown("---")

            st.subheader("📚 Other Relevant Results")

            for i, result in enumerate(results[1:], start=2):

                with st.expander(f"Result {i}"):

                    st.write(result["text"])

                    score = round(result["score"] * 100, 2)

                    st.write(f"Confidence: {score}%")

else:

    st.info("👈 Upload a research paper from the sidebar to begin.")