from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_medical_guidance(description):
    db = Chroma(persist_directory="./chroma_db", embedding_function=HuggingFaceEmbeddings())
    # Search for the top 2 most relevant first-aid steps
    results = db.similarity_search(description, k=2)
    return " ".join([doc.page_content for doc in results])