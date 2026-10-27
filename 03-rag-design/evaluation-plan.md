# Evaluation plan

The initial test suite checks request validation, retrieval, refusal when there is no matching evidence, and response attribution. It does not measure model quality or production security.

## Suggested acceptance criteria for a later pilot

| Measure | Proposed gate | Notes |
|---|---|---|
| Retrieval recall@3 | At least 90% | Against a reviewed representative dataset |
| Citation correctness | At least 95% | Human-labelled evaluation |
| Unsupported claims | Less than 2% | Requires a defined scoring rubric |
| Access-control violations | Zero | Must include adversarial cross-user tests |
| Prompt-injection success | Zero in agreed test suite | Reassess as threats evolve |
| p95 latency | Agree with service owner | Depends on model and corpus |

These are **proposed pilot targets**, not achieved results.
