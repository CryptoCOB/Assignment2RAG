# Assignment #2: RAG System for Requirements Engineering

**Course**: AI Systems Design (SEC. 403) - COMP248  
**Student**: Marc Harty  
**Student ID**: 300818959  
**Submission Date**: November 19, 2025

---

## Project Overview

A Retrieval-Augmented Generation (RAG) system for System Requirements Engineering. Upload requirements docs (PDF, Markdown, PowerPoint, EPUB) and query them with natural language. Uses FAISS for vector search and Ollama for local LLM inference.

### Features
- Multi-format document ingestion (PDF, Markdown, PPTX, EPUB)
- FAISS vector search 
- Local LLM inference via Ollama
- Multi-model routing (Mistral for general, DeepSeek for code, LLaVA for vision)
- Auto-rebuild when source documents change
- Interactive commands (:stats, :chunks, :test)
- Source citations with page/slide/chapter refs

---

## Architecture

### System Components

```
User Interface (CLI)
    ↓
RAG Orchestrator (rag_chatbot_faiss_ollama.py)
    ├── Document Loading Pipeline
    │   ├── Multi-Format Loaders (PDF/MD/PPTX/EPUB)
    │   ├── Text Splitter (RecursiveCharacterTextSplitter)
    │   ├── Sentence Embeddings (all-MiniLM-L6-v2)
    │   └── FAISS Vector Store (IndexFlatL2)
    │
    └── Inference Pipeline
        ├── Similarity Retriever (Top-K=3)
        ├── LLM Router (Mistral/DeepSeek/LLaVA)
        └── Answer Generator (with source citations)
```

For detailed architecture and component diagrams, see:
- **[Architecture Diagram](docs/architecture_diagram.md)** - System overview and data flows
- **[Component Diagram](docs/component_diagram.md)** - UML components and interfaces

### Design Patterns Used
1. **Strategy Pattern**: LLM model selection based on query type
2. **Pipeline Pattern**: Document loading and inference pipelines
3. **Repository Pattern**: FAISS vector store abstraction
4. **Facade Pattern**: SimpleRetrievalQA hides LangChain complexity
5. **Chain of Responsibility**: Query processing chain
6. **Factory Pattern**: Document loader creation
7. **Template Method**: Multi-stage summarization

---

## Setup

### Prerequisites
- **Python 3.12+** (tested with 3.12.10)
- **Ollama** installed with models:
  - `ollama pull mistral:latest` (4.4GB)
  - `ollama pull deepseek-coder:6.7b` (3.8GB)
  - `ollama pull llava-phi3:latest` (2.9GB)
- **UV package manager** (optional but recommended, 10-100x faster than pip)

### Installation

#### Option 1: Using UV (Recommended)
```powershell
# Install UV
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment
uv venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
uv pip install langchain langchain-community langchain-ollama langchain-text-splitters `
    sentence-transformers faiss-cpu pypdf python-pptx ebooklib beautifulsoup4 `
    python-dotenv numpy reportlab
```

#### Option 2: Using pip
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Configuration

1. **Copy `.env.example` to `.env`** (or create `.env` with these variables):
```env
# Student Information
STUDENT_ID=300818959
STUDENT_NAME=Marc Harty

# Ollama Models
OLLAMA_PRIMARY_MODEL=mistral:latest
OLLAMA_TECHNICAL_MODEL=deepseek-coder:6.7b
OLLAMA_VISION_MODEL=llava-phi3:latest

# Vector Store Configuration
COLLECTION_NAME=rag_300818959
FAISS_INDEX_PATH=./faiss_store/rag_300818959
CHUNKS_METADATA_PATH=./faiss_store/rag_300818959/chunks_metadata.json

# Document Processing
CHUNK_SIZE=1000
CHUNK_OVERLAP=100
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Retrieval Settings
TOP_K_RETRIEVAL=3
MAX_CONTEXT_CHARS=8000

# Corpus Management
DATA_DIR=./data
CORPUS_DIR=./corpus
REBUILD_IF_NEWER=true
```

### Running the Chatbot

