# RAG Document QA System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system for question answering over PDF documents.

It allows users to:
- load PDF documents
- convert them into semantic embeddings
- store them in a FAISS vector database
- retrieve the most relevant chunks for a user query
- generate grounded answers using an LLM

The application is built with a Streamlit interface and is intended as a portfolio project demonstrating modern AI engineering skills.

---

## Architecture

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

---

## Features

- PDF document ingestion
- Recursive text chunking
- Semantic search with FAISS
- Retrieval-Augmented Generation (RAG)
- Streamlit-based question answering interface
- Display of retrieved chunks for transparency

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

```text
rag-document-qa/
├── app/
│   └── streamlit_app.py
├── src/
│   ├── ingest.py
│   ├── retrieve.py
│   └── rag_pipeline.py
├── data/
│   └── documents/
├── vector_store/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
