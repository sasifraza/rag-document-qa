import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.ingest import load_and_chunk_documents
from src.retrieve import build_vector_store
from src.rag_pipeline import answer_question

st.title("RAG Document QA System")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if st.button("Load Documents", key="load_docs_btn"):
    documents, chunks = load_and_chunk_documents("data/documents")

    if len(documents) == 0:
        st.error("PDF was found, but no readable text was extracted.")
    elif len(chunks) == 0:
        st.error("Readable pages were found, but chunk creation failed.")
    else:
        st.session_state.vector_store = build_vector_store(chunks)
        st.success(f"Loaded {len(documents)} readable pages and indexed {len(chunks)} chunks.")

question = st.text_input("Ask a question about the documents")

if question and st.session_state.vector_store is not None:
    answer, docs = answer_question(st.session_state.vector_store, question)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Retrieved Chunks")
    for i, doc in enumerate(docs, start=1):
        st.markdown(f"**Chunk {i}**")
        st.write(doc.page_content[:500])