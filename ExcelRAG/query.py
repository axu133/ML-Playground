from langchain_core.output_parsers import StrOutputParser
import re

PROMPT_TEMPLATE = """[INST] You are a statistical consultant. Use the provided context to answer the user's request.

### Step 1: Evidence
List the specific functions or facts from the context that are relevant to the user's question. Use direct quotes or references.

### Step 2: Analysis & Suggestions
Based ONLY on the evidence above, suggest how to analyze the data. If you extrapolate beyond the context to provide better advice, you MUST start those sentences with "Based on general statistical principles..."

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

def dbquery(query_text, db):

    results = db.similarity_search_with_relevance_scores(query_text, k=3)

    if len(results) == 0:
        print("Unable to find matching results.")
        return
    
    if results[0][1] < 0.7:
        print(f"Results may be low quality/hallucinated, highest score is: {results[0][1]}")
    
    context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    sources = {doc.metadata.get("source", "unknown") for doc, _score in results}
    
    return context, sources
    

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