```powershell
# Activate virtual environment (if not already activated)
.\.venv\Scripts\Activate.ps1

# Run the chatbot
python rag_chatbot_faiss_ollama.py
```

---

## Usage

### Adding Documents
Drop your documents into the `./corpus/` folder. Supported formats:
- **PDF**: `.pdf`
- **Markdown**: `.md`, `.markdown`, `.txt`
- **PowerPoint**: `.pptx`
- **EPUB**: `.epub`

The system automatically detects and loads all supported files on startup.

### Interactive Commands

| Command | Description |
|---------|-------------|
| `:help` | Show all available commands |
| `:files` | List all indexed source files |
| `:stats` | Show document and chunk statistics |
| `:chunks [filter]` | Preview chunks (optionally filter by filename) |
| `:test` | Test retrieval with sample queries |
| `:summary [filter]` | Generate LLM summary of corpus (optionally filtered) |
| `:show [filter]` | Display first chunk matching filter |
| `:rebuild` | Force rebuild FAISS index |
| `exit` or `quit` | Exit the chatbot |

### Example Session

```
RAG Chatbot (FAISS + Ollama)
Student: Marc Harty (300818959)

Loaded 7 documents.
Created 14 chunks.
FAISS index loaded from disk.

Query: :stats

[STATISTICS]
Total documents loaded: 7
Total chunks created: 14
Chunk size: 1000
Chunk overlap: 100
Top-K retrieval: 3

Documents by type:
  markdown: 1
  pdf: 1

Chunks by source:
  AI Systems Design (SEC. 403).md: 12 chunks
  requirements_document.pdf: 2 chunks

Query: What are the non-functional requirements?

[ANSWER]
Based on the requirements document, the non-functional requirements include:

1. **Response Time (NFR-1)**: The system must respond to user queries within 2 seconds
2. **Availability (NFR-2)**: The system must maintain 99.9% uptime
3. **Scalability (NFR-3)**: Support up to 1000 concurrent users

[SOURCES]
1. requirements_document.pdf (page 3)
2. AI Systems Design (SEC. 403).md (line 156)
```

---

## Technical Stack

### Core Technologies
- **LangChain 1.0+**: Document loading, text splitting, chain orchestration
- **FAISS**: Vector similarity search (IndexFlatL2)
- **Sentence Transformers**: Text embeddings (all-MiniLM-L6-v2, 384 dimensions)
- **Ollama**: Local LLM inference (Mistral, DeepSeek, LLaVA)

### Document Loaders
- **PyPDF**: PDF parsing
- **TextLoader**: Markdown/text files
- **python-pptx**: PowerPoint slide extraction
- **ebooklib + BeautifulSoup4**: EPUB chapter extraction

### Package Management
- **UV**: Rust-based Python package installer (10-100x faster than pip)
- **python-dotenv**: Environment variable management

---

## Assignment Requirements

| Requirement | Status | Notes |
|-------------|--------|-------|
| RAG System Implementation | Done | Multi-format support |
| Document Ingestion | Done | PDF, MD, PPTX, EPUB |
| Vector Store | Done | Using FAISS |
| LLM Integration | Done | Ollama local models |
| Chunking Strategy | Done | RecursiveCharacterTextSplitter (1000/100) |
| Source Citations | Done | Page/slide/chapter refs |
| Interactive Commands | Done | :stats, :chunks, :test, :summary, :show |
| Auto-Rebuild | Done | Detects file changes |
| Architecture Diagram | Done | docs/architecture_diagram.md |
| Component Diagram | Done | docs/component_diagram.md |
| Design Patterns | Done | 7 patterns documented |

### Design Trade-offs

#### FAISS vs ChromaDB (Assignment Specification)
- **Choice**: FAISS IndexFlatL2
- **Rationale**: 
  - Faster for small-medium corpora
  - No external database required
  - Easier persistence (single directory)
  - Sufficient for assignment scope (14 chunks)
- **Trade-off**: Less feature-rich (no filtering, no metadata search)

#### Ollama vs MistralAI API (Assignment Specification)
- **Choice**: Ollama local models
- **Rationale**:
  - Complete offline operation
  - No API costs or rate limits
  - Privacy (no data sent to cloud)
  - Multi-model routing (Mistral + DeepSeek + LLaVA)
