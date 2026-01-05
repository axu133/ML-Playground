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

TARGET_EXTENSIONS = [
    ".md",      # Markdown docs
    ".djot",    # Djot docs (Gleam specific)
    ".gleam",   # Gleam source code (Whole File)
    ".toml",    # Configuration files
    ".yaml",    # CI/CD workflows
    ".erl"      # Erlang source (FFI internals)
]

# Extensions to not be split
WHOLE_FILE_EXTENSIONS = [".gleam"]

def load_documents(source_dir):
    print(f"Scanning {source_dir} for {TARGET_EXTENSIONS}...")
    documents = []
    
    all_files = []
    for ext in TARGET_EXTENSIONS:
        found = glob.glob(os.path.join(source_dir, f"**/*{ext}"), recursive=True)
        print(f"  Found {len(found)} files with extension {ext}")
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
            print(f"Error reading {file_path}: {e}")

    print(f"\nSummary:")
    print(f"  Skipped {skipped_count} test/build files.")
    print(f"  Kept {kept_count} valid files.")
    
    if kept_count == 0:
        print("WARNING: No documents were kept! Check your folder structure.")
    
    return documents

def split_documents(documents):
    print("Splitting documents...")
    
    # 1. Prose Splitter (Markdown)
    prose_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.MARKDOWN,
        chunk_size=1000,
        chunk_overlap=200
    )
    
    # 2. Code Splitter (Strict Safety)
    # 2000 chars is well within the 2k token limit
    code_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.GO,
        chunk_size=2000, 
        chunk_overlap=400
    )

    # STRICT LIMIT: 6000 Characters
    # This ensures we fit inside the standard 2048 token context window.
    MAX_CHARS_SAFE_LIMIT = 5000
    
    final_chunks = []
    prose_docs = []
    code_docs_to_split = []

    # 3. Sort documents
    for doc in documents:
        file_source = doc.metadata.get("source", "")
        _, ext = os.path.splitext(file_source)
        content_len = len(doc.page_content)

        if ext == ".gleam":
            # Convert "Data/.../gleam/result.gleam" -> "gleam/result"
            # This is a rough heuristic; adjust split('/') indices based on your folder structure
            filename = os.path.basename(file_source)
            module_name = filename.replace(".gleam", "") 
            
            # We inject a clear header at the top of the content
            # This ensures queries for "gleam/result" hit this file hard.
            header = f"Module: gleam/{module_name}\nFile: {filename}\nSource Code:\n"
            doc.page_content = header + doc.page_content
        
        # LOGIC:
        if ext in WHOLE_FILE_EXTENSIONS:
            if content_len < MAX_CHARS_SAFE_LIMIT:
                # Small enough to keep whole (e.g., result.gleam)
                final_chunks.append(doc)
            else:
                # Too big -> Send to Code Splitter (e.g., list.gleam)
                code_docs_to_split.append(doc)
        else:
            prose_docs.append(doc)

    # 4. Process Splits
    if prose_docs:
        print(f"  Splitting {len(prose_docs)} prose documents...")
        final_chunks.extend(prose_splitter.split_documents(prose_docs))
        
    if code_docs_to_split:
        print(f"  Splitting {len(code_docs_to_split)} large code documents...")
        final_chunks.extend(code_splitter.split_documents(code_docs_to_split))

    # 5. PARANOIA CHECK (The "Filter")
    safe_chunks = []
    dropped_count = 0
    
    for chunk in final_chunks:
        c_len = len(chunk.page_content)
        # Final safety net: If a chunk is still > 6000, drop it to save the build.
        if c_len > MAX_CHARS_SAFE_LIMIT:
            print(f"  CRITICAL DROP: Chunk from {chunk.metadata.get('source')} is {c_len} chars. Dropping.")
            dropped_count += 1
        else:
            safe_chunks.append(chunk)

    print(f"Total chunks created: {len(safe_chunks)}")
    if dropped_count > 0:
        print(f"WARNING: Dropped {dropped_count} chunks to prevent crash.")
    
    return safe_chunks

def create_vector_db(chunks):
    if os.path.exists(DB_PATH):
        print(f"Removing existing database at {DB_PATH} for a fresh build...")
        shutil.rmtree(DB_PATH)

    print(f"Initializing Ollama Embeddings ({EMBED_MODEL_NAME})...")
    embeddings = OllamaEmbeddings(model=EMBED_MODEL_NAME, num_ctx=8192)

    print(f"Creating/Indexing Chroma database with {len(chunks)} chunks...")
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