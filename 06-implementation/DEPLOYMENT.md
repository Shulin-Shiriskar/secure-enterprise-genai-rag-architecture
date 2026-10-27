# Deployment guide

## Local

Follow the root README. This is the supported starting point and does not require cloud resources.

## Container

```bash
cd 06-implementation
docker build -t enterprise-rag-demo:0.1 .
docker run --rm -p 8000:8000 enterprise-rag-demo:0.1
```

The container includes only fictional sample documents and uses extractive mode. The local SQLite index is baked into the image and should not be used as a shared production data store.

## Azure Container Apps hosting scaffold

The `infra/` directory contains Terraform to create a resource group, Log Analytics workspace, Container Apps environment and a Container App. It assumes you have already built and published a container image that Azure can pull. A public image is simplest for a demo; a private registry requires separate registry authentication configuration.

```bash
cd 06-implementation/infra
terraform init
terraform plan -var='image=YOUR_PUBLIC_IMAGE:TAG'
terraform apply -var='image=YOUR_PUBLIC_IMAGE:TAG'
```

**Important:** The scaffold defaults to external ingress **disabled**. That is intentional: the prototype has no authentication. Do not enable external ingress for an unprotected API. Use a secured ingress and identity design before exposing it.

This deployment does not create Azure OpenAI or Azure AI Search, configure managed identities, private endpoints, per-document access control or secure a production environment. Review the [gap register](../02-security/production-gap-register.md).

## Azure OpenAI optional mode

Create or obtain an approved Azure OpenAI deployment separately. Set the following at runtime (never commit secrets):

- `ANSWER_MODE=azure`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_OPENAI_API_KEY`

The example client uses an API key for demonstration. For production, replace it with Entra ID authentication and managed identity, with approved network restrictions and model configuration.

## Teardown

```bash
terraform destroy -var='image=YOUR_PUBLIC_IMAGE:TAG'
```

Cloud resources may incur charges while deployed.
