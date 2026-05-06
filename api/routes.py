from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/ask")
def ask(q: str):
    start = time.time()

    # 模拟检索过程
    retrieved_docs = [
        "RAG improves LLM responses by retrieving external knowledge.",
        "It combines search and generation.",
        "Commonly used in enterprise QA systems."
    ]

    # 模拟生成
    answer = f"Based on retrieved context: {retrieved_docs[0]}"

    latency = round(time.time() - start, 3)

    return {
        "query": q,
        "answer": answer,
        "latency": f"{latency}s",
        "docs_used": len(retrieved_docs)
    }
