# Requirements Traceability for Change Analysis

Traceability connects a requirement to its origin and to downstream design, implementation, and verification artifacts. It helps reveal what a proposed change may affect.

## Traceability directions

### Backward / upward traceability

Trace a requirement or artifact back to:
- Stakeholder need.
- Business objective.
- Source request.
- Policy or constraint.
- Parent requirement.

This helps test whether the item is still justified and whether a change affects the intended outcome.

### Forward / downward traceability

Trace a need or requirement forward to:
- Derived requirements.
- Use cases and workflows.
- Architecture decisions and components.
- Data structures and API contracts.
- Implementation tasks.
- Acceptance criteria and test evidence.
- Operations and documentation.

This helps identify likely downstream work when a requirement changes.

## Practical traceability matrix

| Source / parent | Requirement | Design / use case | Component / interface | Test / evidence |
| --- | --- | --- | --- | --- |
| OUT-001 | FR-004 | UC-002 | Attendance API | AT-019 |

Use stable IDs and links. Do not create links merely to make a matrix look complete.

## Change impact graph

For a proposed change:
1. Start from the changed source requirement or contract.
2. Follow known outgoing links to child artifacts.
3. Identify shared components used by multiple requirements.
4. Follow dependencies to external systems and teams.
5. Map each affected item to the verification evidence that may need revision.
6. Record where links are missing or stale.

A missing link creates uncertainty. It does not prove that no impact exists.

## Confidence labels

| Label | Meaning |
| --- | --- |
| Confirmed | Direct evidence shows the artifact or dependency is affected. |
| Strongly indicated | Multiple sources imply impact, but direct confirmation is not available. |
| Potential | Plausible relationship that requires inspection or owner confirmation. |
| No known impact | Checked within a defined scope; no impact was found there. |
| Unknown | Evidence is insufficient to make a useful determination. |

Always state the inspected scope and baseline.

## Maintaining traceability

- Keep IDs stable when requirement wording changes but identity remains the same.
- Create a new ID when the meaning or lifecycle is materially different.
- Preserve superseded links and history.
- Update trace links when architecture, APIs, tests, or requirements are refactored.
- Review high-risk and externally consumed requirements more frequently.
- Do not claim complete traceability if the repository or artifact set is only partially accessible.

## Reference concept

ISO/IEC/IEEE 29148 describes requirements traceability as documenting the derivation path upward to parent needs and the allocation / flow-down path to lower-level artifacts. Apply the concept proportionately; a small project can use a simple table, while a large system may need a managed traceability tool.
