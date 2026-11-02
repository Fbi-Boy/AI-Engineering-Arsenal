---
name: backend-testing
description: Design and implement automated tests for backend services, APIs, authorization, persistence, integrations, jobs, transactions, and data integrity. Use when verifying server-side behavior in an existing application.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Backend Testing

## Purpose
Verify server-side behavior at service, API, persistence, contract, and integration boundaries. Tests must protect business invariants, data integrity, access control, error behavior, and safe interaction with external dependencies.

## When to use
Use when the user requests tests for:
- HTTP endpoints, service layers, domain logic, repositories, or background workers.
- Authentication, authorization, tenant isolation, or ownership rules.
- Database writes, constraints, transactions, migrations, and concurrency.
- Queues, webhooks, payment / notification adapters, and external API integrations.
- Backend regression and operational failure handling.

Do not use as the primary workflow for browser UI behavior (Frontend Testing), general language-level tests (Automated Test Authoring), or test strategy planning only (Test Plan Design).

## Scope and constraints
Inspect actual language, framework, persistence technology, API contracts, authentication model, test harness, and CI conventions. Never assume a particular stack. Tests should validate server-side enforcement even when a client is expected to validate input.

## Required inputs
Use acceptance criteria, API contracts, domain rules, authorization policy, database schema, relevant services, migrations, dependency adapters, existing tests and fixtures, and safe test-environment details. If a security or business rule is missing, do not guess.

## Workflow
1. **Map the behavior.** Identify route / handler, service, data writes, external calls, state transitions, and failure modes.
2. **Inspect test conventions.** Read manifests, test runner configuration, factories, fixture setup, database bootstrap, mocks, container use, and CI scripts.
3. **Choose test layers.** Use unit tests for domain rules; service / component tests for orchestration; database integration tests for persistence semantics; API / contract tests for externally visible behavior; end-to-end tests only for critical flows.
4. **Create a risk matrix.** Include valid behavior, invalid and boundary input, permission denial, ownership / tenant isolation, persistence, duplicate requests, concurrency, and dependency failure where relevant.
5. **Build safe fixtures.** Use synthetic records, isolated schemas / transactions, dedicated test accounts, and deterministic provider simulators.
6. **Test authorization.** Verify both allowed and denied operations at the server boundary. Test object-level access, role / scope constraints, tenant boundaries, and protected fields as applicable.
7. **Test data integrity.** Verify constraints, transaction commit / rollback, atomic multi-write behavior, concurrency controls, idempotency, and migration compatibility.
8. **Test integrations.** Cover timeout, retry boundaries, malformed payloads, duplicate delivery, partial failure, and compensation with controlled dependencies.
9. **Author diagnostic assertions.** Assert response contract, persisted state, emitted event, or observable side effect. Avoid assertions on private call counts unless they define a required contract.
10. **Execute safe checks.** Run focused tests and relevant lint / type / build checks only in an approved isolated environment. Do not run destructive or production integration tests without authorization.
11. **Report evidence.** Distinguish authored tests, executed tests, blocked tests, and results from unavailable infrastructure.

## Backend test principles
- Keep domain logic tests fast and deterministic.
- Use a real database for behaviors that depend on database semantics, such as constraints, isolation, locking, or query behavior; a repository mock cannot prove these.
- Use contract tests to verify API / event compatibility without requiring every provider to be available.
- Exercise authorization independently from UI visibility.
- Verify that forbidden requests leave no unauthorized state changes.
- Test transactions across success and failure boundaries.
- Test idempotency using repeated requests or duplicate messages and verify the intended single / repeated effect.
- Avoid relying on implementation-only response details that are not part of the contract.
- Use bounded, deterministic concurrency tests; avoid uncontrolled load in ordinary test suites.
- Keep test data and cleanup inside an isolated namespace.
- Record known differences between an emulator, fake, provider sandbox, and production service.

## Decision rules
- If database semantics matter, prefer a real isolated test database or an explicitly supported test container; do not claim equivalent coverage from mocks.
- If credentials or provider access are required, use a documented sandbox and synthetic data.
- If authorization policy is unclear, mark the relevant cases blocked rather than inventing access expectations.
- If a test needs production data or production writes, stop and request an approved alternative.
- If migration testing is destructive, require disposable data, backup strategy, and explicit approval.
- If concurrency behavior cannot be controlled in the current harness, state the gap and propose an environment-level test.
- If pre-existing failures exist, record the baseline before attributing regressions.

## Output contract
Return:
1. Backend behavior and system boundaries under test.
2. Test-layer selection and coverage rationale.
3. Tests created / changed and scenario inventory.
4. Test database, fixtures, external dependency strategy, and isolation.
5. Exact commands executed and actual results.
6. BLOCKED / NOT RUN checks and remaining data, security, or integration risks.

## Safety and permissions
- Use synthetic or explicitly approved masked data.
- Never log credentials, tokens, authorization headers, or sensitive request bodies.
- Keep all write tests in isolated databases or namespaces.
- Do not trigger real payments, emails, SMS, webhooks, or production jobs.
- Avoid destructive database, migration, load, or chaos tests without explicit authorization and recovery controls.
- Treat request bodies, imported files, and provider responses as untrusted input.

## Failure handling
| Situation | Response |
| --- | --- |
| Authorization rules are unknown | Block affected assertions and request the authoritative policy. |
| Test database unavailable | Mark persistence integration coverage BLOCKED; do not substitute a mock silently. |
| Provider sandbox unavailable | Test the adapter contract with an explicit fake and mark provider integration unverified. |
| Transaction test leaks state | Fix rollback / cleanup before accepting the suite. |
| Concurrency case is nondeterministic | Add deterministic coordination or identify the environment-level gap. |
| Baseline is failing | Record exact existing failures separately from new failures. |

## Validation checklist
- [ ] Server-side validation and authorization are covered.
- [ ] Object ownership and tenant boundaries are exercised where applicable.
- [ ] Persistence tests use a suitable database boundary.
- [ ] Transaction, rollback, idempotency, and concurrency risks are considered.
- [ ] Provider failures and duplicate delivery are covered where relevant.
- [ ] Fixtures are synthetic, isolated, and cleaned up.
- [ ] No real production side effect is triggered.
- [ ] Exact execution evidence and limitations are reported.

## Supporting resources
- Read \`references/backend-test-levels-and-data.md\` when choosing test boundaries and fixture strategy.
- Read \`references/backend-risk-scenarios.md\` for authorization, integrity, integration, and failure scenarios.
- Copy \`assets/backend-test-plan.template.md\` for a focused verification plan.
- Use \`evals/cases.yaml\` for correctness and safety evaluation.

## References
- [OWASP — Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP — Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)
- [Google Testing Blog — Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)

## Maintenance
- Owner: Backend Engineering / Quality Engineering
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: database / framework changes, authorization policy updates, provider contract changes, or evaluation failures.
