# Sample Requirements Document for Testing

This is a test document for the RAG system.

## Functional Requirements

**FR-1**: The system shall allow users to upload documents in PDF, Markdown, PowerPoint, and EPUB formats.

**FR-2**: The system shall provide a natural language interface for querying document contents.

**FR-3**: The system shall return answers with source citations including page/slide/chapter references.

## Non-Functional Requirements

**NFR-1**: The system must respond to queries within 5 seconds on standard hardware.

**NFR-2**: The system shall maintain 99% accuracy in retrieving relevant document sections.

**NFR-3**: The system shall support offline operation without internet connectivity.

## Technical Requirements

**TR-1**: The system shall use FAISS for vector similarity search.

**TR-2**: The system shall support local LLM inference via Ollama.

**TR-3**: The system shall implement automatic index rebuilding when source documents change.
