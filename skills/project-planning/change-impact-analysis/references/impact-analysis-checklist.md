# Change Impact Analysis Checklist

Use the dimensions that are relevant to the proposed change. Record Not Applicable only when the scope makes that judgment reasonable.

## Product and requirements

- Does the change alter an outcome, actor, workflow, business rule, or system boundary?
- Are functional requirements added, modified, or removed?
- Do acceptance criteria or the Definition of Done need revision?
- Are existing behaviors required to remain backward-compatible?
- Are there conflicting or superseded requirements?

## Architecture and interfaces

- Do component responsibilities or boundaries change?
- Are APIs, events, contracts, or integration consumers affected?
- Are versioning, compatibility, rate limits, or failure behavior affected?
- Does an accepted ADR become inconsistent?
- Are third-party dependencies or vendor obligations introduced?

## Data

- Are entities, attributes, relationships, constraints, or ownership affected?
- Is migration, backfill, retention, deletion, or reconciliation required?
- Can old and new application versions operate against the data during rollout?
- Are backups and rollback procedures adequate?
- Is data quality or integrity at risk?

## Security and privacy

- Does the change affect identity, authentication, authorization, or privilege?
- Does data sensitivity, exposure, retention, or sharing change?
- Are audit logs, consent, or access records affected?
- Are secrets, keys, or credentials handled differently?
- Is a threat model or specialist security / privacy review needed?

## Quality attributes

- Performance and capacity.
- Availability and resilience.
- Recovery and backup.
- Accessibility and usability.
- Maintainability and supportability.
- Portability and compatibility.

Do not invent numeric thresholds; link to an approved target or mark it open.

## Verification

- Which unit tests need changes?
- Which integration and contract tests are affected?
- Are regression and end-to-end scenarios required?
- Do fixtures, mocks, and test data need revision?
- Are security, privacy, accessibility, performance, or recovery tests needed?
- What evidence will demonstrate successful completion?

## Operations and people

- Does deployment, monitoring, alerting, or runbook content change?
- Are support teams, administrators, or users affected?
- Is training or communication needed?
- Are external vendors or teams dependencies?
- Is a rollout, feature flag, phased migration, or rollback plan needed?

## Delivery and governance

- Is the release or milestone boundary affected?
- Does the change require reprioritization or new capacity?
- Who is authorized to approve the change?
- Are architecture, product, security, or domain reviews required?
- What evidence is still missing?

## Minimum report quality

The report should clearly show:
- What was inspected and against which baseline.
- What is directly affected versus potentially affected.
- What is unknown and how to validate it.
- What decisions are required before implementation.
- Which verification and transition tasks are necessary.
