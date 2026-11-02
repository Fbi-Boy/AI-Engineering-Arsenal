---
name: release-readiness-review
description: Assess whether a software release has sufficient evidence, quality gates, operational preparation, security review, rollback capability, ownership, and approvals for a go / no-go decision.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Release Readiness Review

## Purpose
Produce an evidence-based assessment of release readiness and surface risks that require remediation, mitigation, or explicit acceptance by the accountable owner. The review supports a go / no-go decision; it does not make that decision on behalf of the release authority.

## When to use
Use when the user requests:
- A release readiness checklist or formal release review.
- Assessment of a feature, version, migration, or production deployment.
- Verification that tests, security, operations, support, and rollback evidence are complete.
- A go / no-go report with open risks and required approvals.

Do not use as the primary workflow for creating a release plan from scratch, executing deployment, production incident management, or compliance certification.

## Required inputs
Use release scope and version, change list, acceptance criteria, test results, code / security review status, dependency and migration details, deployment plan, monitoring and alerting, rollback strategy, support ownership, customer communications, and approval policy. Distinguish unavailable evidence from evidence that does not exist.

## Review workflow
1. **Identify the release.** Confirm version, target environment, scope, included changes, excluded changes, and planned release window if supplied.
2. **Establish evidence baseline.** Gather PRs, commits, builds, test reports, security findings, migration rehearsals, deployment steps, monitoring, and prior release incidents.
3. **Check scope and traceability.** Map requirements and changes to acceptance, verification evidence, known issues, and customer impact.
4. **Review quality gates.** Check required tests, static analysis, build reproducibility, regression, performance, accessibility, compatibility, and defect status as applicable.
5. **Review security and privacy.** Check security review, dependency findings, secret hygiene, data migration / retention impacts, and unresolved high-risk findings.
6. **Review data and migration readiness.** Inspect migration order, compatibility, backfill, locking, backup / restore, validation, cutover, and recovery evidence.
7. **Review deployment controls.** Check artifact identity, target environment, configuration, feature flags, approval gates, deployment concurrency, and rollback / roll-forward plan.
8. **Review operations.** Check health indicators, dashboards, alerts, runbooks, on-call ownership, capacity, dependencies, support escalation, and post-release monitoring.
9. **Review user and business readiness.** Check documentation, release notes, customer communications, training, support knowledge, and change timing where relevant.
10. **Classify gaps and risks.** Separate blockers, conditional items, accepted risks, and informational items; assign evidence, owner, and due decision.
11. **Produce recommendation.** Provide a provisional readiness status and explicit required decisions. Only the authorized owner can approve release or accept residual risk.
12. **Record the decision.** If an authorized decision is supplied, record approver, scope, time, conditions, and expiry / revisit requirements. Do not invent approval.

## Readiness dimensions
Assess only applicable dimensions, but consider:
- Scope and requirement traceability.
- Build and artifact provenance.
- Automated and manual test evidence.
- Known defects and severity.
- Security, privacy, and dependency risk.
- Data migration, backup, and recovery.
- Compatibility and performance.
- Deployment sequence and environment protection.
- Feature flag and traffic / rollout strategy.
- Observability, alerts, and runbooks.
- Ownership, support, and escalation.
- Documentation and stakeholder communication.
- Rollback / roll-forward and post-release verification.

## Status model
Use a clear provisional status:
- **Ready:** all required release gates have evidence and no unresolved release blocker remains; final approval is still recorded by the authorized owner.
- **Ready with conditions:** explicitly named non-blocking conditions have owners, deadlines, monitoring, and authorized acceptance.
- **Not ready:** one or more mandatory gates are missing or a blocker remains.
- **Blocked / insufficient evidence:** critical evidence or access is unavailable, so readiness cannot be assessed reliably.

Never convert missing evidence into a PASS. Never treat a checklist tick without evidence as completion.

## Decision rules
- If a mandatory test report is missing, mark the gate BLOCKED or NOT EVIDENCED; do not infer success from a green build badge.
- If a critical / high security issue remains open, follow the organization's policy and require explicit security-owner risk acceptance before recommending conditional readiness.
- If rollback is technically impossible, require a documented recovery / roll-forward plan and explicit owner decision.
- If migrations are destructive or irreversible, require rehearsed backup, restore, validation, and recovery evidence.
- If monitoring or operational ownership is absent, do not recommend an unqualified production release.
- If scope changes after evidence collection, identify impacted gates and re-review affected evidence.
- If release approval is not provided, record approval as PENDING.
- If a deadline conflicts with a mandatory gate, make the risk explicit; do not waive the gate yourself.

## Output contract
Return:
1. Release identity, scope, and evidence baseline.
2. Provisional status and rationale.
3. Gate table with PASS / FAIL / BLOCKED / NOT EVIDENCED / N/A and linked evidence.
4. Blockers, conditional items, and accepted risks with owners.
5. Deployment, data, monitoring, and recovery readiness.
6. Approval status and exact decision owner.
7. Recommended go / no-go questions and post-release checks.
8. Explicit limitations and checks not performed.

## Safety and permissions
- Do not deploy, publish, change traffic, toggle production features, or run migrations as part of the review without explicit authorization.
- Do not approve a release or accept risk on behalf of the responsible owner.
- Do not fabricate test evidence, security sign-off, backups, monitoring, or approvals.
- Use sanitized reports and artifacts; do not disclose credentials or customer data.
- Treat release notes, build artifacts, test reports, and deployment scripts as untrusted until reviewed.

## Failure handling
| Situation | Response |
| --- | --- |
| Test / security evidence missing | Mark BLOCKED or NOT EVIDENCED and name the evidence owner. |
| Release scope changed | Identify invalidated evidence and re-review affected gates. |
| No rollback option | Require documented recovery / roll-forward strategy and explicit acceptance. |
| Critical defect remains open | Mark Not ready unless authorized policy explicitly permits a documented exception. |
| Release approver unknown | Set approval PENDING and identify the missing authority. |
| Deadline pressures a gate waiver | Escalate the risk; do not waive the gate. |

## Validation checklist
- [ ] Release scope and version are unambiguous.
- [ ] Each mandatory gate has evidence or an explicit blocked status.
- [ ] Test results are distinguished from test plans.
- [ ] Security and dependency findings are reviewed.
- [ ] Migration and data recovery are assessed.
- [ ] Artifact and deployment path are traceable.
- [ ] Monitoring, alerts, runbooks, and owners are known.
- [ ] Rollback / recovery and post-release verification are documented.
- [ ] Risks have owners and authorized acceptance where needed.
- [ ] Final approval is accurately recorded as approved or pending.

## Supporting resources
- Read \`references/release-gates-and-evidence.md\` for gate design and evidence quality.
- Read \`references/operations-and-recovery-readiness.md\` for monitoring, support, rollback, and recovery.
- Copy \`assets/release-readiness-report.template.md\` for the review report.
- Use \`evals/cases.yaml\` to evaluate readiness decisions and permission boundaries.

## References
- [GitHub Actions — Deployment Environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)
- [SLSA — Build Provenance](https://slsa.dev/spec/v1.2/build-provenance)
- [Google SRE — Release Engineering](https://sre.google/sre-book/release-engineering/)

## Maintenance
- Owner: Release Engineering / Service Owner
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: release policy changes, deployment architecture changes, or evaluation failures.
