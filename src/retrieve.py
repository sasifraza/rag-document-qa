from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def build_vector_store(chunks):
    embeddings = get_embedding_model()
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store


def retrieve_docs(vector_store, question: str, k: int = 4):
    return vector_store.similarity_search(question, k=k)