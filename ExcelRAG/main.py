import query
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
import os

if "messages" not in st.session_state:
    st.session_state.messages = []

@st.cache_resource(show_spinner="Loading AI Model...", show_time=True)
def load_rag():
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    CHROMA_PATH = "chroma_split"
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = ChatOllama(model="mistral")
    return db, model
db, model = load_rag()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ask a question"):
    with st.status("processing") as status:
        st.write("searching documents")
        st.session_state.messages.append({"role": "user", "content": prompt})
        context, sources = query.dbquery(prompt, db) # type: ignore
        st.write("generating answer")
        result = query.modelquery(prompt, model, context, sources)
        status.update(label="done", state="complete", expanded=False)
        
        st.session_state.messages.append({"role": "assistant", "content": result[0]})
        st.rerun()
