# Production gap register

The following controls are **not delivered** by the initial prototype. They are tracked here so the project does not imply a higher assurance level than the code provides.

| ID | Gap | Priority | Closure evidence |
|---|---|---|---|
| SEC-01 | No validated user authentication | Critical | Entra ID integration and token validation tests |
| SEC-02 | No document-level authorisation | Critical | ACL-filtered retrieval and cross-user negative tests |
| SEC-03 | No private endpoints or restricted egress | High | Network design, IaC and connectivity tests |
| SEC-04 | No managed identity for model/search access | High | Role assignments and removal of runtime keys |
| SEC-05 | No production ingestion approval workflow | High | Owner approval, malware scan and classification checks |
| SEC-06 | No enterprise audit trail | High | Central logs, retention and access controls |
| SEC-07 | No prompt-injection regression suite | High | Adversarial corpus and measured results |
| SEC-08 | No rate limits or per-user quotas | High | Load tests and gateway policies |
| SEC-09 | No backup, DR or deletion propagation | High | Recovery and deletion test evidence |
| SEC-10 | No automated dependency/image scanning | Medium | CI findings and remediation policy |
| SEC-11 | No independent security review | High | Signed review and go-live approval |

The Terraform starter is a **hosting scaffold**, not evidence of closure for these gaps.
