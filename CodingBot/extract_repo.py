import os
import json
import argparse
from pathlib import Path

NICHE_EXTENSIONS = {'.gleam', '.rs', '.hs'} 
DOC_EXTENSIONS = {'.md', '.txt', '.rst', '.adoc'}
IGNORE_DIRS = {'.git', 'build', 'dist', 'node_modules', '__pycache__', '.github'}

def is_text_file(file_path):
    """
    Checks if a file is readable text by trying to read the first chunk.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except (UnicodeDecodeError, IOError):
        return False

def process_for_graphrag(repo_path, output_dir):
    """
    Flattens the repo into a single folder of .txt files.
    Filename format: path_to_file___filename.txt
    """
    repo_path = Path(repo_path).resolve()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Scanning for GraphRAG: {repo_path}")
    
    file_count = 0
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()

            if (ext in NICHE_EXTENSIONS or ext in DOC_EXTENSIONS) and is_text_file(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    # --- GRAPH RAG FORMATTING ---
                    # 1. Create a unique filename based on the path (so you don't overwrite 'main.rs' with another 'main.rs')
                    # Example: src/utils/helper.gleam -> src__utils__helper.gleam.txt
                    relative_path = file_path.relative_to(repo_path)
                    safe_name = str(relative_path).replace(os.sep, "__") + ".txt"
                    
                    # 2. Add header context 
                    # (Helpful for the Graph extractor to know what file it is looking at)
                    augmented_content = f"FILENAME: {relative_path}\nEXTENSION: {ext}\n\n{content}"

                    # 3. Write to the flat input folder
                    with open(output_dir / safe_name, 'w', encoding='utf-8') as out_f:
                        out_f.write(augmented_content)
                    
                    file_count += 1
                    
                except Exception as e:
                    print(f"⚠️ Error processing {file_path}: {e}")

    print(f"✅ GraphRAG Input Ready! {file_count} files saved to '{output_dir}/'")

if __name__ == "__main__":
    process_for_graphrag("gleam", "input")