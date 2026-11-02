# When to Create an Architecture Decision Record

An ADR is valuable when it preserves reasoning that would otherwise be difficult to reconstruct. It should not become a bureaucratic record for every implementation detail.

## Strong candidates

Create an ADR when a choice:
- Is costly, risky, or difficult to reverse.
- Establishes a system boundary, architectural pattern, or deployment model.
- Changes data ownership, persistence, consistency, or migration strategy.
- Selects a major platform, framework, vendor, or external dependency.
- Defines an API or integration contract with compatibility consequences.
- Affects security, privacy, reliability, availability, recovery, or performance.
- Establishes a standard used by multiple teams or services.
- Creates a meaningful operational or maintenance obligation.

## Usually not an ADR

A short code comment, pull-request description, or local note may be sufficient for:
- Naming choices.
- Small refactors that preserve behavior and architecture.
- Local library usage within an established standard.
- Routine implementation details that are easy to change.
- Decisions already fully captured in an authoritative design record.

## One decision per record

Weak: "Choose our frontend framework, database, hosting, and authentication provider."

Better: separate records for:
1. Frontend application framework.
2. Primary persistence technology.
3. Hosting / deployment model.
4. Authentication and identity integration.

Link related ADRs so future maintainers can understand the combined design.

## Questions that indicate significance

- Would reversing the choice cause substantial rework or migration?
- Does the choice affect multiple components or teams?
- Does it introduce a new security, privacy, or operational risk?
- Will future maintainers need to understand why this option was chosen?
- Does it establish a precedent or constrain future choices?

If the answer is no to all, an ADR may not be worthwhile.

## Timing

Record the decision when the context and alternatives are still fresh, ideally before implementation makes the choice difficult to revisit. A retrospective ADR can still be useful, but label its status and distinguish known history from reconstructed rationale.

## Lifecycle discipline

- Proposed: the decision is under review.
- Accepted: the authorized decision-maker explicitly agrees.
- Rejected: the option was considered and declined.
- Superseded: a later record replaces it.
- Deprecated: the decision no longer applies.

An accepted ADR is historical evidence. Do not rewrite it to pretend a different decision was made earlier. Create a new record and link it.
