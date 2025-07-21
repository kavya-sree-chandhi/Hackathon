# 🧠 AI Research Agent for Healthcare Diagnostics

This project is an intelligent research assistant that autonomously conducts research, synthesizes information, and produces a comprehensive report on a given research question.This project automates literature review and question-answering for medical diagnostics using AI. It focuses on domain-specific topics such as breast cancer and brain tumor detection, leveraging cutting-edge technologies like LLMs, vector stores, and academic/web scraping.

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
![Research_Agent_Architecture drawio](https://github.com/user-attachments/assets/d1503e7b-39ee-41b3-a614-d2d6409df785)

The system is designed in 4 layers, implemented as shown in the architecture diagram.

1️⃣ User Interface
Implemented with Streamlit

Accepts user research topic

Displays real-time progress of research nodes

Shows final report and allows export

2️⃣ Orchestration Layer
Implemented using LangGraph

Defines workflow as a graph of nodes and edges

Nodes:

📋 Planner Node: breaks down research topic into sub-questions

🔍 Information Gatherer Node: queries multiple sources

📝 Synthesis Node: organizes and drafts findings

✅ Verifier Node: fact-checks and assigns confidence scores

📄 Report Generator Node: formats final report, adds citations & summary

Handles state management, retries, and conditional flows

3️⃣ Data & Knowledge Sources
🌐 Web Search: DDGS (DuckDuckGo Search API)

📚 Academic Papers: PubMed, arXiv

📄 Local Documents: PDF/text parser (PyMuPDF)

4️⃣ LLM & Reasoning
Powered by LLaMA (mistral:latest)

Responsible for planning, summarizing, verifying, and writing

## 📝 Setup & Installation

Prerequisites:

Python 3.10+

pip

virtualenv

## Clone the repository

git clone https://github.com/<your-username>/intelligent-research-assistant.git

cd intelligent-research-assistant

## Create virtual environment & activate

python -m venv venv

source venv/bin/activate     # Linux/macOS

venv\Scripts\activate        # Windows

## Install dependencies

pip install -r requirements.txt

## Run the application

streamlit run app.py

## 📷 Demo



https://github.com/user-attachments/assets/bfa77ba6-315c-433a-b86a-7ce84abc1b3c






