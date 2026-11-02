# Test Reliability and Isolation

## Determinism
Control or inject sources of nondeterminism:
- Clock and timezone.
- Random seeds and generated identifiers.
- Network and external service responses.
- Filesystem paths and temporary directories.
- Environment variables and process configuration.
- Concurrency, scheduling, and shared resources.

Do not freeze these values globally if tests can run in parallel. Prefer per-test controls and cleanup.

## Isolation
Each test should be able to run alone and in a different order. Isolate:
- Database records, schemas, or transactions.
- Browser/session state where applicable.
- Queues, topics, buckets, and object keys.
- Temporary files and ports.
- Global settings, caches, and static state.

Use unique test namespaces and reliable teardown. A cleanup step must not delete resources outside its owned namespace.

## Async and concurrency
- Await asynchronous work and assert the resulting state.
- Prefer synchronization on observable events or bounded conditions to arbitrary sleeps.
- Test race conditions only in a controlled environment with explicit barriers or coordination.
- Do not add broad retries that hide a race or product defect.
- Make test timeout values proportionate and explain non-default settings.

## External boundaries
Prefer local emulators, contract tests, provider sandboxes, or explicit test doubles. Make it obvious when a test does not reach the real provider. Do not call a production API simply because credentials are available in the environment.

## Diagnostics
Preserve the first useful failure signal:
- Test identifier and scenario.
- Expected and observed outcome.
- Relevant sanitized logs or traces.
- Environment and dependency versions.
- Seed and configuration when they affect reproduction.

Never publish secrets, session cookies, authorization headers, real personal data, or sensitive request bodies in logs or test artifacts.

## Flaky test workflow
1. Confirm whether the failure reproduces in isolation.
2. Compare isolated and parallel execution.
3. Inspect timing, shared state, network, clock, order, and cleanup.
4. Separate environment instability from an application defect.
5. Fix the cause and add diagnostic evidence.
6. Re-run the affected test and relevant suite.
7. Record remaining uncertainty instead of silently quarantining the test.

Quarantine or skip only under an explicit team policy, with an owner, reason, and revisit condition.
