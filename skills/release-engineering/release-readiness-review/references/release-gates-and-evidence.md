# Release Gates and Evidence

## Evidence quality
Prefer direct, attributable evidence:
- Commit / pull request and included change list.
- Reproducible build identifier and immutable artifact digest.
- Test report with command, environment, version, timestamp, and actual result.
- Security review and dependency scan results with scope and tool versions.
- Migration rehearsal, backup verification, and data reconciliation.
- Approved deployment plan, environment protection, and change record.
- Monitoring dashboard, alert test, runbook, and named owner.
- Recorded go / no-go decision from the authorized approver.

A plan is not execution evidence. A status badge without scope or report may be insufficient. A passing check in one environment does not prove every target environment.

## Gate table
For each gate, record:
- Requirement and rationale.
- Status: PASS, FAIL, BLOCKED, NOT EVIDENCED, or N/A.
- Evidence location and time.
- Scope / version covered.
- Owner and required action.
- Whether an approved exception exists.

## Common gates
### Product and scope
- Requirements and acceptance criteria are complete.
- Included changes match the intended release.
- Known limitations and customer impact are documented.

### Engineering quality
- Required CI checks pass on the release commit.
- Regression and critical integration coverage is complete.
- Defect triage is current and blockers are resolved.
- Build artifact is identifiable and reproducible enough for the project.

### Security and privacy
- Security review is complete at required depth.
- Critical dependency and vulnerability findings are resolved or explicitly accepted by the authorized owner.
- Secrets and private data are not present in artifacts.
- Data handling and privacy impacts are reviewed.

### Data and compatibility
- Schema and migration sequence is reviewed and rehearsed.
- Backup and restore assumptions are verified.
- Old / new application compatibility is understood.
- Reconciliation checks are defined for important data changes.

### Delivery and ownership
- Deployment steps and environment are known.
- Required approvals are recorded.
- Monitoring, alerts, and runbooks are ready.
- Support and on-call ownership are explicit.
- Rollback / recovery path and post-release validation are rehearsed or evidenced.

## Risk acceptance
An exception must name the specific risk, impact, compensating controls, owner, approver, expiry or revisit date, and affected release. The reviewer records the exception but does not grant it.
