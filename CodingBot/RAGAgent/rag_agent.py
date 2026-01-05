import re
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

GROUNDING_JUDGE_TEMPLATE = """[INST] You are a high-precision Audit Bot. 
Compare the provided ANSWER against the CONTEXT to calculate a Grounding Score.

### CONTEXT:
{context}

### ANSWER:
{answer}

### INSTRUCTIONS:
1. List every specific tool, function, or statistical claim made in the ANSWER.
2. Check if each exists in the CONTEXT.
3. Calculate a Grounding Score (0 to 100). 100 means every single word is backed by context. 0 means it's all outside knowledge or hallucination.
4. Output your response in this EXACT format:
SCORE: [number]
REASON: [one sentence explanation]
[/INST]
"""

PROMPT_TEMPLATE = """[INST] You are a Gleam programming expert.
Answer the user's question using ONLY the context below.

{CODE_RULES}

{GLEAM_CHEAT_SHEET}

EXAMPLES:
EXAMPLE 1:
[INCORRECT]
let x = trim(" hello ")
println(x)

[CORRECT]
import gleam/io
import gleam/string

pub fn main() {{
  let x = string.trim(" hello ")
  io.println(x)
}}

EXAMPLE 2:
[INCORRECT]
fn reverse(list) {{ ...manual code... }}
fn main() {{
  let x = reverse(list)
}}

[CORRECT]
import gleam/list
import gleam/string
import gleam/io

pub fn main() {{
  let pokemon = ["natu", "chimecho"]
  
  // Use pipes and standard library
  let result = pokemon
    |> list.reverse()
    |> string.join(",")
    
  io.println(result)
}}

CONTEXT:
{full_context}

QUESTION:
{query_text} [/INST]
"""

CODE_RULES = """
STRICT CODE RULES:
1. **ALWAYS** start with necessary imports.
2. **ALWAYS** wrap executable code inside `pub fn main() {{ ... }}`.
3. Use 'let' for assignments.
4. **ALWAYS** prefix functions (e.g., `string.trim`).
5. **DO NOT** re-implement standard functions (like `reverse`, `map`, `filter`, `join`). CALL them directly from the `list`, `string`, or `result` modules.
6. **ALWAYS** use the pipe operator `|>` for chaining data transformations.
"""

GLEAM_CHEAT_SHEET = """
Reference for Imports:
- String operations -> import gleam/string
- Integer operations -> import gleam/int
- List operations   -> import gleam/list
- Result/Error handling -> import gleam/result
- Option/Some/None  -> import gleam/option
- Printing/Debug    -> import gleam/io
"""

