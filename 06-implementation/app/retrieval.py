"""Small lexical search adapter for the portfolio prototype."""
import re
import sqlite3
from pathlib import Path


def open_db(db_path: str) -> sqlite3.Connection:
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    return db


def create_index(db_path: str) -> None:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    with open_db(db_path) as db:
        db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(source, chunk_id UNINDEXED, content)")


def search(db_path: str, question: str, limit: int = 3) -> list[dict]:
    tokens = re.findall(r"[a-zA-Z0-9]{2,}", question.lower())
    if not tokens or not Path(db_path).exists():
        return []
    # Tokens are quoted, rather than passed through as raw FTS syntax.
    query = " OR ".join('"' + token + '"' for token in tokens[:12])
    with open_db(db_path) as db:
        rows = db.execute(
            "SELECT source, chunk_id, content FROM chunks WHERE chunks MATCH ? ORDER BY bm25(chunks) LIMIT ?",
            (query, limit),
        ).fetchall()
    return [dict(row) for row in rows]
