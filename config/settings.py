# config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# API KEYS
# =========================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# =========================
# DATA SOURCES
# =========================

DATA_SOURCES = [
    {"type": "web", "path": "https://python.langchain.com/docs/introduction/"},
    {"type": "web", "path": "https://python.langchain.com/docs/modules/agents/"}
]


# =========================
# CHUNKING
# =========================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


# =========================
# RETRIEVAL
# =========================

TOP_K = 5
RERANK_TOP_N = 3


# =========================
# MODEL SETTINGS
# =========================

MODEL_NAME = "mixtral-8x7b-32768"
TEMPERATURE = 0


# =========================
# VECTOR STORE
# =========================

INDEX_PATH = "index"