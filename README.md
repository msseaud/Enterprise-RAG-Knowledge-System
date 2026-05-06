# Enterprise-RAG-Knowledge-System

## 🚀 Overview

This project implements a lightweight RAG (Retrieval-Augmented Generation) knowledge system for document-based question answering.

## ⚙️ Features

* Semantic search based on embeddings
* Simple API interface using FastAPI
* Modular architecture (API / Core / Memory)
* Extensible for multi-agent pipelines

## 📦 Installation

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
uvicorn app:app --reload
```

## 🧪 Demo

### Example Query

Input:

```
What is RAG?
```

Output:

```
RAG (Retrieval-Augmented Generation) combines retrieval and generation to improve answer quality.
```

## 🧠 Architecture

```
Query → Retriever → Generator → Response
```

## 📊 Example Logs

```
[INFO] System started
[INFO] Loading embeddings model
[INFO] Vector store initialized

[QUERY] What is RAG?
[Retriever] Found relevant documents
[Generator] Answer generated
```

## 📌 Status

This project has been tested locally and is used for basic knowledge retrieval scenarios.

## 🔍 Sample Output

[INFO] Uploading document...
[INFO] Splitting into chunks...
[INFO] Generating embeddings...
[INFO] Stored in vector index

[QUERY] Explain RAG
[Retriever] Top 3 documents retrieved
[Generator] Answer generated successfully
