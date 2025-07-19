# RAG - Retrieval-Augmented Generation Repository

This repository contains comprehensive implementations of RAG (Retrieval-Augmented Generation) systems with various search methodologies and Python 3.13 compatibility.

## Python 3.13 Compatibility

This repository has been updated to ensure full compatibility with Python 3.13. All dependencies and code have been verified to work correctly with Python 3.13.

### Requirements

- **Python**: 3.9+ (tested and compatible with Python 3.13)
- **Dependencies**: See `requirements.txt` for complete list

### Installation

1. Ensure you have Python 3.9 or higher (Python 3.13 recommended):
   ```bash
   python --version
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (create a `.env` file):
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Repository Contents

This repository contains implementations of various RAG approaches:

### 1. Keyword Search
- **keyword_1.py**: Basic keyword search using TF-IDF and cosine similarity
- **keyword_2.py**: PDF-based keyword search implementation

### 2. Vector Search  
- **vector.py**: FAISS-based vector search with sentence transformers
- **llama_1.py**: LlamaIndex vector search with Ollama LLM integration

### 3. Hybrid Search
- **Hybrid_1.py**: Combined BM25 and vector search using LangChain and Groq
- **llama_hybrid.py**: LlamaIndex-based hybrid search system

### 4. Advanced RAG
- **rag_with_context.py**: Hybrid RAG system with conversation context memory

## Features

- Multiple search methodologies (keyword, vector, hybrid)
- Conversation context preservation
- Local index storage and retrieval
- Integration with various LLM providers (Groq, Ollama)
- PDF document processing
- Modular and extensible architecture
