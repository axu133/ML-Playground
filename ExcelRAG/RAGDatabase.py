from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os
import shutil

DATA_PATH = "statistical_functions"
CHROMA_PATH = "chroma_split"

headers_to_split_on = [
    ('#', "function_name"),
    ('##', "Syntax"),
    ('##', "Examples")
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob = "*.md", loader_cls=TextLoader)
    documents = loader.load()
    return documents

documents = load_documents()

all_splits = []

for doc in documents:
    splits = splitter.split_text(doc.page_content)

    for split in splits:
        split.metadata.update(doc.metadata)

    all_splits.extend(splits)

if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

db = Chroma.from_documents(
    documents=all_splits,
    embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
    persist_directory=CHROMA_PATH
    )