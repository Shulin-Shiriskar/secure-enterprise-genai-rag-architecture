# Governance and approval approach

The fictional use case is a read-only internal document assistant. A provisional **Tier 2 (Limited)** classification may be reasonable for approved low-sensitivity documents with no automated actions. This is an illustration, **not** a classification that applies to every RAG solution.

The tier may increase if the assistant processes sensitive employee or customer information, influences safety-critical decisions, performs actions, or reaches a wider audience. The actual classification must follow the criteria and approval authorities defined in the [Enterprise AI Governance Framework](https://github.com/Shulin-Shiriskar/enterprise-ai-governance-framework).

## Required gates

| Gate | Evidence |
|---|---|
| Use-case registration | Owner, purpose, users, data classes |
| Risk classification | Scored rationale and escalation triggers |
| Architecture review | Logical design, integration and threat boundaries |
| Security/privacy review | Identity, data access, retention and supplier assessment |
| Pilot approval | Test results, accepted risks and rollback plan |
| Go-live approval | Control evidence and accountable sign-off |
| Ongoing review | Monitoring, incidents and material-change reassessment |

A portfolio demonstration does not replace these approvals.
