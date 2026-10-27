# Terraform hosting scaffold

This module provisions a minimal Azure Container Apps environment and demo app. It deliberately disables external ingress because the app has no authentication.

It does **not** provision a production RAG architecture, Azure OpenAI, Azure AI Search, private networking, registry authentication or secure secret management. Review the [deployment guide](../DEPLOYMENT.md) and [production gaps](../../02-security/production-gap-register.md).

Terraform AzureRM v4 requires `subscription_id`. Pass it with `-var`, a `.tfvars` file or `TF_VAR_subscription_id`.
