# System Architecture Review Checklist

## Scope and drivers
- [ ] System boundary, target release, and exclusions are explicit.
- [ ] Stakeholder goals and important functional requirements are represented.
- [ ] Critical quality attributes are identified with operating context.
- [ ] Constraints are sourced and distinguished from preferences.

## Responsibilities and boundaries
- [ ] Each major component / container has a clear responsibility.
- [ ] Data ownership and source-of-truth boundaries are clear.
- [ ] External actors and dependencies are accurately identified.
- [ ] Trust boundaries and sensitive data flows are visible.
- [ ] Coupling, shared state, and cross-boundary dependencies are understood.

## Interaction and failure
- [ ] Synchronous and asynchronous interactions are distinguished.
- [ ] Timeouts, retries, idempotency, ordering, and partial failure are considered where relevant.
- [ ] Recovery and degraded operation are discussed.
- [ ] Integration contracts and compatibility needs are identified.

## Quality attributes
- [ ] Security, privacy, availability, performance, scalability, and maintainability are addressed where material.
- [ ] Each major quality requirement has a design response and verification idea.
- [ ] No arbitrary performance or availability threshold is presented as approved.
- [ ] Operations, observability, and support responsibilities are considered.

## Diagram quality
- [ ] C4 level matches the question and audience.
- [ ] Naming is consistent across diagrams.
- [ ] Relationships have clear meaning.
- [ ] Diagrams do not mix logical and deployment concerns without explanation.
- [ ] Inferred / uncertain elements are marked.
- [ ] Sensitive information is excluded from public artifacts.

## Trade-offs and governance
- [ ] Alternatives are credible and compared against actual drivers.
- [ ] Complexity and operational cost are proportionate.
- [ ] Significant choices have ADR candidates.
- [ ] Assumptions, risks, open decisions, and decision owners are explicit.
- [ ] Architecture approval is not implied by a generated diagram.
