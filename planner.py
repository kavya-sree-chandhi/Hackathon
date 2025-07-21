# agent/planner.py
from langchain_ollama import OllamaLLM

def generate_subquestions(query):
    llm = OllamaLLM(model="mistral:latest")
    prompt = (
        "Decompose the research question into 3-5 specific, answerable sub-questions:\n"
        f"{query}\n"
        "Return as a numbered list."
    )
    response = llm.invoke(prompt)
    subqs = []
    for line in response.splitlines():
        line = line.strip()
        if line and (line[0].isdigit() or line.startswith("-")):
            subqs.append(line.lstrip("1234567890.-) ").strip())
    return subqs
