# RAG System with FastAPI and LangChain

[中文文档](README-zh.md)

This project is a simple Retrieval-Augmented Generation (RAG) system using FastAPI and LangChain. It is designed to process natural language queries and provide relevant answers based on the provided content.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **LangChain**: A framework for developing applications powered by language models, facilitating the integration of LLMs into the application.
- **Tongyi**: An LLM used for processing and generating responses to queries.

## Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**:
   - Create a `.env` file based on the `env.example` template.
   - Set your environment variables, particularly `OPENAI_API_KEY` if using OpenAI's models.

### Running the Application

1. **Start the FastAPI server**:

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation**:
   - The FastAPI server will be available at `http://127.0.0.1:8000`.
   - Interactive API docs will be available at `http://127.0.0.1:8000/docs`.

### Example Usage

```bash
curl -X POST "http://127.0.0.1:8000/rag/query" -H "Content-Type: application/json" -d '{
    "prompt": "What is the main topic?",
    "title": "Introduction to FastAPI",
    "content": "FastAPI is a modern, fast web framework for building APIs with Python 3.7+."
}'
```
