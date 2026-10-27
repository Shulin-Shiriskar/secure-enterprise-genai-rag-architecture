"""Demo API. No authentication: sample documents only, local use recommended."""
import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from .retrieval import search
from .answering import extractive_answer, azure_answer

logger = logging.getLogger(__name__)
app = FastAPI(title="Enterprise Document Assistant — Prototype", version="0.1.0")


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)


class Source(BaseModel):
    source: str
    chunk_id: str
    content: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]
    mode: str


@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}


@app.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    db_path = os.getenv("RAG_DB_PATH", "./rag.db")
    try:
        passages = search(db_path, request.question)
    except Exception:
        logger.exception("Retrieval failed")
        raise HTTPException(status_code=503, detail="Retrieval service unavailable")
    mode = os.getenv("ANSWER_MODE", "extractive").lower()
    if mode == "extractive":
        answer = extractive_answer(passages)
    elif mode == "azure":
        try:
            answer = await azure_answer(request.question, passages)
        except Exception:
            logger.exception("Model request failed")
            raise HTTPException(status_code=502, detail="Model service unavailable")
    else:
        raise HTTPException(status_code=500, detail="Invalid answer mode configuration")
    return AskResponse(answer=answer, sources=[Source(**p) for p in passages], mode=mode)