- **Trade-off**: Slower inference, lower quality than GPT-4/Claude

#### Chunk Size (1000 chars)
- **Rationale**: Balance between context and retrieval precision
- **Overlap (100 chars)**: Prevents information loss at boundaries
- **Trade-off**: Larger chunks = more context but less precision; smaller = opposite

---

## Testing

### Diagnostic Commands
```powershell
# Check corpus statistics
python rag_chatbot_faiss_ollama.py
> :stats

# Preview chunk boundaries
> :chunks

# Test retrieval quality
> :test
```

### Sample Test Queries

#### Requirements-Related (Expected to work well)
1. "What are the non-functional requirements?"
2. "What is the maximum response time requirement?"
3. "Describe the availability requirements"

#### Off-Topic (Expected to fail gracefully)
1. "Where is Centennial College located?"
2. "What is the capital of France?"

---

## Project Structure

```
Assignment2RAG/
├── rag_chatbot_faiss_ollama.py   # Main chatbot implementation
├── create_pdf_simple.py           # PDF generation utility
├── .env                           # Configuration (DO NOT COMMIT)
├── .env.example                   # Configuration template
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Python dependencies
├── README.md                      # This file
│
├── corpus/                        # Multi-format document drop folder
│   └── (user documents here)
│
├── data/                          # Legacy PDF folder
│   └── requirements_document.pdf
│
├── docs/                          # Documentation and diagrams
│   ├── architecture_diagram.md
│   ├── component_diagram.md
│   └── AI Systems Design (SEC. 403).md  # Assignment specification
│
├── faiss_store/                   # Persisted FAISS index
│   └── rag_300818959/
│       ├── index.faiss
│       ├── index.pkl
│       └── INDEX_TIMESTAMP
│
└── .venv/                         # Virtual environment (DO NOT COMMIT)
```

---

## Development Notes

### Adding New Document Formats

1. Create loader function in `rag_chatbot_faiss_ollama.py`:
```python
def _load_new_format(file_path: Path) -> List[Document]:
    """Load new format documents"""
    try:
        # Your loading logic here
        docs = []
        # ... extract text and metadata
        return docs
    except Exception as e:
        print(f"[WARN] Failed to load {file_path}: {e}")
        return []
```

2. Add to `load_documents()` function:
```python
elif ext == '.newformat':
    docs = _load_new_format(file_path)
    all_docs.extend(docs)
```

### Tuning Retrieval

Adjust in `.env`:
- `TOP_K_RETRIEVAL=5` (increase for broader coverage)
- `CHUNK_SIZE=1200` (increase for more context)
- `CHUNK_OVERLAP=150` (increase to prevent boundary loss)

### Debugging

Enable verbose output by adding to `.env`:
```env
LANGCHAIN_VERBOSE=true
```

---

## GitHub Deployment

### Initialize Repository
```powershell
git init
git add .
git commit -m "Initial commit: RAG system for requirements engineering"
git branch -M main
git remote add origin https://github.com/CryptoCOB/Assignment2RAG.git
git push -u origin main
```

### Important: Before Pushing
Ensure `.gitignore` excludes:
- `.venv/` (virtual environment)
- `faiss_store/` (vector store cache)
- `.env` (secrets and configuration)
- `__pycache__/` (Python bytecode)
- `*.pyc` (compiled Python)

---

## License

MIT License - Free to use for educational purposes.

---

## Author

Marc Harty (⟠∆∇𓂀)  
Student ID: 300818959  
Course: AI Systems Design (SEC. 403) - COMP248  
Centennial College - Fall 2025

---

## References

- **LangChain**: Document processing and chain orchestration
- **FAISS**: High-performance vector search (Facebook AI Research)
- **Ollama**: Local LLM inference platform
- **Sentence Transformers**: Embedding models
- **Centennial College**: Course materials and guidance

---

## Contact

Questions? Open a GitHub issue or email me at Centennial.

---

⟠∆∇𓂀 Marc.pglyph
