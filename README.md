# Advanced RAG Chatbot with Self-Correction

## Project Overview

This project aims to develop an intelligent RAG (Retrieval-Augmented Generation) chatbot that can answer questions based on a custom knowledge base. A key differentiating feature is the implementation of a "self-correction" mechanism to detect and mitigate AI hallucinations or unsupported answers, enhancing reliability.

## Current Status

**Progress:**

- **Python Environment:** Set up a virtual environment and installed core dependencies (`psycopg2-binary`, `openai`, `python-dotenv`).
- **Database Setup:** Configured and launched a PostgreSQL database with the `pgvector` extension using Docker Compose.
- **Database Schema:** Created the `document_chunks` table to store text content, OpenAI embeddings (1536 dimensions), source information, and additional metadata.
- **Credential Management:** Implemented `.env` for secure handling of database and API credentials, and added `.env` to `.gitignore`.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed.
- Python 3.8+ installed.
- An OpenAI API Key (will be used in upcoming steps).

### 1. Clone the Repository

```bash
git clone https://github.com/agajankush/rag_chatbot_self_correction.git
cd rag_chatbot_self_correction
```
