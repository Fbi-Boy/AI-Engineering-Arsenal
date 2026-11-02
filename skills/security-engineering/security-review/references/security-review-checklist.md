# Security Review Checklist

Use only the sections relevant to the declared architecture and threat model.

## Scope and trust boundaries
- Identify public and internal entry points, tenant boundaries, sensitive assets, and privileged operations.
- Identify data sources, transformations, storage locations, exports, and external recipients.
- Mark third-party content, files, webhooks, and API responses as untrusted.

## Identity and authorization
- Authentication required on protected routes and jobs.
- Session / token lifecycle, expiry, revocation, secure storage, and transport.
- Function-level, object-level, tenant-level, and property-level authorization.
- Privilege escalation, role assignment, admin impersonation, and account recovery.
- Authorization enforced at the server / service boundary, not only in the UI.

## Input and output
- Allowlist or schema-based validation with type, length, range, and semantic limits.
- Parameterized database access and safe query construction.
- Output encoding for the relevant rendering context.
- File upload type, size, storage, path, and content handling.
- SSRF, open redirects, path traversal, unsafe deserialization, injection, and resource consumption where relevant.

## Data protection
- Data minimization and classification.
- Encryption in transit and established cryptographic libraries.
- Key management and rotation ownership.
- Secret handling in source, logs, CI, artifacts, and environment.
- Retention, deletion, export, audit, and backup exposure.

## Application behavior
- State transition and business logic abuse.
- Rate limiting and abuse protection.
- Replay, duplicate, race, and idempotency concerns.
- Safe error messages and no stack / secret leakage.
- Secure defaults and fail-closed behavior where appropriate.

## Dependencies and delivery
- Direct and transitive dependency inventory.
- Lockfile integrity and known vulnerability review.
- Maintainer / source trust and package name confusion risk.
- Build and workflow token permissions.
- Third-party action / plugin provenance and pinning policy.
- Artifact integrity, signing / attestation, and release provenance where in scope.

## Evidence discipline
- Record the exact file / symbol / line or configuration path.
- Trace a realistic attack path and state preconditions.
- Separate observed code from runtime assumptions.
- Do not claim a control exists solely because a library is present.
