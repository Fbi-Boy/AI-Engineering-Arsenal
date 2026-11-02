# Work Decomposition Patterns

Choose the smallest useful breakdown that makes the work understandable, testable, and reviewable.

## Common work-item hierarchy

| Level | Typical purpose | Exit evidence |
| --- | --- | --- |
| Outcome | A measurable user or business change. | Outcome measure or decision evidence. |
| Milestone | A meaningful delivery or learning checkpoint. | Demonstrable result or validated learning. |
| Epic / capability | A coherent group of related behavior. | Child stories satisfy the capability intent. |
| User story / feature | A user goal or system behavior. | Acceptance criteria pass. |
| Task / subtask | A bounded implementation or verification action. | Reviewable artifact or completion evidence. |
| Spike | Time-boxed investigation to reduce uncertainty. | Findings, recommendation, and next decision. |

Do not force every project to use every level.

## Decomposition patterns

### Vertical slices

Split by user-visible or system-observable outcomes. A slice may include UI, API, domain logic, persistence, and tests, but delivers a thin end-to-end capability.

Example:
- User can view their own attendance record.
- User can request a correction.
- Authorized staff can approve or reject a correction.

Vertical slices make feedback possible earlier than a sequence of disconnected frontend-only and backend-only work.

### Workflow steps

Use when a process has distinct stages or handoffs. Include alternate and failure paths so the breakdown does not cover only the happy path.

### Business rules

Split complex rules when each rule can be implemented and verified independently. Preserve a shared source of truth when rules interact.

### Technical enablers

Use for cross-cutting prerequisites such as authentication integration, observability, test infrastructure, or data migration. Link each enabler to the outcomes it unlocks.

### Spikes

Use a spike when uncertainty is too high for a responsible implementation estimate. Define:
- The question to answer.
- The time box, if authorized by the team.
- Evidence to collect.
- Output format.
- Decision the findings enable.

A spike is not an unbounded task labeled "research".

## Example: campus attendance feature

Outcome: A student can see whether an attendance event was recorded.

Possible slices:
1. View own attendance for a selected course and period.
2. Display clear loading, empty, and error states.
3. Request correction with a reason and supporting evidence, if that workflow is approved.
4. Allow an authorized staff role to review a correction.
5. Notify the student of the recorded decision.

For each slice, consider permissions, audit history, tests, and data retention. Do not assume policy or workflow rules that stakeholders have not confirmed.

## Avoid common decomposition failures

- **Technical silos only:** "Build database", "build API", "build UI" with no demonstrable outcome.
- **Too many tiny tasks:** splitting every keystroke or trivial action creates coordination overhead.
- **Missing quality work:** no testing, error handling, observability, security, or documentation.
- **Unbounded research:** a spike without a question or decision output.
- **Hidden dependencies:** a task appears ready even though an API contract or policy decision is unresolved.
- **False certainty:** a task has an exact estimate despite major unknowns.
