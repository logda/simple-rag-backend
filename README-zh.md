# 基于 FastAPI 和 LangChain 的 RAG 系统

[English Documentation](README.md)

本项目是一个使用 FastAPI 和 LangChain 构建的简单的检索增强生成（RAG）系统，旨在处理自然语言查询并根据提供的内容生成相关答案。

## 功能特点

- **FastAPI**：一个现代化、快速（高性能）的用于构建 API 的 Web 框架，支持 Python 3.7 及更高版本。
- **LangChain**：一个用于开发由语言模型驱动的应用程序的框架，方便将 LLM 集成到应用程序中。
- **Tongyi**：用于处理和生成查询响应的语言模型（LLM）。

## 快速开始

### 前提条件

- Python 3.7 及以上版本
- pip（Python 包管理器）

### 安装步骤

1. **克隆项目仓库**：

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **创建虚拟环境**（可选，但推荐）：

   ```bash
   python3 -m venv env
   source env/bin/activate  # Windows 系统使用 `env\Scripts\activate`
   ```

3. **安装所需依赖**：

   ```bash
   pip install -r requirements.txt
   ```

4. **设置环境变量**：
   - 根据 `env.example` 模板创建 `.env` 文件。
   - 设置你的环境变量，尤其是 `OPENAI_API_KEY`，如果你使用的是 OpenAI 的模型。

### 运行应用程序

1. **启动 FastAPI 服务器**：

   ```bash
   uvicorn main:app --reload
   ```

2. **访问 API 文档**：
   - FastAPI 服务器将运行在 `http://127.0.0.1:8000`。
   - 交互式 API 文档可以在 `http://127.0.0.1:8000/docs` 访问。

### 示例用法

```bash
curl -X POST "http://127.0.0.1:8000/rag/query" -H "Content-Type: application/json" -d '{
    "prompt": "主要话题是什么？",
    "title": "FastAPI 介绍",
    "content": "FastAPI 是一个现代化、快速的用于构建 API 的 Web 框架，支持 Python 3.7 及以上版本。"
}'
```
