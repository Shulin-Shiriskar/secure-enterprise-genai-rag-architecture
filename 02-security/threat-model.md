# Threat model

## Assets and boundaries

Assets include approved documents, search indexes, user identities, prompts, model responses, API credentials and audit events. The principal trust boundaries are user-to-API, document-to-retrieval, retrieval-to-model and app-to-cloud services.

| Threat | Example | Required mitigation | v0.1 |
|---|---|---|---|
| Unauthorised document access | User retrieves restricted material | Validated identity, ACL-aware retrieval, negative tests | Missing |
| Prompt injection | Retrieved page says to ignore system instructions | Treat retrieved text as data, isolate instructions, adversarial tests | Partial |
| Data exfiltration | Sensitive passages sent to wrong service | Classification gates, approved endpoints, egress restrictions | Missing |
| Secret exposure | API key committed to repository | Managed identity, Key Vault, secret scanning | Partial (env only) |
| Index poisoning | Unapproved document added to corpus | Ingestion approvals, provenance, versioning | Missing |
| Denial of service | Repeated expensive requests | Authentication, rate limiting, quotas and autoscaling | Missing |
| Hallucinated answers | Confident response without evidence | Citations, refusal on insufficient evidence, evaluations | Partial |
| Sensitive logging | Prompts or documents stored in logs | Log minimisation, access control, retention policy | Partial |

## Prompt injection handling

The application places retrieved content in a clearly marked evidence section and instructs the model not to follow commands inside that section. This is **not a complete defence**. The production design also needs retrieval authorisation, content screening, evaluation against malicious documents and monitoring.

## Security review gate

Do not expose the demo publicly or load enterprise documents until the critical items in the [gap register](production-gap-register.md) have been closed and independently tested.
