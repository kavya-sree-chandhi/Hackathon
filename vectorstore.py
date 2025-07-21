# agent/vectorstore.py

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


def get_vectorstore():
    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    vectorstore = Chroma(
        collection_name="my_collection",
        embedding_function=embeddings
    )
    return vectorstore


def add_chunks_to_vectorstore(chunks, vectorstore):
    """
    Add a list of Document chunks to the vectorstore.
    """
    vectorstore.add_documents(chunks)


def query_vectorstore(query, vectorstore, k=4):
    """
    Query the vectorstore for top-k similar chunks.
    """
    results = vectorstore.similarity_search(query, k=k)
    return results
