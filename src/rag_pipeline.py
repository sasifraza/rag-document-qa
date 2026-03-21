import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

from src.retrieve import retrieve_docs




def answer_question(vector_store, question: str):
    docs = retrieve_docs(vector_store, question, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0
    )

    prompt = f"""
You are a helpful assistant. Use only the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content, docs