# Backend Implementation Quality Checklist

## Scope and architecture
- [ ] Feature behavior and acceptance criteria are clear.
- [ ] Runtime, framework, dependency, and module boundaries are inspected.
- [ ] Existing route / controller / service / repository patterns are reused.
- [ ] API and database contracts are aligned.
- [ ] Scope excludes unrelated refactors.

## Input and authorization
- [ ] External input is validated for syntax and domain semantics.
- [ ] Unknown and protected fields are rejected or handled explicitly.
- [ ] Authentication is distinct from authorization.
- [ ] Function-level permissions are enforced.
- [ ] Object ownership and tenant boundaries are checked.
- [ ] Privileged property changes are protected server-side.

## Domain and persistence
- [ ] Business invariants are enforced in a shared domain boundary.
- [ ] Transaction scope matches data consistency requirements.
- [ ] Concurrent updates and stale writes are considered.
- [ ] Queries are parameterized and appropriately bounded.
- [ ] PK, FK, uniqueness, and other integrity constraints are respected.
- [ ] Migrations are compatible and separately reviewed where required.

## Integrations and side effects
- [ ] Timeouts and retry limits are explicit.
- [ ] Non-idempotent operations are protected against unsafe duplicate execution.
- [ ] Partial failure and compensation are considered.
- [ ] Network calls do not create uncontrolled transaction locks.
- [ ] Queue / worker acknowledgement is distinguished from completion.
- [ ] External errors and payloads are treated as untrusted.

## Errors and observability
- [ ] Error responses follow a stable contract.
- [ ] Sensitive details are not returned to callers.
- [ ] Logs include useful context without secrets or unnecessary personal data.
- [ ] Correlation / trace IDs are propagated where supported.
- [ ] Failure, retry, and dead-letter conditions are observable.

## Tests and delivery
- [ ] Happy path and domain rules are covered.
- [ ] Invalid, boundary, and authorization cases are covered.
- [ ] Transaction rollback / duplicate / concurrency paths are tested where relevant.
- [ ] External failures and retries are tested.
- [ ] Relevant lint, type, test, and build commands were run.
- [ ] Migration / deployment actions are identified but not executed without permission.
