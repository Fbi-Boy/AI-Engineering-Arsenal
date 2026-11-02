# Test Authoring Principles

## Choose a level that matches the risk
- **Unit:** fast feedback for deterministic logic and domain rules.
- **Component:** one cohesive component with selected collaborators controlled.
- **Integration:** real interaction between components such as application and database, filesystem, queue, or provider sandbox.
- **Contract:** compatibility of an API, event, schema, or message boundary.
- **End-to-end:** a small set of critical user journeys across the assembled system.

A test suite should balance speed, confidence, diagnosis, and maintenance cost. Do not apply a fixed percentage or fixed test count to every project.

## Scenario design
For each requirement or defect, consider:
- Valid representative input and expected outcome.
- Invalid syntax and invalid semantics.
- Minimum, maximum, empty, missing, and oversized values.
- State transitions, duplicate actions, retries, and concurrency.
- Permission boundaries and ownership boundaries.
- Dependency timeout, malformed response, unavailable service, and partial failure.
- Regression condition that previously failed.

Use equivalence partitions and boundary analysis to avoid redundant test combinations. Use decision tables for combinations of business rules and state-transition cases where behavior depends on current state.

## Assertions and test oracles
A test oracle is the authoritative basis for deciding whether observed behavior is correct. Derive it from requirements, contracts, approved examples, or explicit invariants.

A useful assertion:
- Checks a meaningful output, state transition, persisted value, emitted event, or user-visible consequence.
- Includes diagnostic context in the failure message where the framework supports it.
- Avoids brittle snapshots of irrelevant fields or private implementation structure.
- Does not merely assert that a helper was invoked if the actual outcome can be observed.

Avoid asserting exact timestamps, generated IDs, ordering, whitespace, or internal call counts unless that detail is part of the contract.

## Fixtures and factories
- Keep fixture setup small, explicit, and discoverable.
- Give tests the minimum data they need.
- Prefer factories/builders for complex domain objects, with safe defaults and per-test overrides.
- Make fixture lifetime and cleanup behavior explicit.
- Avoid suite-global mutable state.
- Do not let fixture indirection obscure why the scenario should pass or fail.
- Parameterize only cases that share the same decision structure.

## Test doubles
- **Stub:** returns a controlled response.
- **Mock/spy:** verifies an interaction when the interaction itself is part of the contract.
- **Fake:** provides a lightweight working implementation, such as an in-memory repository.
- **Simulator:** models a complex dependency or environment in a controlled way.

Use test doubles at external boundaries, nondeterministic systems, or expensive dependencies. Do not mock every internal layer. A test with only mocks may verify the mock configuration rather than actual integration.

## Mutation and regression
A useful regression test should fail on the faulty behavior and pass after the correction. When available and proportionate, mutation testing can reveal assertions that do not detect meaningful code changes. Mutation score is a diagnostic, not a universal quality target.

## Review prompts
- Would this test fail if the defect returned?
- Could the assertion pass when the behavior is broken?
- Is the expected value supported by a requirement?
- Is the test independent of execution order?
- Is a real collaborator simpler and more trustworthy than another mock?
- Is the test at the right level for the risk?
