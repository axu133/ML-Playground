from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
CHROMA_PATH = "chroma_split"
model = ChatOllama(model="mistral")
PROMPT_TEMPLATE = """
You are a strict assistant. Answer the question ONLY using the provided context.
If the answer is not in the context, say "I do not know the answer because it is not in my database."

Context: {context}
Question: {query}
"""

db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

def query(query_text):

    results = db.similarity_search_with_relevance_scores(query_text, k=3)

    if len(results) == 0:
        print("Unable to find matching results.")
        return
    
    if results[0][1] < 0.7:
        print(f"Results may be low quality, highest score is: {results[0][1]}")
    
    context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    prompt = PROMPT_TEMPLATE.format(context = context, query = query_text)

    print("LLM Prompted")
    response = model.invoke(prompt)

    return response

answer = query("I have data on consumer spending patterns, give me some suggestions on how I can analyze the data. The data is what they purchased, how much they purchased it for, and what quantity.")
print(answer.content) # type: ignore