"""Index fictional sample documents. Replaces the existing local index."""
import os
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "sample_docs"
DB = Path(os.getenv("RAG_DB_PATH", str(ROOT / "rag.db")))


def chunk_words(text: str, size: int = 110, overlap: int = 20) -> list[str]:
    words = text.split()
    if not words:
        return []
    step = size - overlap
    return [" ".join(words[i:i + size]) for i in range(0, len(words), step)]


def main():
    DB.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB) as db:
        db.execute("DROP TABLE IF EXISTS chunks")
        db.execute("CREATE VIRTUAL TABLE chunks USING fts5(source, chunk_id UNINDEXED, content)")
        total = 0
        for path in sorted(DOCS.glob("*.txt")):
            for number, chunk in enumerate(chunk_words(path.read_text(encoding="utf-8")), 1):
                db.execute("INSERT INTO chunks(source, chunk_id, content) VALUES (?, ?, ?)", (path.name, str(number), chunk))
                total += 1
    print(f"Indexed {total} chunks from {len(list(DOCS.glob('*.txt')))} fictional sample files into {DB}")


if __name__ == "__main__":
    main()
