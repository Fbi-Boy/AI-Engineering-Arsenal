# Sequence Diagram Review Checklist

## Scenario and scope
- [ ] One coherent scenario is modeled.
- [ ] Goal, trigger, preconditions, and expected result are stated.
- [ ] Current observed behavior is distinguished from proposed future behavior.
- [ ] System boundary and participant ownership are clear.

## Participants and messages
- [ ] Lifelines represent meaningful actors, components, or systems.
- [ ] Every message has a sender, receiver, and clear intent.
- [ ] Names align with architecture, use cases, and API contracts.
- [ ] Sync calls, async messages, returns, and events are distinguishable.
- [ ] Message ordering is evidence-based or marked provisional.

## Branches and concurrency
- [ ] alt / opt / loop guards are explicit and meaningful.
- [ ] par is used only for truly concurrent behavior.
- [ ] Loop bounds or exit conditions are understandable.
- [ ] Break / critical fragments are justified by scenario semantics.

## Failure and resilience
- [ ] Validation and authorization failures are represented where relevant.
- [ ] Timeouts and external failures are considered.
- [ ] Retry and idempotency behavior is explicit or marked open.
- [ ] Partial success and compensation are described when material.
- [ ] Async acknowledgment is separated from later completion.

## Security and data
- [ ] Sensitive data is minimized in message labels and examples.
- [ ] Authentication and object-level authorization appear at the correct boundary.
- [ ] Credentials and private endpoints are not embedded.
- [ ] Data ownership and transaction boundaries are not implied incorrectly.

## Quality and traceability
- [ ] Diagram remains readable at the intended audience / level.
- [ ] Important interactions trace to requirements, use cases, or acceptance criteria.
- [ ] Unknown implementation behavior is labeled.
- [ ] Diagram is not used as a substitute for activity, state, ERD, or architecture views.
