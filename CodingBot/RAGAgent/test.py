from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from query import modelquery, dbquery

def load_rag():
    embedding_function = OllamaEmbeddings(model="nomic-embed-text")
    CHROMA_PATH = "CodingBot/RAGAgent/chroma_db_gleam"
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = ChatOllama(model="mistral")
    return db, model
db, model = load_rag()

query_text = "Show me the implementation of length in list.gleam. Does it use recursion?"

context, sources = dbquery(query_text, db)

print(modelquery(query_text, model, context, sources)[0])