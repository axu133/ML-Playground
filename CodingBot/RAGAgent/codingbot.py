from rag_agent import RAGAgent
import subprocess
import re
import os

SANDBOX_DIR = "sandbox"
FILE_PATH = os.path.join(SANDBOX_DIR, "src/sandbox.gleam")

class CodingBot:
    def __init__(self, RAG, max_retries = 3):
        self.rag = RAG
        self.max_retries = max_retries

    def extract_code(self, text): # Extracts code from LLM output
        code_blocks = re.findall(r"```(?:gleam)?\n(.*?)```", text, re.DOTALL)
        
        if code_blocks:
            full_code = "\n\n".join(block.strip() for block in code_blocks)
            return full_code
        
        if "import gleam" in text and "pub fn main" in text:
            print("   [Parser Warning] No markdown tags found. Using raw text.")
            return text.strip()
        
        return None
    
    def write_to_file(self, code):
        with open(FILE_PATH, 'w') as f:
            f.write(code)
    
    def run_gleam(self):
        result = subprocess.run(
            ["gleam", "run"],
            cwd=SANDBOX_DIR,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    
    def prompt(self, user_request):
        pmpt = user_request

        for attempt in range(self.max_retries):
            #print(f"\n [DEBUG] Prompt:\n{pmpt}")
            response = self.rag.query(pmpt)
            #print(f"\n[DEBUG] Raw LLM Response:\n{response}\n[DEBUG] End Response\n")

            code = self.extract_code(response)

            if not code:
                print("No code block found")
                break
            
            self.write_to_file(code)
            return_code, stdout, stderr = self.run_gleam()

            if return_code == 0:
                return code
            else:
                print("Compiler Error")
                pmpt = f"""The previous code you wrote failed to compile.
USER REQUEST: {user_request}

YOUR CODE:
{code}

COMPILER ERROR:
{stderr}

INSTRUCTIONS:
1. Analyze the error.
2. Fix the code.
3. Output the FULL corrected code block.

OUTPUT FORMAT:
```gleam
[CODE HERE]
```
"""
        print(f"Failed to compile after {self.max_retries} attempts")

if __name__ == "__main__":
    rag = RAGAgent(db_path="chroma_db_gleam")
    bot = CodingBot(rag, 5)

    bot.prompt("Write a program that prints 'Hello World' in all uppercase")


