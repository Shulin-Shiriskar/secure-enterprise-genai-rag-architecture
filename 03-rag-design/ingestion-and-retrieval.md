# Ingestion and retrieval

## Prototype flow

1. Place approved `.txt` files in `06-implementation/sample_docs/`.
2. Run `python scripts/ingest.py`.
3. The script splits text into overlapping word chunks and builds a local SQLite FTS5 index.
4. The API searches the index and returns up to three passages with file names and chunk identifiers.
5. The answer service either quotes the highest-ranked passage or asks Azure OpenAI to summarise the retrieved evidence.

## Why this is only a baseline

Full-text search works well for exact terms but is weak at semantic matching. The target Azure design should use Azure AI Search with hybrid retrieval, document metadata, access filters, index versioning and measured ranking quality. The index should be rebuilt or updated when documents change or are revoked.

## Evaluation plan

Build a reviewed question set with expected documents and known unanswerable questions. Track retrieval recall@k, groundedness, citation accuracy, refusal behaviour, latency and cost. Include prompt-injection and unauthorised-access tests before any production release.
