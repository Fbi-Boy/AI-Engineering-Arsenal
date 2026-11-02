# Pipeline Stages and Artifact Flow

## Typical stage model
Adapt stages to the repository; not every project needs every stage.

1. **Change validation:** formatting, lint, static analysis, type checking, and policy checks.
2. **Fast tests:** unit and component tests with deterministic local dependencies.
3. **Integration validation:** database, contract, service, and selected system tests.
4. **Build:** compile / bundle / package from a known source commit and locked dependencies.
5. **Artifact verification:** inspect package contents, checksums, SBOM, signatures or attestations where appropriate.
6. **Pre-release validation:** end-to-end, migration rehearsal, smoke tests, and security checks in a controlled environment.
7. **Promotion:** deploy the same artifact to an environment using an approved identity and protection rules.
8. **Post-deploy verification:** health, key journeys, error rate, latency, and rollback / pause criteria.

## Artifact identity
Record at minimum:
- Source repository and commit.
- Build workflow / builder identity.
- Toolchain and dependency lock state.
- Artifact digest and storage location.
- Relevant test and policy evidence.
- Provenance / attestation reference when produced.

Avoid rebuilding separately for each environment if reproducible promotion of the same verified artifact is feasible. If the environment-specific build is unavoidable, document why it differs and how equivalence is established.

## Caching
- Cache package-manager downloads or build intermediates, not trusted release artifacts without verification.
- Scope cache keys by lockfile and platform.
- Avoid sharing writable caches between untrusted contribution jobs and privileged release jobs.
- Use a clean build as a diagnostic when cache integrity or reproducibility is uncertain.

## Reliability and cost
- Parallelize independent jobs.
- Keep required status checks stable and clearly named.
- Avoid redundant full-suite execution after equivalent validated jobs unless evidence justifies it.
- Use sharding only when tests are independent and test data is isolated.
- Preserve enough logs and artifacts to diagnose failures without retaining sensitive data indefinitely.
