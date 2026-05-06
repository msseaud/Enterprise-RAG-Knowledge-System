from fastapi import APIRouter

router = APIRouter()

@router.get("/ask")
def ask(q: str):
    return {"answer": f"You asked: {q}"}
