# 🧠 AI Research Agent for Healthcare Diagnostics

This project is an intelligent research assistant that automates literature review and question-answering for medical diagnostics using AI. It focuses on domain-specific topics such as breast cancer and brain tumor detection, leveraging cutting-edge technologies like LLMs, vector stores, and academic/web scraping.

> 📌 Example Question: _"How does AI help to detect brain tumors?"_

## 🚀 Features

- 🔍 Automatically generates sub-questions from user queries using an LLM
- 🌐 Gathers information from:
  - Web sources (via DuckDuckGo/Google search)
  - Academic sources (arXiv and PubMed)
  - Local PDF files (`/docs` folder)
- 📚 Performs document chunking, embedding, and vector search
- 🧠 Synthesizes high-quality answers for each sub-question
- 📝 Generates a final report with:
  - Findings (Finding 1, Finding 2...)
  - Executive Summary
  - IEEE-style hyperlinked References
- 📄 Export options: PDF, Word (.docx), Markdown, and Text

---

## 🛠️ Tech Stack

| Component       | Technology               |
|----------------|---------------------------|
| UI             | [Streamlit](https://streamlit.io/) |
| LLM            | [Ollama](https://ollama.com/) + LLaMA3 |
| Text Splitter  | LangChain RecursiveCharacterTextSplitter |
| Embedding      | [nomic-embed-text](https://docs.nomic.ai/) |
| Vector DB      | In-memory FAISS via LangChain |
| PDF Parsing    | PyMuPDF (`fitz`)          |
| Word/PDF Export| `python-docx`, `fpdf`     |

---

## Architecture diagram
