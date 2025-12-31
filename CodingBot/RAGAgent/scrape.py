import os
import shutil
import glob
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

SOURCE_DIR = "Data/GleamRAGAgent" 
DB_PATH = "CodingBot/RAGAgent/chroma_db_gleam"
EMBED_MODEL_NAME = "nomic-embed-text"

# Define all the extensions you want to capture
TARGET_EXTENSIONS = [
    ".md",      # Markdown docs
    ".djot",    # Djot docs (Gleam specific)
    ".gleam",   # Gleam source code
    ".toml",    # Configuration files
    ".yaml",    # CI/CD workflows
    ".rs",      # Rust source (Compiler internals)
    ".erl"      # Erlang source (FFI internals)
]

def load_documents(source_dir):
    print(f"Scanning {source_dir} for {TARGET_EXTENSIONS}...")
    documents = []
    
    all_files = []
    # Loop through all extensions and gather files
    for ext in TARGET_EXTENSIONS:
        found = glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
        print(f"   Found {len(found)} files with extension {ext}")
        all_files.extend(found)
    
    print(f"Total raw files found: {len(all_files)}. Filtering now...")

    kept_count = 0
    skipped_count = 0

    for file_path in all_files:
        norm_path = os.path.normpath(file_path)
        path_parts = norm_path.split(os.sep)
        
        # Filter out tests and build artifacts
        is_test_file = False
        for part in path_parts:
            # Added 'target' to filter list (common in Rust/Gleam builds)
            if part.lower() in ['test', 'build', 'tests', 'target']:
                is_test_file = True
                break
        
        if is_test_file:
            skipped_count += 1
            continue

        try:
            loader = TextLoader(file_path, encoding='utf-8')
            documents.extend(loader.load())
            kept_count += 1
        except Exception as e:
            # Silently skip binary/encoding errors usually associated with weird files
            print(f"Error reading {file_path}: {e}")

    print(f"\nSummary:")
    print(f"   Skipped {skipped_count} test/build files.")
    print(f"   Kept {kept_count} valid files.")
    
    if kept_count == 0:
        print("WARNING: No documents were kept! Check your folder structure.")
    
    return documents

def split_documents(documents):
    print("Splitting documents into chunks...")
    
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.MARKDOWN,
        chunk_size=1000,
        chunk_overlap=200
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")
    return chunks

def create_vector_db(chunks):
    if os.path.exists(DB_PATH):
        print(f"Removing existing database at {DB_PATH} for a fresh build...")
        shutil.rmtree(DB_PATH)

    print(f"Initializing Ollama Embeddings ({EMBED_MODEL_NAME})...")
    embeddings = OllamaEmbeddings(model=EMBED_MODEL_NAME)

    print("Creating/Indexing Chroma database (this may take a moment)...")
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_PATH
    )
    print(f"Database successfully created at: {os.path.abspath(DB_PATH)}")

if __name__ == "__main__":
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Directory '{SOURCE_DIR}' not found.")
    else:
        docs = load_documents(SOURCE_DIR)
        if docs:
            chunks = split_documents(docs)
            create_vector_db(chunks)
        else:
            print("No documents found. Check your folder contents.")