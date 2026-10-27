# Cost and release considerations

## Cost drivers

Azure Container Apps hosting, Log Analytics ingestion, Azure OpenAI tokens, Azure AI Search capacity, private networking and storage all contribute to cost. The Terraform starter does not provide a full cost estimate; check current Azure pricing in the target region before provisioning.

## Release checklist

- [ ] Confirm sample data only in the prototype.
- [ ] Run automated tests and review dependency findings.
- [ ] Review architecture decisions and the production gap register.
- [ ] Configure billing alerts and a resource owner.
- [ ] Verify container image provenance.
- [ ] Obtain approval before any external exposure or real-data ingestion.
- [ ] Document rollback and resource teardown.

For a public portfolio, screenshots, architecture documents and test evidence are preferable to leaving a billable demo environment running.
