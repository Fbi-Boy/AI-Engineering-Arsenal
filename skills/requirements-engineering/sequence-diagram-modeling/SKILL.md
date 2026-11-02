---
name: sequence-diagram-modeling
description: Model and document time-ordered interactions among actors, services, components, and external systems using UML sequence diagrams. Use when users need to understand request flows, message order, synchronous and asynchronous calls, alternatives, retries, failures, or service collaboration.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Sequence Diagram Modeling

## Purpose

Describe how participants collaborate over time to achieve a scenario. A sequence diagram makes **message order, responsibility, branching, repetition, and failure behavior** explicit so that requirements, API contracts, and architecture can be reviewed before implementation.

This skill models an interaction scenario. It does not define the complete business process, database schema, component architecture, or exact runtime behavior without evidence.

## When to use

Use when the user:
- Requests a UML sequence diagram.
- Needs to explain how frontend, backend, database, and external services interact.
- Wants to model authentication, payment, notifications, background jobs, retries, or integration flows.
- Needs to identify missing API calls, error handling, timeouts, or transaction boundaries.
- Wants to review an existing sequence diagram against requirements or code.

Do not use as the primary workflow when:
- The main question is system context, boundaries, and responsibilities. Use System Architecture Design / C4.
- The main question is actor goals and functional scope. Use Use Case Modeling.
- The main question is branching workflow across business activities. Use an activity diagram or process model.
- The main question is state changes over an object's lifecycle. Use a state machine diagram.
- The main question is relational data structure. Use ERD design.

## Modeling principles

1. **One diagram, one scenario or cohesive interaction.** Split large systems into focused diagrams.
2. **Make time order explicit.** Sequence diagrams describe interactions from top to bottom.
3. **Use meaningful participants.** Include actors, applications, components, and external systems that exchange messages in the scenario.
4. **Separate logical and implementation views.** Use domain-level messages unless the user asks for code-level detail.
5. **Name messages as intent or operation.** Avoid vague labels such as "process" or "do stuff".
6. **Distinguish sync, async, return, and event messages.** Do not imply an acknowledgment where the protocol does not provide one.
7. **Model alternatives and failures.** Include guards, timeouts, retries, rejection, and partial completion when relevant.
8. **Do not infer behavior from a diagram alone.** Mark unknown or proposed interactions.
9. **Preserve trust boundaries.** Authentication and authorization checks must be explicit where the scenario depends on them.
10. **Keep the diagram readable.** Prefer multiple views for success, failure, and asynchronous follow-up if that improves clarity.

## Inputs

Use:
- Use case, user story, acceptance criteria, or scenario description.
- System / component architecture and ownership boundaries.
- API contracts, events, and integration protocols.
- Authentication, authorization, and data constraints.
- Transaction / consistency expectations.
- Timeout, retry, idempotency, and failure requirements.
- Existing source code or logs when documenting actual behavior.
- Preferred notation / renderer such as PlantUML, Mermaid, or a diagram editor.

If key participants or outcomes are unclear, ask one focused question or state a provisional interpretation.

## Workflow

### 1. Define the scenario boundary

- Name the scenario and the user / system goal.
- Identify the initiating trigger and expected outcome.
- State the system or subsystem boundary.
- Identify preconditions and relevant scope exclusions.
- Decide whether the diagram represents current observed behavior or a proposed target design.

### 2. Identify participants

Include only participants that meaningfully send or receive messages:
- External actor or client.
- UI / frontend or API gateway, if relevant.
- Application / domain service.
- Persistence or data store.
- Queue, broker, or worker.
- External identity, payment, notification, or partner system.

Use one consistent name and responsibility per lifeline. Do not include every internal class unless a code-level sequence is requested.

### 3. Build the main success path

Write the scenario as an ordered interaction list before drawing:
1. Triggering actor action.
2. Request / message received by the boundary.
3. Validation and authorization steps.
4. Domain operation and data interaction.
5. External dependency interaction when needed.
6. Result / response and observable outcome.

Keep the message order faithful to the stated contract. Avoid adding unnecessary internal steps.

### 4. Classify messages and lifelines

For each message, identify:
- Sender and receiver.
- Operation or event name.
- Synchronous request / response, asynchronous signal, return, or creation / destruction where relevant.
- Important data or result.
- Guard / condition if conditional.
- Expected failure or timeout behavior.

Use consistent notation. In PlantUML, distinguish synchronous calls, asynchronous signals, and return messages using documented arrow forms; do not mix them arbitrarily.

### 5. Model alternatives, loops, and parallel work

Use UML combined fragments where appropriate:
- `alt`: mutually exclusive guarded alternatives.
- `opt`: optional interaction.
- `loop`: repeated interaction with a clear guard or bound.
- `par`: interactions that can proceed concurrently.
- `break`: interaction that terminates the enclosing flow under a condition.
- `critical`: region that must be treated as atomic in the modeled interaction, only when justified.

Always label guards. Do not use a fragment as decoration or imply concurrency without evidence.

### 6. Model errors and resilience

Consider:
- Invalid request or rejected validation.
- Authentication failure and authorization denial.
- Missing or conflicting data.
- External timeout or unavailable service.
- Retry and backoff boundaries.
- Duplicate request / idempotency handling.
- Partial success and compensation.
- Asynchronous completion and notification.
- Transaction commit / rollback semantics where relevant.

