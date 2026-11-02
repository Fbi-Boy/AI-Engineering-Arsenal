# Operations and Recovery Readiness

## Observability
Confirm that the service exposes actionable signals for the release:
- Availability and key business transaction success.
- Error rate, latency, saturation, and resource use.
- Dependency health and queue / job backlog.
- Logs and traces with correlation identifiers and appropriate redaction.
- Alerts with thresholds, routing, owner, and runbook link.

Do not invent service-level objectives or alert thresholds. Use approved operational targets.

## Deployment and rollout
Review:
- Exact artifact and configuration to deploy.
- Environment and branch restrictions.
- Approval gates and change window.
- Feature flags, canary, traffic ramp, or staged rollout where supported.
- Concurrency protection against overlapping deployments.
- Health checks and stop / pause criteria.
- Compatibility across mixed versions during rollout.

## Recovery
A useful recovery plan identifies:
- Trigger and decision owner.
- Whether rollback is technically supported.
- Data compatibility and irreversible operations.
- Previous artifact and configuration identity.
- Recovery steps, expected duration assumptions, and verification.
- Roll-forward option if rollback is unsafe.
- Communication and escalation path.

A database restore is not equivalent to an application rollback. Consider data written after deployment and migrations that are not backward compatible.

## Support readiness
- Named service and on-call owner.
- Escalation and incident channel.
- Updated runbook and known issue notes.
- Support / customer-facing team briefing where appropriate.
- Post-release verification period and follow-up review.
