# ADR-001: Use local full-text search for the first executable baseline

**Status:** Accepted for prototype only

## Context

A portfolio prototype should run without cloud spend or a subscription. Azure AI Search is the preferred target for enterprise retrieval, but introduces resource provisioning and credential requirements before the basic application flow can be tested.

## Decision

Use SQLite FTS5 for the initial executable version. Keep retrieval behind a small function boundary and document the migration path to Azure AI Search.

## Consequences

- The prototype is easy to run and test offline.
- Search is lexical, not semantic. Synonyms and paraphrases may perform poorly.
- Permission trimming, vector retrieval, index lifecycle and distributed scaling are not provided.
- Replacing the retrieval layer is required before production adoption.