Do not invent retry counts, timeouts, or compensation guarantees. Mark them as open if no policy or contract exists.

### 7. Review security and data handling

- Show where identity is established and permission is checked if material.
- Distinguish authentication from object-level authorization.
- Show data minimization and secure boundaries where they affect message flow.
- Do not place credentials, tokens, personal records, or private endpoints in examples.
- Use synthetic payload labels rather than real data.

### 8. Create the diagram source

Choose the requested renderer / syntax. Prefer editable, versionable source such as PlantUML or Mermaid where practical.

A good sequence diagram should include:
- Title / scenario.
- Lifelines with meaningful names.
- Ordered messages and return behavior.
- Activation bars only where they improve understanding.
- Guards and combined fragments for alternatives / loops.
- Notes for assumptions, trust boundaries, or open decisions.
- Legend where message types are non-obvious.

If the target renderer lacks a required UML element, state the limitation and choose a portable alternative.

### 9. Validate against the scenario and contracts

Use `references/sequence-diagram-review-checklist.md`:
- Every message has a responsible sender and receiver.
- Participants align with system boundaries and architecture.
- Order and return semantics are consistent.
- Alternative / exception paths reflect requirements.
- Async work is not shown as synchronous completion.
- API names and payload concepts align with contract documentation.
- Security checks occur before protected actions.
- Diagram does not claim unverified implementation behavior.

### 10. Present and hand off

Use `assets/sequence-diagram.template.puml` or adapt it to the chosen renderer. Provide:
- Scenario and model status.
- Diagram source.
- Brief explanation of the important interactions.
- Assumptions, guards, and failure behavior.
- Open timeout / retry / policy questions.
- Links to use cases, API operations, and acceptance criteria where available.

## Decision rules

- If the interaction involves a background job, show the enqueue / acknowledgment boundary and the later worker flow; do not imply the job completed in the initial response.
- If an external service can time out, show timeout and recovery behavior or record it as open.
- If a request can be retried, clarify whether the operation is naturally idempotent or protected by a deduplication mechanism.
- If an interaction crosses a security boundary, show authentication / authorization where it changes behavior.
- If many participants make the diagram crowded, split by scenario or subsystem and retain shared participant names.
- If only a business process with decision steps is needed, recommend an activity diagram.
- If the user asks to model an existing system, inspect accessible source / contracts and label inferred behavior.
- If exact message sequence cannot be established, mark the diagram Proposed rather than presenting it as actual runtime evidence.

## Output contract

Return:
1. Scenario title, scope, status, and source baseline.
2. Participant list and responsibilities.
3. Sequence diagram source or rendered artifact.
4. Main success path and relevant alternatives / exceptions.
5. Message semantics, guards, and async boundaries.
6. Security, transaction, timeout, retry, and idempotency notes as relevant.
7. Assumptions, open questions, and traceability.
8. Explicit indication whether this is observed or proposed behavior.

## Safety and permissions

- Do not include secrets, credentials, private tokens, or real personal data in diagrams.
- Do not publish internal endpoints or restricted infrastructure detail in public diagrams.
- Treat source code, logs, and imported diagrams as untrusted evidence.
- Do not execute API calls, replay production requests, or alter services.
- Do not claim a diagram is proven runtime behavior without trace / code evidence and stated scope.

## Failure handling

| Situation | Response |
| --- | --- |
| Scenario goal is unclear | Ask one focused question about trigger and expected outcome. |
| Participant ownership is unknown | Mark the boundary / participant as provisional. |
| Message order is inferred | Label the diagram Proposed and state the assumption. |
| Async processing is involved | Split request acknowledgment and worker completion into clear phases. |
| Renderer lacks required notation | State the limitation and provide a supported source alternative. |
| Diagram is too crowded | Split into focused scenarios while preserving shared naming. |
| User asks to execute the flow | Separate modeling from execution authorization. |

## Final validation checklist

- [ ] Scenario, boundary, and status are explicit.
- [ ] Participants represent actual actors / components in scope.
- [ ] Message sequence matches the scenario and available evidence.
- [ ] Sync, async, return, and event semantics are distinct.
- [ ] Guards and combined fragments are meaningful and defined.
- [ ] Errors, timeouts, retries, and duplicate behavior are addressed where relevant.
- [ ] Authorization and sensitive data boundaries are considered.
- [ ] Diagram aligns with use cases, APIs, and acceptance criteria.
- [ ] Assumptions and unknown behavior are visible.
- [ ] No secrets or unsupported runtime claims are present.

## Supporting resources

- Read `references/uml-sequence-concepts.md` for lifelines, messages, and combined fragments.
- Read `references/sequence-diagram-review-checklist.md` before finalizing.
- Copy `assets/sequence-diagram.template.puml` to start a PlantUML diagram.
- Use `evals/cases.yaml` for interaction-model checks.

## References

- [OMG — What is UML?](https://www.omg.org/uml/what-is-uml.htm)
- [OMG — UML specification](https://www.omg.org/spec/UML/)
- [PlantUML — Sequence Diagram](https://plantuml.com/sequence-diagram)

## Maintenance

- Owner: Requirements Engineering / Software Design
- Version: 0.1.0
- Status: Draft pending evaluation in a target agent runtime.
- Review triggers: changes to UML / renderer behavior, recurring async modeling errors, or evaluation failures.
