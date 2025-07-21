# agent/synthesis.py

from langchain_community.llms import Ollama

def synthesize_answer(subquestion, context_chunks):
    """
    Synthesizes an answer for a sub-question using relevant text chunks and LLM.
    Returns the generated answer as a string.
    """
    llm = Ollama(model="mistral:latest")
    context = "\n\n".join(chunk.page_content for chunk in context_chunks)
    prompt = (
        f"Based on the following information, answer this sub-question clearly, concisely, "
        f"with citations for each claim (use [source] if the chunk metadata includes a source):\n\n"
        f"Sub-question: {subquestion}\n\n"
        f"Context:\n{context}\n"
        "If context includes a 'source' metadata, use it as a citation."
    )
    answer = llm(prompt)
    return answer

def generate_report(subquestions, answers, sources):
    """
    Assembles the full report from all sub-question answers.
    Returns a formatted string (can be saved as .md or .txt).
    """
    report = "# Research Report\n\n"
    report += "## Executive Summary\n"
    report += "This report answers the key research question using multiple sources and synthesized findings.\n\n"
    
    for i, (subq, ans) in enumerate(zip(subquestions, answers), 1):
        report += f"### {i}. {subq}\n{ans}\n\n"

    # Adding the references with clickable links
    report += "## References\n"
    for idx, source in enumerate(sources, 1):
        report += f"[{idx}]: {source}\n"
    
    return report


# # Example usage
# if __name__ == "__main__":
#     # Fake context chunks for demo
#     from langchain_core.documents import Document
#     chunks = [Document(page_content="AI has improved cancer detection rates in recent studies. [source: arXiv:2007.07892]")]
#     answer = synthesize_answer("How has AI improved cancer diagnostics?", chunks)
#     print(answer)
