from langchain_core.output_parsers import StrOutputParser
import re

PROMPT_TEMPLATE = """[INST] You are a technical consultant. Use the provided context to answer the user's request.

### Step 1: Evidence
List the specific functions or facts from the context that are relevant to the user's question. Use direct quotes or references. When providing code snippets or function names, strictly adhere to the snake_case syntax used in the retrieved Gleam documentation.

### Step 2: Analysis & Suggestions
Based ONLY on the evidence above, suggest how to analyze the data. If you extrapolate beyond the context to provide better advice, you MUST start those sentences with "Based on general coding principles..."

### Context: 
{context}

### Question: 
{query} [/INST]
"""

GROUNDING_JUDGE_TEMPLATE = """[INST] You are a high-precision Audit Bot. 
Compare the provided ANSWER against the CONTEXT to calculate a Grounding Score.

### CONTEXT:
{context}

### ANSWER:
{answer}

### INSTRUCTIONS:
1. List every specific tool, function, or statistical claim made in the ANSWER.
2. Check if each exists in the CONTEXT.
3. Calculate a Grounding Score (0 to 100). 100 means every single word is backed by context. 0 means it's all outside knowledge.
4. Output your response in this EXACT format:
SCORE: [number]
REASON: [one sentence explanation]
[/INST]
"""

def _get_golden_chunks(docs, query_text):
    """
    Helper function: Filters a large list of docs to find 'Golden Chunks' (definitions).
    """
    query_words = set(query_text.lower().split())
    # Added "type" and "struct" to stop words so we don't accidentally filter them out if they are the target
    stop_words = {"show", "the", "function", "in", "code", "gleam", "how", "what", "implementation", "define", "vs", "and", "or", "difference", "between", "compare", "definition", "of"}
    potential_funcs = query_words - stop_words
    
    high_priority = []
    medium_priority = []

    for doc in docs:
        content_lower = doc.lower()
        
        # Priority 1: Definition (pub fn, fn, or pub type)
        is_def = False
        for term in potential_funcs:
            # We check for types now too!
            if (f"pub fn {term}" in content_lower or 
                f"fn {term}" in content_lower or 
                f"pub type {term}" in content_lower or
                f"pub opaque type {term}" in content_lower):
                is_def = True
                break
        
        if is_def:
            high_priority.append(doc)
        # Priority 2: Mention
        elif any(term in content_lower for term in potential_funcs):
            medium_priority.append(doc)

    if high_priority:
        return high_priority 
    elif medium_priority:
        return medium_priority[:10]
    else:
        return docs[:5]

def dbquery(query_text, db) -> tuple:
    print(f"\n--- Processing Query: '{query_text}' ---")
    
    context_parts = []
    sources = set()
    
    # 1. Check for MULTIPLE Specific File Targets
    file_matches = re.findall(r"(\w+\.gleam)", query_text)
    
    if file_matches:
        target_files = list(set(file_matches))
        print(f"-> Targeted Files Detected: {target_files}")
        
        collection = db._collection
        all_meta = collection.get(include=["metadatas"])
        
        for target_file in target_files:
            matching_ids = []
            
            if all_meta['metadatas']:
                for idx, meta in enumerate(all_meta['metadatas']):
                    if meta and target_file in meta.get("source", ""):
                        matching_ids.append(all_meta['ids'][idx])
            
            if matching_ids:
                print(f"-> Found {len(matching_ids)} chunks for {target_file}")
                raw_results = collection.get(ids=matching_ids, include=["documents"])
                docs = raw_results['documents']
                
                if len(docs) > 5:
                    print(f"-> File '{target_file}' is large. Scanning for 'Golden Chunks'...")
                    docs = _get_golden_chunks(docs, query_text)
                    print(f"-> Reduced to {len(docs)} relevant chunks.")

                file_context = "\n\n".join(docs)
                context_parts.append(f"--- START OF FILE: {target_file} ---\n{file_context}\n--- END OF FILE: {target_file} ---")
                sources.add(target_file)
            else:
                print(f"-> Warning: File '{target_file}' not found in DB.")

    # 2. Fallback to Vector Search
    if not context_parts:
        print("-> Performing Standard Semantic Search...")
        results = db.similarity_search_with_relevance_scores(query_text, k=5)
        if results:
            context_parts = [doc.page_content for doc, _score in results]
            sources = {doc.metadata.get("source", "unknown") for doc, _score in results}

    # 3. Add the "Official Source" Header
    if context_parts:
        # This header forces the LLM to trust the code implicitly
        header = "!!! CONTEXT FROM OFFICIAL GLEAM STANDARD LIBRARY !!!\n\n"
        final_context = header + "\n\n".join(context_parts)
        return final_context, sources
    
    return "", set()
    

def modelquery(query_text, model, context, sources):
    chain = model | StrOutputParser()
    prompt = PROMPT_TEMPLATE.format(context = context, query = query_text)
    response = chain.invoke(prompt) 

    judge_prompt =  GROUNDING_JUDGE_TEMPLATE.format(context = context, answer = response)
    judge_response = chain.invoke(judge_prompt)

    score_match = re.search(r"SCORE: \s*(\d+)", judge_response)
    grounding_score = score_match.group(1) if score_match else "Unknown"

    final_output =f"--- RESPONSE ---\n{response}"
    metadata = f"--- METADATA ---\nGrounding Score: {grounding_score}%\nSources: {sources}\nJudge Logic: {judge_response.split('REASON:')[-1].strip() if 'REASON:' in judge_response else judge_response}"

    return final_output, metadata