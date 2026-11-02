# API Security and Reliability Design Notes

## Authentication is not authorization

Authentication establishes a caller identity or credential context. Authorization decides whether that caller may perform a particular operation on a particular object and property.

Review:
- Object-level access: can this caller access this resource instance?
- Function-level access: can this caller invoke this operation?
- Property-level access: can this caller read or write this field?
- Tenant-level access: is the resource inside the caller's authorized tenant?
- Administrative operations: are privileged paths separately controlled and audited?

Do not infer permissions from a frontend control, an opaque identifier, or a successful login.

## Input and output controls

- Validate type, size, range, format, and domain rules server-side.
- Reject unknown or protected writable properties unless an explicit extension contract exists.
- Map request models to domain commands deliberately.
- Return only fields the caller is authorized to read.
- Avoid exposing stack traces, SQL errors, internal URLs, credentials, or raw dependency exceptions.

## Resource consumption

Apply controls proportionate to the risk:
- Maximum request and upload sizes.
- Bounded pagination.
- Query and sort allowlists.
- Per-user / per-tenant rate limits.
- Timeouts and bounded retries.
- Concurrency and expensive-operation limits.
- Abuse controls for sensitive business workflows.

## Idempotency and retries

For retryable write requests, define:
- The idempotency key format and scope.
- How long deduplication records are retained.
- Whether the same key with a different payload is rejected.
- How duplicate requests return the original result.
- How the system handles a failure after side effects but before response delivery.

Do not assume every POST can be safely retried. Do not add retry loops without backoff, limits, and operation-specific semantics.

## Concurrency and consistency

When concurrent writes matter, document:
- Version / ETag or equivalent concurrency token.
- Conditional update behavior.
- Conflict response.
- Whether last-write-wins is acceptable.
- Transaction or eventual consistency guarantees.

## Security review baseline

The OWASP API Security Top 10 includes risks such as broken object-level authorization, broken authentication, broken object property-level authorization, unrestricted resource consumption, and broken function-level authorization. Use it as a review prompt, not a substitute for a threat model or security testing.

## Sources

- [OWASP API Security Top 10](https://owasp.org/API-Security/)
- [Microsoft — API implementation best practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-implementation)
- [OpenAPI security schemes](https://spec.openapis.org/oas/v3.2.1.html#security-scheme-object)
