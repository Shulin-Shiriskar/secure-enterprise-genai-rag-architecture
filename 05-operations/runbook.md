# Operations runbook

## Local startup

From `06-implementation/`, run ingestion and then start the FastAPI service. `GET /health` confirms that the application process is responding; it does not prove Azure dependencies are healthy.

## Troubleshooting

- **No sources found:** confirm ingestion ran and the question shares terms with the sample documents.
- **SQLite FTS unavailable:** use a Python build with SQLite FTS5 enabled.
- **Azure model request fails:** confirm endpoint, deployment, API version, key and network access. Do not print secrets when debugging.
- **Responses are not grounded:** return to extractive mode and inspect the retrieved evidence; do not rely on a generated answer without verification.

## Monitoring plan

Track request count, latency, retrieval hit rate, refusal rate, upstream model failures and token usage. Avoid logging full prompts or retrieved document contents by default. Establish alert thresholds from pilot measurements.

## Incident response

For suspected leakage or unauthorised retrieval, disable model generation and public access, preserve relevant metadata logs, rotate exposed credentials, notify the incident owner and assess data exposure. Re-enable only after review and control testing.
