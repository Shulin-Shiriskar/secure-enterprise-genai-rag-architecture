# Security design notes

## Identity

Use Microsoft Entra ID for workforce sign-in. Validate token issuer, audience, expiry and signatures at the API boundary. Authorisation must use trusted claims, not client-supplied headers.

## Retrieval permissions

Carry document ownership, classification and access-control metadata into the search index. Filter results using the validated user's entitlements before constructing a model prompt. Test with users who have overlapping and disjoint access.

## Network

The target Azure design uses private endpoints where supported, controlled egress, DNS resolution for private services and restricted administrative access. These controls are not part of the current Terraform starter.

## Secrets

Prefer managed identities and least-privilege roles. If a temporary API key is used for a prototype, supply it through runtime configuration and never commit it or store it in Terraform state.

## Data handling

Define allowed classifications, retention, deletion propagation, geographic processing requirements and approved model deployments before ingesting operational data.