class RAGAgent:
    def __init__(self, db_path, embedding_model="nomic-embed-text", llm_model="mistral"):
        self.embedding_function = OllamaEmbeddings(model=embedding_model)
        self.db_path = db_path
        self.db = Chroma(persist_directory=db_path, embedding_function=self.embedding_function)
        self.raw_collection = self.db._collection
        self.llm = ChatOllama(model=llm_model)

        self.last_context = None
        self.last_query = None
        self.last_response = None

    def _get_golden_chunks(self, docs, query_text):
        query_words = set(query_text.lower().split())
        stop_words = {"show", "the", "function", "in", "code", "gleam", "how", "what", "implementation", "define", "vs", "and", "or", "difference", "between", "compare", "definition", "of"}
        potential_terms = query_words - stop_words
        
        high_priority = []
        medium_priority = []

        for doc in docs:
            content_lower = doc.lower()
            
            is_def = False
            for term in potential_terms:
                if (f"pub fn {term}" in content_lower or 
                    f"fn {term}" in content_lower or 
                    f"pub type {term}" in content_lower or
                    f"pub opaque type {term}" in content_lower):
                    is_def = True
                    break
            
            if is_def:
                high_priority.append(doc)
            elif any(term in content_lower for term in potential_terms):
                medium_priority.append(doc)

        if high_priority:
            return high_priority 
        elif medium_priority:
            return medium_priority[:10]
        else:
            return docs[:5]

    def refine_query(self, query_text):
        refine_prompt = f"""[INST] You are a Keyword Generator. 
Your ONLY task is to output a space-separated list of technical terms.

INPUT: {query_text}

INSTRUCTIONS:
1. Analyze the INPUT.
2. Output 3-5 relevant API keywords for the Gleam language.
3. OUTPUT FORMAT: pure text, no markdown, no code.

CORRECT EXAMPLES:
input: "how to loop"
output: list.map list.each iterator.iterate recurse

input: "remove spaces"
output: string.trim string.trim_start string.trim_end

input: "parse number"
output: int.parse float.parse result.unwrap

YOUR OUTPUT:
[/INST]"""
        
        chain = self.llm | StrOutputParser()
        refined_output = chain.invoke(refine_prompt).strip()

        clean_text = re.sub(r"```.*?```", "", refined_output, flags=re.DOTALL)
        
        lines = [line for line in clean_text.split('\n') if not any(x in line for x in ["import ", "fn ", "{", "}", "="])]
        
        clean_text = " ".join(lines)
        keywords = re.findall(r"[\w\.]+", clean_text)
        
        final_keywords = " ".join(keywords)
        
        print(f"-> Keywords: '{final_keywords}'")

        return f"{query_text} {final_keywords}"

    def query(self, query_text):
        context_parts = []
        sources = set()
        
        file_matches = re.findall(r"(\w+\.gleam)", query_text)
        
        if file_matches:
            target_files = list(set(file_matches))
            
            all_meta = self.raw_collection.get(include=["metadatas"])
            
            for target_file in target_files:
                matching_ids = []
                
                if all_meta['metadatas']:
                    for idx, meta in enumerate(all_meta['metadatas']):
                        if meta and target_file in meta.get("source", ""):
                            matching_ids.append(all_meta['ids'][idx])
                
                if matching_ids:
                    raw_results = self.raw_collection.get(ids=matching_ids, include=["documents"])
                    docs = raw_results['documents']
                    
                    if len(docs) > 5:
                        docs = self._get_golden_chunks(docs, query_text)

                    file_context = "\n\n".join(docs)
                    context_parts.append(f"--- START OF FILE: {target_file} ---\n{file_context}\n--- END OF FILE: {target_file} ---")
                    sources.add(target_file)

        if not context_parts:
            effective_query = self.refine_query(query_text)

            results = self.db.similarity_search_with_relevance_scores(effective_query, k=5)
            if results:
                context_parts = [doc.page_content for doc, _score in results]
                sources = {doc.metadata.get("source", "unknown") for doc, _score in results}

        if not context_parts:
            return "I could not find any relevant information in the database."

        header = "!!! CONTEXT FROM OFFICIAL GLEAM STANDARD LIBRARY !!!\n\n"
        full_context = header + "\n\n".join(context_parts)

        prompt = PROMPT_TEMPLATE.format(CODE_RULES = CODE_RULES, GLEAM_CHEAT_SHEET = GLEAM_CHEAT_SHEET, full_context=full_context, query_text=query_text)

        chain = self.llm | StrOutputParser()
        response = chain.invoke(prompt)
        
        self.last_context = full_context
        self.last_query = query_text
        self.last_response = response

        return response
    
    def evaluate_last_response(self):
        if not self.last_context or not self.last_response:
            return "No previous query to evaluate."

        prompt = GROUNDING_JUDGE_TEMPLATE.format(
            context=self.last_context,
            answer=self.last_response
        )
        
        chain = self.llm | StrOutputParser()
        judge_output = chain.invoke(prompt)
        
        score_match = re.search(r"SCORE: \s*(\d+)", judge_output)
        score = int(score_match.group(1)) if score_match else 0
        
        return {
            "score": score,
            "is_grounded": score >= 90,
            "full_evaluation": judge_output
        }

if __name__ == "__main__":
    agent = RAGAgent(db_path="CodingBot/RAGAgent/chroma_db_gleam")
    
    query = "How do I create a key-value map from a list of tuples?"

    response = agent.query(query)
    print("--- AGENT RESPONSE ---")
    print(response)
    
    """
    print("\n--- GROUNDING EVALUATION ---")
    eval_result = agent.evaluate_last_response()
    print(eval_result['full_evaluation'])
    """