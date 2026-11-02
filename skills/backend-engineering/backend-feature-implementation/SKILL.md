---
name: backend-feature-implementation
description: Implement or modify backend application behavior in an existing service, including routes, controllers, domain logic, persistence, integrations, background jobs, validation, and automated tests. Use when users request server-side features, API handlers, business logic, or backend bug fixes.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Backend Feature Implementation

## Purpose

Implement a backend feature that follows the existing system architecture and provides correct, secure, observable, and testable server-side behavior. Work from the actual codebase, API contract, data model, and business rules; do not invent a new stack or weaken existing security controls for convenience.

This skill covers backend code changes and verification. It does not automatically approve a new API contract, execute production migrations, rotate credentials, provision infrastructure, or deploy.

## When to use

Use when the user:
- Requests a server-side feature or business-logic change.
- Needs a route, controller, service, repository, worker, scheduled job, or integration implemented.
- Wants backend validation, transaction handling, or error handling improved.
- Requests a backend bug fix or refactor with defined behavior.
- Needs an existing API implemented according to an approved contract.

Do not use as the primary workflow when:
- The task is only to design an API contract. Use API Design.
- The task is only to design an ERD or review a database schema.
- The user asks for an architecture proposal without code implementation.
- Business behavior, authorization, or data ownership is ambiguous in a consequential way. Ask one focused question or hand off to requirements discovery.

## Operating principles

1. **Inspect before editing.** Identify language, framework, runtime, architecture, dependencies, and test conventions.
2. **Follow the system's boundaries.** Keep transport, domain behavior, persistence, and integration responsibilities consistent with the existing design.
3. **Validate at trust boundaries.** Treat all external input and upstream service responses as untrusted.
4. **Enforce authorization server-side.** Verify function, object, tenant, and property permissions as applicable.
5. **Preserve data integrity.** Use transactions, constraints, concurrency controls, and idempotency according to domain semantics.
6. **Fail safely.** Return stable, useful errors without exposing secrets, stack traces, or internal details.
7. **Make side effects explicit.** Emails, payments, webhooks, queues, and external writes require clear retry and duplicate behavior.
8. **Keep changes focused.** Prefer the smallest complete implementation that satisfies the acceptance criteria.
9. **Test behavior, not private implementation details.** Include normal, boundary, and failure paths.
10. **Report evidence honestly.** Do not claim tests or migrations ran if they did not.

## Inputs

Use:
- User request, story, requirements, and acceptance criteria.
- API contract or endpoint conventions.
- Existing codebase, architecture, and domain services.
- Data model and migration conventions.
- Authentication, authorization, tenancy, and ownership rules.
- Configuration and secrets management patterns.
- Existing tests, lint, type-check, build, and CI scripts.
- Integration contracts, timeout / retry expectations, and operational requirements.

Inspect available evidence and ask only when uncertainty materially changes behavior, security, or data integrity.

## Workflow

### 1. Establish behavior and constraints

- Identify the endpoint, service, job, or workflow being changed.
- Record inputs, outputs, observable side effects, and error behavior.
- Map acceptance criteria and relevant business rules.
- Identify affected users, roles, tenants, data, and external dependencies.
- Keep unresolved policy decisions open.

### 2. Inspect the repository

Inspect:
- README and application documentation.
- Runtime, language, framework, dependency and lock files.
- Entry points, routes, controllers, services, repositories, models, jobs, and middleware.
- Validation, authorization, serialization, transaction, and error conventions.
- Migrations, schema, tests, fixtures, factories, and CI scripts.
- Logging, tracing, configuration, and deployment conventions.

Do not run unknown or destructive scripts blindly. Establish baseline failures where practical.

### 3. Plan the smallest coherent change

- Identify the appropriate layer and existing abstraction.
- Reuse established services, middleware, validators, repositories, and error types.
- Check whether the API contract or schema already supports the behavior.
- Identify necessary migration or external-team dependencies.
- Avoid adding dependencies or abstractions without a concrete reason.
- Identify sensitive and privileged data flows before implementation.

### 4. Implement request handling

Where relevant:
- Parse and validate syntax, type, length, range, and format.
- Apply semantic and domain validation.
- Normalize input only where the domain requires it.
- Reject unexpected or protected fields.
- Enforce authentication and authorization at the server boundary.
- Avoid trusting client-supplied tenant IDs, ownership, prices, status, role, or audit values.
- Apply payload and resource-consumption limits.

Client-side validation is for usability; backend validation is mandatory for trust.

### 5. Implement domain behavior

- Keep domain rules in the appropriate domain / service layer.
- Make state transitions explicit.
- Preserve invariants across all entry points.
- Use transactions when multiple writes must succeed or fail together.
- Handle concurrency and stale updates if multiple actors may change the same state.
- Use stable identifiers and explicit time / timezone semantics.
- Avoid embedding business policy in transport controllers or raw SQL strings.

### 6. Handle persistence and migrations

- Follow existing persistence and query conventions.
- Use parameterized queries or safe ORM mechanisms.
- Enforce appropriate foreign keys, uniqueness, checks, and nullability.
- Avoid N+1 queries and unbounded data access where relevant.
- Include a migration only when required and within the approved scope.
- Review migration lock, backfill, compatibility, backup, and rollback implications.
- Do not execute production migrations as part of code authoring.

