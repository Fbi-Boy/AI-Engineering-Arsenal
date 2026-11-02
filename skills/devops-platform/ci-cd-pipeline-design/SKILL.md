---
name: ci-cd-pipeline-design
description: Design secure, maintainable continuous integration and delivery pipelines for an existing software repository, including validation stages, artifact flow, environment promotion, approvals, rollback, and supply-chain controls.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# CI/CD Pipeline Design

## Purpose
Design an automated integration and delivery pipeline that gives fast, trustworthy feedback and promotes immutable, traceable artifacts through controlled environments. The design must fit the repository's actual stack, delivery model, hosting platform, and risk.

This skill designs and documents pipeline changes. It does not automatically create cloud infrastructure, add secrets, grant permissions, run production deployments, or change protected environment rules.

## When to use
Use when the user requests:
- CI workflow design or pipeline improvement.
- Test, lint, type-check, build, package, and security stages.
- Artifact creation, promotion, deployment approvals, rollback, or release automation.
- Build reproducibility, provenance, or software supply-chain hardening.

Do not use as the primary workflow for a one-off local test run, general infrastructure architecture, or production incident response.

## Required inputs
Use repository structure and manifests, test/build commands, package manager and lockfiles, target platform, branching and release strategy, environment topology, secret management, deployment ownership, quality gates, compliance constraints, and required approvals. Mark missing context explicitly.

## Workflow
1. **Inspect the repository.** Detect languages, manifests, lockfiles, build commands, test suites, artifact outputs, existing workflows, and deployment scripts.
2. **Map delivery flow.** Identify triggers, branch protections, validation requirements, environments, artifact consumers, owners, and manual decisions.
3. **Set pipeline goals.** Balance feedback time, repeatability, coverage, cost, security, and operational reliability.
4. **Design validation stages.** Include formatting / lint, type checks, unit and integration tests, build, contract / end-to-end tests, and security checks where justified by the project.
5. **Define artifact lifecycle.** Build once where practical, identify artifacts immutably, record source commit and build metadata, retain evidence, and promote the same verified artifact between environments.
6. **Apply security controls.** Use least-privilege token permissions, protected secrets, trusted workflow sources, immutable action references or approved lockfiles, isolated runners, safe handling of pull-request code, and dependency controls.
7. **Define environment gates.** Use environment-specific approvals, branch restrictions, concurrency controls, and separation of validation from deployment.
8. **Plan failure and rollback.** Define stop conditions, artifact retention, deployment health checks, rollback or roll-forward strategy, and owner responsibilities.
9. **Review cost and maintainability.** Use dependency-aware caching, avoid duplicated expensive jobs, parallelize independent work, and keep workflow complexity proportional.
10. **Produce a reviewable design.** Include a workflow diagram or stage table, permissions matrix, trigger matrix, artifact flow, secrets plan, gate ownership, and operational notes.
11. **Validate safely.** Check syntax and configuration with available static validators. Do not execute a deployment or alter protected settings without explicit authorization.

## Design principles
- Start from the existing repository and target platform; do not assume GitHub Actions, Docker, Kubernetes, or a cloud vendor.
- Prefer explicit triggers and clear separation of pull-request checks, release builds, and deployment workflows.
- Make the least-privilege permission set explicit at workflow and job level.
- Do not expose privileged secrets to untrusted fork code or unsafe pull-request workflows.
- Pin third-party actions to immutable full-length commit SHAs or use the platform's approved dependency lock mechanism; review action source and ownership.
- Do not interpolate untrusted event fields directly into shell commands. Pass validated values through safe environment variables or structured inputs.
- Avoid using pull_request_target to execute untrusted contribution code with privileged tokens.
- Treat caches as untrusted inputs; do not let untrusted branches poison privileged release caches.
- Keep artifacts immutable and traceable to the source commit and toolchain.
- Separate build provenance from assumptions about source review or source integrity.
- Use staged promotion, approvals, and environment protections for high-impact deployments.
- Use concurrency controls to prevent overlapping deployments to the same target.
- Make rollback / recovery a designed capability, not a final release-day assumption.
- Avoid duplicating test execution unnecessarily; preserve clear required-check semantics.

## Decision rules
- If platform or hosting is unknown, produce a platform-neutral pipeline design and list options rather than inventing a platform.
- If test commands are unknown, inspect manifests and existing CI; do not create fictional scripts.
- If a workflow needs write permissions, justify the exact job and permission; default other jobs to read-only or none.
- If secrets are required, describe secret names and scopes without requesting or storing secret values in the repository.
- If deployment approval policy is missing, mark it as a required owner decision.
- If runners or environments are unavailable, document the design and mark execution validation BLOCKED.
- If action versions cannot be verified, do not invent commit SHAs; record a version-pin follow-up.

## Output contract
Return:
1. Repository stack and observed build / test conventions.
2. Pipeline diagram or ordered stage table.
3. Event / branch / path trigger matrix.
4. Job dependency and parallelism plan.
5. Permission and secret-scope matrix.
6. Artifact, provenance, environment promotion, and rollback design.
7. Required configuration and files to change.
8. Static validation performed and exact results.
9. Unresolved platform, owner, or approval decisions.

## Safety and permissions
- Never place secret values in workflow files, examples, logs, or PR descriptions.
- Do not grant broad write-all permissions as a shortcut.
- Do not run untrusted pull-request code in a privileged deployment context.
- Do not deploy, publish, release, rotate secrets, alter protection settings, or provision paid infrastructure without explicit authorization.
- Use protected environments for privileged deployment jobs where supported.
- Treat downloaded actions, packages, artifacts, caches, and event payloads as untrusted until verified.

## Failure handling
| Situation | Response |
| --- | --- |
| Platform unknown | Provide platform-neutral design and list decisions needed. |
| Build / test command missing | Inspect repository manifests; mark unknown commands as open. |
| Secret required | Specify approved secret scope; never ask the user to paste the value into source. |
| Workflow permission unclear | Default to least privilege and request owner confirmation for write scopes. |
| Static validator unavailable | Mark syntax validation BLOCKED; do not claim validity. |
| Deployment environment unprotected | Flag as a release risk and require owner decision before production automation. |

## Validation checklist
- [ ] Trigger and branch conditions are explicit.
- [ ] Required validation stages match actual project commands.
- [ ] Job permissions are least privilege and justified.
- [ ] Untrusted PR content cannot access privileged deployment secrets.
- [ ] Third-party actions / reusable workflows have a trusted pinning strategy.
- [ ] Artifacts are traceable and promoted without untracked rebuilding where feasible.
- [ ] Secrets and environments are properly separated.
- [ ] Deployments use appropriate approvals and concurrency controls.
- [ ] Rollback / recovery and health checks are documented.
- [ ] Static validation and deployment execution are reported separately.

## Supporting resources
- Read \`references/pipeline-stages-and-artifacts.md\` for stage / artifact patterns.
- Read \`references/pipeline-security-and-governance.md\` for workflow permissions, untrusted code, secrets, and environment gates.
- Copy \`assets/pipeline-design.template.md\` to document the design.
- Use \`evals/cases.yaml\` for pipeline security and quality evaluation.

## References
- [GitHub Actions — Secure Use Reference](https://docs.github.com/en/actions/reference/security/secure-use)
- [GitHub Actions — Workflow Syntax and Permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [GitHub Actions — Deployment Environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [SLSA — Build Track Basics](https://slsa.dev/spec/v1.2/build-track-basics)

## Maintenance
- Owner: DevOps / Platform Engineering
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: CI platform, runner, deployment target, security baseline, or supply-chain guidance changes.
