# Solution overview

## Business context

A fictional Australian transport operator wants staff to find answers in approved internal policies and technical guidance without sending entire document libraries to a model. The first use case is a read-only assistant for low-sensitivity documents.

## In scope

- Controlled ingestion of a small document set.
- Keyword retrieval with source references in the prototype.
- Optional answer generation using an existing Azure OpenAI deployment.
- A hosting baseline and a clear route to enterprise controls.

## Out of scope for v0.1

- Production identity and access management.
- Document-level permission trimming.
- Azure AI Search and vector embeddings.
- Automated document lifecycle and deletion propagation.
- High availability, disaster recovery and production SLAs.

## Target request flow

1. A user authenticates through enterprise identity (future production requirement).
2. The API verifies the user's claims and authorisation (not implemented in v0.1).
3. The retrieval layer returns only documents the user can access (not implemented in v0.1).
4. Retrieved content is treated as untrusted evidence.
5. The answer service generates a grounded response or says the evidence is insufficient.
6. Security-relevant events are logged without unnecessary document contents.

## Key quality attributes

| Attribute | Target approach | v0.1 status |
|---|---|---|
| Confidentiality | Private network and authorised retrieval | Not implemented |
| Integrity | Versioned ingestion, source attribution | Partial |
| Availability | Health checks, scaling and DR | Basic health check only |
| Observability | Request metrics, model and retrieval telemetry | Basic application logs |
| Explainability | Source references and clear limitations | Implemented |
| Cost control | Usage quotas, token limits and budgets | Basic response limits |

See [decision records](decisions/) and [security gaps](../02-security/production-gap-register.md).
