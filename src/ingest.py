from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_chunk_documents(folder_path: str = "data/documents"):
    loader = PyPDFDirectoryLoader(folder_path)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    non_empty_documents = []
    for doc in documents:
        if doc.page_content and doc.page_content.strip():
            non_empty_documents.append(doc)

    print(f"Non-empty pages: {len(non_empty_documents)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(non_empty_documents)

    print(f"Created {len(chunks)} chunks")

    return non_empty_documents, chunks