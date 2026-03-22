# RAG Document QA System

## Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system for answering questions over PDF documents.

The system allows users to:

- Load PDF documents
- Convert document text into **semantic embeddings**
- Store embeddings in a **FAISS vector database**
- Retrieve relevant document chunks for a query
- Generate **grounded answers using an LLM**

The application is built with **Streamlit** and demonstrates modern **AI engineering workflows**.

---

## Architecture

```
PDF Documents
     ↓
Document Loader
     ↓
Text Chunking
     ↓
Embeddings (Sentence Transformers)
     ↓
FAISS Vector Store
     ↓
Semantic Retrieval
     ↓
LLM Answer Generation
     ↓
Streamlit UI
```

---

## Features

- PDF document ingestion
- Recursive text chunking
- Semantic search using **FAISS**
- Retrieval-Augmented Generation (RAG)
- Streamlit interactive interface
- Retrieved context displayed for transparency

---

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Sentence Transformers
- OpenAI API
- PyPDF

---

## Project Structure

```
rag-document-qa/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── ingest.py
│   ├── retrieve.py
│   └── rag_pipeline.py
│
├── data/
│   └── documents/
│
├── vector_store/
│
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/sasifraza/rag-document-qa.git
cd rag-document-qa
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Add PDF documents

Place PDF files inside:

```
data/documents/
```

### 6. Run the application

```bash
streamlit run app/streamlit_app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Example Use Cases

- Ask questions about research papers
- Summarize long PDF documents
- Retrieve evidence-based answers from documents
- Explore knowledge inside large document collections

---

## Demo

*(Add screenshots here)*

Example:

```
![Interface](assets/interface.png)
![Indexing](assets/indexing.png)
![Question Answering](assets/qa_demo.png)
```

---

## Future Improvements

- Persistent FAISS index loading
- Drag-and-drop PDF upload
- Source citation with page numbers
- Docker containerization
- Cloud deployment (Azure / AWS)
- Support for multiple LLM providers

---

## Author

Syed Asif Raza
