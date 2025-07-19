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

## Testing and Running the Code

### Quick Start Testing
Run the comprehensive test suite to verify all scripts work:
```bash
python3 run_all_tests.py
```

### Individual Script Testing
Test individual components:
```bash
# Test keyword search
python3 test_keyword_1.py
python3 test_keyword_2.py

# Test vector search
python3 test_vector.py
python3 test_llama_1.py

# Test hybrid search
python3 test_hybrid_1.py
python3 test_llama_hybrid.py

# Test RAG with context
python3 test_rag_with_context.py
```

### Running Original Interactive Scripts
To run the original interactive scripts:
```bash
# Keyword search examples
python3 "Keyword Search/keyword_1.py"
python3 "Keyword Search/keyword_2.py"

# Vector search examples
python3 "Vector Search/vector.py"
python3 "Vector Search/llama_1.py"

# Hybrid search examples
python3 "Hybrid Search/Hybrid_1.py"
python3 "Hybrid Search/llama_hybrid.py"

# Advanced RAG
python3 rag_with_context.py
```

## API Key Requirements

### Scripts that require GROQ_API_KEY:
- `rag_with_context.py` - **Required** for LLM functionality
- `Hybrid Search/Hybrid_1.py` - **Required** for answer generation
- `Hybrid Search/llama_hybrid.py` - **Required** for LLM functionality

### Scripts that work without API keys:
- `Keyword Search/keyword_1.py` - Basic TF-IDF search
- `Keyword Search/keyword_2.py` - PDF keyword search
- `Vector Search/vector.py` - FAISS vector similarity search

### Scripts with external dependencies:
- `Vector Search/llama_1.py` - May require Ollama setup for local LLM

## Troubleshooting

### Common Issues

1. **Missing API Key Error**
   ```
   ValueError: GROQ_API_KEY environment variable is required
   ```
   **Solution**: Set your Groq API key in the `.env` file

2. **PDF Not Found Error**
   ```
   FileNotFoundError: [Errno 2] No such file or directory: 'data/sample.pdf'
   ```
   **Solution**: Ensure PDF files exist in the respective data directories

3. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'llama_index'
   ```
   **Solution**: Run `pip install -r requirements.txt`

4. **Ollama Connection Error** (for llama_1.py)
   ```
   Connection refused to Ollama server
   ```
   **Solution**: Install and start Ollama locally, or modify script to use different LLM

### Data Requirements
- `Keyword Search/keyword_2.py`: Requires PDF files in `Keyword Search/data/`
- `Vector Search/`: May use PDF files in `Vector Search/data/`
- `Hybrid Search/`: May use PDF files in `Hybrid Search/data/`

### Performance Notes
- First run may be slower due to model downloads (sentence-transformers, etc.)
- Cache directories will be created automatically for embeddings
- Vector indices are built on-the-fly for demonstration purposes
