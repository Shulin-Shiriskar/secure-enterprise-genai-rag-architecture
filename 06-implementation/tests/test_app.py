import os
import sqlite3
from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app
from app.retrieval import search
from scripts.ingest import chunk_words


def test_chunking():
    assert chunk_words("one two three", size=2, overlap=1) == ["one two", "two three", "three"]


def test_retrieval_and_api(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    with sqlite3.connect(db_path) as db:
        db.execute("CREATE VIRTUAL TABLE chunks USING fts5(source, chunk_id UNINDEXED, content)")
        db.execute("INSERT INTO chunks VALUES (?, ?, ?)", ("policy.txt", "1", "High-risk AI requires Governance Committee approval."))
    monkeypatch.setenv("RAG_DB_PATH", str(db_path))
    monkeypatch.setenv("ANSWER_MODE", "extractive")
    client = TestClient(app)
    response = client.post("/ask", json={"question": "Who approves high-risk AI?"})
    assert response.status_code == 200
    body = response.json()
    assert body["sources"][0]["source"] == "policy.txt"
    assert "Governance" in body["answer"]


def test_empty_evidence(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    with sqlite3.connect(db_path) as db:
        db.execute("CREATE VIRTUAL TABLE chunks USING fts5(source, chunk_id UNINDEXED, content)")
    monkeypatch.setenv("RAG_DB_PATH", str(db_path))
    monkeypatch.setenv("ANSWER_MODE", "extractive")
    client = TestClient(app)
    response = client.post("/ask", json={"question": "Unknown subject"})
    assert response.status_code == 200
    assert response.json()["sources"] == []


def test_validation():
    response = TestClient(app).post("/ask", json={"question": "a"})
    assert response.status_code == 422
