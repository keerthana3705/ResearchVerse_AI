# 📚 ResearchVerse AI

An AI-powered Research Paper Question Answering System built using **Python**, **Streamlit**, **Sentence Transformers**, and **Natural Language Processing (NLP)**.

Users can upload any research paper (PDF), ask questions, and receive the most relevant answers using semantic search.

---

## 🚀 Features

- 📄 Upload any research paper (PDF)
- 🤖 AI-powered semantic search
- 🧠 Sentence Transformer embeddings
- 🔍 Top 3 relevant answers
- 📊 Confidence score
- 📈 PDF statistics
- 💻 Simple and interactive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF2
- Sentence Transformers
- Scikit-learn
- NumPy

---

## 📂 Project Structure

```
ResearchVerse_AI/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── papers/
├── screenshots/
└── report/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/keerthana3705/ResearchVerse_AI.git
```

Move into the project folder:

```bash
cd ResearchVerse_AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload a research paper in PDF format.
2. The application extracts all text from the document.
3. The text is divided into smaller chunks.
4. Sentence Transformer converts each chunk into embeddings.
5. Your question is converted into an embedding.
6. Cosine Similarity finds the most relevant chunk.
7. The best matching answer is displayed along with a confidence score.

---

## 📸 Screenshots

(Add screenshots here after testing the application.)

---

## 🔮 Future Enhancements

- Support multiple PDF documents
- AI-generated summaries
- Voice-based questions
- Chat history
- Keyword highlighting
- Export answers to PDF

---

## 👩‍💻 Author

**Keerthana Balakrishnan**

B.E. Artificial Intelligence and Data Science

GitHub: https://github.com/keerthana3705

LinkedIn: https://linkedin.com/in/keerthana3705

---

## ⭐ If you found this project useful, consider giving it a star!