import chromadb
import os

# --- Configuration ---
# The path matches the one shown in your traceback
DB_PATH = r"D:\Code\ML-Playground\CodingBot\RAGAgent\chroma_db_gleam"
COLLECTION_NAME = "langchain"  # LangChain usually defaults to this name
SEARCH_TERM = "result.gleam"   # The file/substring you are hunting for
# ---------------------

def inspect_db():
    print(f"--- Loading database from {DB_PATH} ---")
    
    if not os.path.exists(DB_PATH):
        print(f"ERROR: Database path does not exist: {DB_PATH}")
        return

    # 1. Initialize the native Chroma client
    client = chromadb.PersistentClient(path=DB_PATH)

    # 2. Verify the collection exists
    collections = client.list_collections()
    collection_names = [c.name for c in collections]
    
    if COLLECTION_NAME not in collection_names:
        print(f"Could not find collection '{COLLECTION_NAME}'. Found: {collection_names}")
        # If your collection has a different name, we try to guess it
        if len(collection_names) > 0:
            actual_collection = collection_names[0]
            print(f"Defaulting to collection: '{actual_collection}'")
        else:
            return
    else:
        actual_collection = COLLECTION_NAME

    collection = client.get_collection(actual_collection)
    count = collection.count()
    print(f"Total chunks in database: {count}")

    print(f"\n--- Hunting for '{SEARCH_TERM}' in metadata source ---")

    # 3. Fetch ALL metadata to filter in Python
    # We only fetch metadata and IDs first to keep it fast. 
    # We will fetch the actual document content only for the matches.
    all_data = collection.get(include=["metadatas"])

    matching_ids = []
    
    # 4. Filter manually in Python
    # all_data['metadatas'] is a list of dictionaries
    if all_data['metadatas']:
        for idx, meta in enumerate(all_data['metadatas']):
            # Safety check: meta can technically be None
            if meta:
                source = meta.get("source", "")
                if SEARCH_TERM in source:
                    matching_ids.append(all_data['ids'][idx])

    num_matches = len(matching_ids)
    print(f"Found {num_matches} chunks matching '{SEARCH_TERM}'")

    if num_matches == 0:
        return

    # 5. Fetch details for the matches
    print("\n--- Match Details ---")
    results = collection.get(ids=matching_ids, include=["metadatas", "documents"])

    for i in range(num_matches):
        doc_id = results['ids'][i]
        meta = results['metadatas'][i]
        content = results['documents'][i]
        
        print(f"\n[Chunk ID]: {doc_id}")
        print(f"[Source]: {meta.get('source', 'Unknown')}")
        print("-" * 40)
        # Print first 300 chars of content to preview
        print(f"{content[:300]}...") 
        print("-" * 40)

if __name__ == "__main__":
    inspect_db()