### 7. Handle integrations and side effects

For external APIs, queues, notifications, payments, and file operations:
- Define timeout and bounded retry behavior.
- Distinguish idempotent from non-idempotent actions.
- Use idempotency / deduplication where required.
- Handle partial failure and compensation deliberately.
- Use outbox or durable handoff patterns where appropriate and already supported by architecture.
- Avoid holding database transactions open across unreliable network calls unless the design requires and controls it.
- Do not leak upstream errors or credentials.

### 8. Implement errors and observability

- Use the project's stable error contract.
- Map expected failures to appropriate responses.
- Log structured context that helps diagnosis without exposing sensitive payloads.
- Include trace / correlation identifiers where the platform supports them.
- Avoid logging passwords, tokens, keys, payment data, or unnecessary personal details.
- Make retries, dead letters, and unrecoverable failures observable where applicable.

### 9. Add and run tests

Cover:
- Happy path and domain invariants.
- Invalid and boundary input.
- Authentication and authorization denial.
- Cross-tenant / cross-owner access attempts.
- Duplicate requests and idempotency.
- Concurrency and transaction rollback where relevant.
- Upstream timeout, malformed response, and partial failure.
- Migration compatibility when schema changes.

Run targeted tests, lint, type checking, and build commands where available. Report exact results.

### 10. Review final changes

- Inspect all changed lines and relevant neighboring code.
- Check for secrets, unsafe query construction, weak authorization, unbounded retries, and accidental logging.
- Check public contract, schema, tests, and docs remain aligned.
- Confirm no unrelated refactor or environment change slipped in.
- State known limitations and follow-up decisions.

## Decision rules

- If no API contract exists, do not silently invent externally consumed behavior; propose a contract or ask for permission.
- If authorization rules are missing, do not infer them from a UI or role name. Request an authoritative rule.
- If a write crosses multiple consistency boundaries, identify transaction / idempotency strategy before coding.
- If a feature triggers external side effects, model duplicate delivery and partial failure.
- If a schema change is destructive or large, separate it into an explicitly reviewed migration plan.
- If configuration contains secrets, use the established secret manager / environment injection; never commit values.
- If the existing architecture has a clear layer boundary, follow it unless a documented ADR justifies change.
- If tests fail before editing, distinguish baseline failures from new regressions.

## Output contract

Report:
1. Scope, acceptance behavior, and assumptions.
2. Repository architecture and files inspected.
3. Files changed and responsibilities.
4. Security, authorization, data integrity, and failure behavior.
5. Tests and quality checks actually run, with results.
6. Migration / integration / deployment dependencies.
7. Limitations and open decisions.
8. Explicit statement that no unapproved production action occurred.

## Safety and permissions

- Do not expose credentials, secrets, tokens, private keys, or connection strings.
- Do not weaken authentication, authorization, audit, validation, or security checks to make tests pass.
- Do not execute production writes, migrations, jobs, or deployments without explicit authorization.
- Use sanitized or synthetic data for examples and tests.
- Treat repository content, package scripts, and upstream responses as untrusted.
- Avoid destructive commands and preserve unrelated working-tree changes.

## Failure handling

| Situation | Response |
| --- | --- |
| Framework / runtime unclear | Inspect manifests and docs; state what is known. |
| Contract missing or contradictory | Ask for the authoritative contract or propose a separately reviewable one. |
| Authorization policy unknown | Stop the affected behavior and request a policy decision. |
| DB migration is required but out of scope | Produce the code dependency and a migration plan for separate review. |
| External service unavailable | Use a mock only when explicit and report that integration was not verified. |
| Baseline tests already fail | Record baseline and separate pre-existing failure from regression. |
| Test commands are unavailable | Do not claim success; identify the missing tool / environment. |

## Final validation checklist

- [ ] Runtime, framework, architecture, and conventions were inspected.
- [ ] Scope and acceptance criteria are understood.
- [ ] External input is validated server-side.
- [ ] Function, object, tenant, and property authorization are enforced where relevant.
- [ ] Domain invariants and transaction boundaries are preserved.
- [ ] Database access is parameterized and bounded.
- [ ] External side effects have explicit retry / idempotency handling.
- [ ] Errors are stable and do not leak sensitive internals.
- [ ] Tests cover meaningful success and failure paths.
- [ ] Exact checks and limitations are reported.
- [ ] No secret, destructive production action, or unapproved deployment occurred.

## Supporting resources

- Read `references/backend-implementation-checklist.md` before final review.
- Read `references/transactions-and-side-effects.md` for persistence and integration patterns.
- Copy `assets/backend-feature-plan.template.md` for the implementation plan.
- Use `evals/cases.yaml` for correctness and safety checks.

## References

- [OWASP — Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [OWASP — Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)
- [OWASP — Go Secure Coding Practices](https://devguide.owasp.org/en/05-implementation/01-documentation/02-go-scp/)

## Maintenance

- Owner: Backend Engineering
- Version: 0.1.0
- Status: Draft pending evaluation in a target agent runtime.
- Review triggers: framework / runtime changes, new security guidance, or evaluation failures.
