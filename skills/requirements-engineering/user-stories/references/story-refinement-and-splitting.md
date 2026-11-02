# User Story Refinement and Splitting Guide

## Use the story pattern as a prompt

"As a [role], I want [capability], so that [benefit]" helps reveal user, capability, and value. It is not a mandatory sentence shape for every backlog item. System requirements, technical enablers, and constraints may need another form.

## Refinement questions

- Who experiences the need?
- What outcome are they trying to achieve?
- What happens today?
- What business rule or policy applies?
- What data is required and who owns it?
- What is the normal path?
- What important alternate / failure path exists?
- What should the user observe?
- What is explicitly out of scope?
- What evidence will show that the outcome is achieved?

## INVEST as a heuristic

| Dimension | Useful question | Warning sign |
| --- | --- | --- |
| Independent | Can it be planned without unnecessary blockers? | Many hidden cross-team dependencies. |
| Negotiable | Is the outcome clear while solution details remain open? | The story prescribes every UI / code detail too early. |
| Valuable | Does the result help a user, stakeholder, or system quality goal? | No clear beneficiary or reason. |
| Estimable | Does the team know enough to reason about size? | Major unknowns are hidden in the description. |
| Small | Is it a manageable slice for the team's horizon? | Several workflows or roles are bundled. |
| Testable | Can a reviewer observe the result? | Vague words such as "better" or "easy". |

A story may have dependencies and still be valid. INVEST identifies discussion topics; it is not a mathematical score.

## Splitting patterns

### By workflow step with standalone value

Large: "Manage student attendance."

Possible slices:
1. View own attendance by course and date.
2. View attendance status details for one event.
3. Submit a correction request, if policy permits.
4. Review a correction request by an authorized role.
5. Notify the requester of the decision.

Each slice should be useful and testable, not merely a layer of the same implementation.

### By business rule or scenario

Split different decision paths when they create separate value or can be delivered independently:
- Submit standard request.
- Submit request with supporting evidence.
- Handle a duplicate request.
- Handle a request after a deadline.

Keep shared validation rules traceable to one authoritative source.

### By actor or permission boundary

Create separate stories when actors have different goals or policy:
- Student views own records.
- Lecturer records attendance for assigned course.
- Administrator resolves disputed records.

Do not assume permissions from role names; use the approved access policy.

### By data lifecycle

Split creation, review, correction, archive, or export when each has a meaningful goal and separate acceptance behavior.

### Spike / discovery

Use a time-boxed spike when a key uncertainty blocks responsible design:
- Question to answer.
- Evidence to collect.
- Time box if agreed.
- Expected artifact.
- Decision enabled.

A spike is not a generic "research more" placeholder.

## Avoid bad splits

- By page or button only.
- By frontend/backend/database layers without an independently useful result.
- By arbitrary data fields.
- By happy path only while failure / authorization paths are forgotten.
- By splitting one story into tasks so small they have no reviewable result.

## Sources

- [Atlassian — User stories](https://www.atlassian.com/agile/project-management/user-stories)
- [GOV.UK — Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories)
