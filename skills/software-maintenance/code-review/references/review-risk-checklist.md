# Code Review Risk Checklist

Select the dimensions relevant to the diff. A checklist prompt is not a finding unless evidence shows a defect or risk.

## Correctness
- [ ] Does the code satisfy the stated requirement and preserve existing behavior?
- [ ] Are null, empty, invalid, and boundary values handled?
- [ ] Are state transitions and invariants preserved?
- [ ] Are timezones, precision, locale, and encoding handled correctly?
- [ ] Are error paths, cancellation, cleanup, and partial failures correct?
- [ ] Are concurrency, shared state, ordering, and race conditions considered?

## Architecture and compatibility
- [ ] Does the change follow established responsibility boundaries?
- [ ] Are interfaces, schemas, public APIs, and serialized formats compatible?
- [ ] Are callers and consumers updated where necessary?
- [ ] Are dependencies justified and compatible?
- [ ] Is configuration / migration behavior safe for mixed versions?
- [ ] Does the change add accidental complexity?

## Security and data
- [ ] Inputs are validated server-side and canonicalized where needed.
- [ ] Authorization is checked for function, object, tenant, and property access.
- [ ] Queries use safe parameterization / ORM mechanisms.
- [ ] Output encoding matches the context.
- [ ] File paths, uploads, redirects, and deserialization are constrained.
- [ ] Secrets are not committed, logged, or returned.
- [ ] Sensitive data is minimized and correctly protected.
- [ ] Errors do not leak stack traces or internal details.
- [ ] Dependencies and build scripts are assessed for supply-chain impact.

## Tests and operations
- [ ] Tests cover new behavior and meaningful failure paths.
- [ ] Assertions would fail when the relevant behavior is broken.
- [ ] Test data and mocks match the real contract.
- [ ] Flaky timing, shared state, and external service dependence are controlled.
- [ ] Logging / metrics / tracing provide useful evidence without private data.
- [ ] Deployment / migration / rollback implications are considered.
- [ ] Relevant docs / runbooks / changelog are updated.

## Review discipline
- Inspect changed lines and enough context to understand their effects.
- Prefer a concrete defect over a subjective preference.
- Explain the exact trigger and consequence.
- Avoid duplicating findings for one root cause.
- Credit clear design or testing work when useful.
- A clean review means no actionable findings in scope, not proof of defect-free software.
