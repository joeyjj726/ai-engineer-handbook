# First AI

A hands-on AI engineering project built with Python, FastAPI, and Ollama.

## Features

- Local LLM with Ollama
- REST API integration
- FastAPI backend
- Interactive API documentation (Swagger)
- Context window demonstration
- Conversation history (Terminal version)

---

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Ollama
- Qwen3 8B
- Requests
- uv

---

## Project Structure

```
first-ai/
│
├── app.py              # FastAPI backend
├── chat.py             # Terminal chatbot
├── raw_api.py          # Raw Ollama REST API example
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your_repo_url>
cd first-ai
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull qwen3:8b
```

---

## Running the Project

### Start Ollama

If using Homebrew:

```bash
brew services start ollama
```

Check status:

```bash
brew services list
```

---

### Start FastAPI

```bash
uv run uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

### Run Terminal Chat

```bash
uv run chat.py
```

---

## Useful Commands

```bash
# Enter project
cd ~/AI/projects/first-ai

# Start FastAPI
uv run uvicorn app:app --reload

# Run terminal chatbot
uv run chat.py

# List installed models
ollama list

# Check Ollama service
brew services list

# Start Ollama
brew services start ollama

# Stop Ollama
brew services stop ollama
```

---

## Lessons Completed

### Lesson 1

- Calling Ollama REST API
- Building a simple chatbot
- Understanding HTTP requests and responses

### Lesson 2

- Conversation history
- Context Window
- Prompt Tokens
- Output Tokens

### Lesson 3

- FastAPI basics
- REST API
- Swagger
- Pydantic models
- Connecting FastAPI to Ollama

---

## Next Steps

- Session Management
- Streaming Responses
- Prompt Engineering
- Embeddings
- Vector Database
- RAG
- AI Agents
- MCP
