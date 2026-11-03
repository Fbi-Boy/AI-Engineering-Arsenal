# Memory Governance and Data Lifecycle

## Memory record provenance
A memory item should carry, where applicable:
- Owner and scope (user / project / tenant).
- Content category and purpose.
- Source and timestamp.
- Confidence / verification state.
- Sensitivity classification.
- Consent or policy basis.
- Created / last-confirmed / expiry time.
- Correction, export, and deletion reference.

Avoid storing inferred preferences or identity facts as confirmed user statements.

## Purpose limitation
Store the least information necessary for a defined use. Prefer short-lived task context to indefinite persistence when the value is only needed for one workflow. Frequently changing facts should be read from the authoritative source.

## Lifecycle actions
For each category define:
- Retention and expiry.
- User correction and review.
- Export and portability.
- Deletion and revocation.
- Backup lifecycle and restore behavior.
- Cache / index / derived summary invalidation.
- Audit retention and legal hold ownership.

A deletion response must distinguish the primary record from replicas, caches, search indexes, logs, backups, and external processors. Do not claim deletion is complete until the defined lifecycle is satisfied.

## Access control
Enforce scope at read and write time, not only in a UI. Re-check access for background jobs and shared artifacts. Apply the same policy to embeddings, summaries, and cached copies. Never use memory as an authority source for a permission check.

## Sensitive content
Do not store secrets, tokens, passwords, session cookies, or private keys. Do not infer sensitive traits. Redact personal / customer content from telemetry and test fixtures.
