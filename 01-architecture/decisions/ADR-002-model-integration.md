# ADR-002: Make model generation optional

**Status:** Accepted

## Decision

Use extractive answers by default. Allow Azure OpenAI generation only when the operator explicitly selects `ANSWER_MODE=azure` and provides deployment settings.

## Rationale

This keeps the demo reproducible, avoids unexpected costs and makes the retrieval evidence visible even when model access is unavailable.

## Trade-offs

Extractive answers are less natural. Model-generated answers can be easier to read but require grounding tests, token budgets, content safety checks and operational monitoring.
