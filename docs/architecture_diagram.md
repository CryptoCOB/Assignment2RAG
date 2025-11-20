# RAG System Architecture

## High-Level Architecture

```mermaid
flowchart TB
    User[User Interface<br/>Interactive CLI]
    
    subgraph Orchestrator[RAG Orchestrator]
        Router[Query Router]
        Commands[Command Handler]
    end
    
    subgraph LoadingPipeline[Document Loading Pipeline]
        Loaders[Multi-Format Loaders<br/>PDF, MD, PPTX, EPUB]
        Splitter[Text Splitter<br/>Chunk Size: 1000<br/>Overlap: 100]
        Embedder[Sentence Embeddings<br/>all-MiniLM-L6-v2]
        Index[FAISS Vector Store<br/>IndexFlatL2]
    end
    
    subgraph InferencePipeline[Inference Pipeline]
        Retriever[Similarity Retriever<br/>Top-K=3]
        LLMRouter[LLM Router]
        Mistral[Mistral<br/>General Queries]
        DeepSeek[DeepSeek Coder<br/>Technical Queries]
        LLaVA[LLaVA Phi3<br/>Vision Queries]
        Generator[Answer Generator]
    end
    
    CorpusFiles[(Corpus Files<br/>PDF, MD, PPTX, EPUB)]
    FAISSStore[(FAISS Index<br/>Persisted)]
    
    User -->|Query/Command| Orchestrator
    
    Orchestrator -->|Document Management| LoadingPipeline
    Orchestrator -->|Question Answering| InferencePipeline
    
    CorpusFiles -->|Read| Loaders
    Loaders -->|Documents| Splitter
    Splitter -->|Chunks| Embedder
    Embedder -->|Vectors| Index
    Index -->|Save| FAISSStore
    FAISSStore -->|Load| Index
    
    Router -->|Query| Retriever
    Index -->|Search| Retriever
    Retriever -->|Context| LLMRouter
    
    LLMRouter -->|General| Mistral
    LLMRouter -->|Technical| DeepSeek
    LLMRouter -->|Vision| LLaVA
    
    Mistral --> Generator
    DeepSeek --> Generator
    LLaVA --> Generator
    
    Generator -->|Answer + Sources| User
    Commands -->|Stats/Chunks/Test| User
    
    style User fill:#e1f5ff
    style Orchestrator fill:#fff4e1
    style LoadingPipeline fill:#e8f5e9
    style InferencePipeline fill:#f3e5f5
    style CorpusFiles fill:#fce4ec
    style FAISSStore fill:#fce4ec
```

## Component Interaction Flow

### Document Ingestion Flow
1. **Corpus Scanning**: System scans `./corpus/` and `./data/` directories
2. **Format Detection**: Identifies file types (PDF, MD, PPTX, EPUB)
3. **Document Loading**: Format-specific loaders extract text + metadata
4. **Text Splitting**: RecursiveCharacterTextSplitter creates chunks (1000 chars, 100 overlap)
5. **Embedding Generation**: SentenceTransformer creates 384-dim vectors
6. **Index Building**: FAISS IndexFlatL2 stores vectors for similarity search
7. **Persistence**: Index saved to `./faiss_store/rag_300818959/`

### Query Processing Flow
1. **User Input**: User submits natural language query
2. **Command Check**: Router checks for special commands (`:stats`, `:chunks`, etc.)
3. **Vector Search**: Query embedded → FAISS finds top-K similar chunks
4. **Context Retrieval**: Top-3 chunks retrieved with metadata (source, page)
5. **LLM Selection**: Router chooses model based on query keywords
   - Technical keywords → DeepSeek Coder
   - Vision keywords → LLaVA Phi3
   - Default → Mistral
6. **Answer Generation**: LLM synthesizes answer from retrieved context
7. **Source Citation**: System returns answer with source references

### Auto-Rebuild Mechanism
- **Trigger**: File modification time newer than FAISS index timestamp
- **Action**: Automatic re-ingestion and re-indexing
- **Control**: Configurable via `REBUILD_IF_NEWER=true` in `.env`

## Key Design Decisions

### Why FAISS over ChromaDB?
- **Performance**: FAISS optimized for similarity search (Facebook AI Research)
- **Offline**: No external dependencies, runs completely local
- **Simplicity**: Lightweight, easy to persist and load
- **Trade-off**: Less feature-rich than ChromaDB but sufficient for assignment

### Why Ollama over MistralAI API?
- **Privacy**: All processing local, no data sent to cloud
- **Cost**: Free, no API tokens required
- **Offline**: Works without internet connection
- **Trade-off**: Slower inference, lower quality than cloud GPT-4/Claude

### Why Multi-Model Routing?
- **Specialization**: DeepSeek excels at code, LLaVA handles images
- **Quality**: Task-appropriate models produce better answers
- **Flexibility**: Easy to add new models for specific domains

### Why RecursiveCharacterTextSplitter?
- **Semantic Coherence**: Tries to split on sentence/paragraph boundaries
- **Overlap**: 100-char overlap prevents context loss at boundaries
- **Configurable**: Chunk size tunable via `.env`
