# Multi-Source RAG Application

A dynamic, production-ready Retrieval-Augmented Generation (RAG) system built with **LangChain**, **Streamlit**, and **FAISS**. This application allows you to seamlessly orchestrate local knowledge retrieval while integrating multi-modal document ingestion entirely from the UI.

![Streamlit UI Snapshot](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit) 
![Langchain](https://img.shields.io/badge/Orchestration-LangChain-1C3C3C?style=for-the-badge)
![Ollama Local Embeddings](https://img.shields.io/badge/Embeddings-Ollama-white?style=for-the-badge)
![Groq Generative](https://img.shields.io/badge/Generative_LLM-Groq-f55036?style=for-the-badge)

## 📌 Features

- **Dynamic Data Ingestion**: Add URLs, physical PDF files, and Text documents securely via the Streamlit interface. 
- **Active Metadata Tracking**: View exactly what documents are inside your semantic memory using a robust visual mapping system (`sources.json`).
- **Graceful Error Rejection**: Advanced validation logic prevents database crashes (e.g., catching and rejecting scan-only PDFs that contain zero readable strings).
- **Reranking Integration**: Incorporates `ms-marco` cross-encoder capabilities to strictly re-rank search results and prevent hallucinations before the context enters the LLM window.
- **One-Click Database Nuke**: Cleanly wipe your entire FAISS structural array and audit logs seamlessly straight from the UI sidebar. 

---

## 🚀 Getting Started

### 1. Prerequisites 
- Python 3.9+
- An active `GROQ_API_KEY`
- **Ollama** installed on your system running the local embedding model:
  ```bash
  ollama pull nomic-embed-text
  ```

### 2. Environment Configuration
Create a `.env` file in the root of the directory and assign your Groq API key:
```env
GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxx"
```

### 3. Installation
Install the required system dependencies:
```bash
pip install -r requirements.txt
```

### 4. Running the Platform
Boot up the Streamlit interface:
```bash
python -m streamlit run app/streamlit_app.py
```

---

## 🛠️ Architecture 

1. `app/streamlit_app.py`: The frontend UI managing physical uploads and visual configurations. 
2. `main.py`: Coordinates dynamic embedding insertions, validation logic, and querying systems.
3. `config/settings.py`: Constant declarations and fallback configurations. 
4. `ingestion/`: Specialized pipeline utilities allowing web scraping, recursive character chunking, and embedded local conversion.
5. `retrieval/`: Handles memory retrieval natively routing FAISS document nodes.
6. `generation/`: Contains LLM endpoints and strict grounding prompt design.
