# UML Sequence Diagram Concepts

## Lifelines

A lifeline represents one participant in an interaction over time. It may represent an actor, software component, service, or external system. Use names that match the architecture and API contract.

A lifeline should not be added simply because an implementation has a file or class. Include it when it sends / receives a relevant message in the modeled scenario.

## Messages

Common message categories include:
- Synchronous call: sender waits for the called interaction to return before proceeding.
- Asynchronous signal / call: sender continues without waiting for a synchronous return.
- Reply / return: communicates the result of a prior call.
- Create / destroy: represents lifecycle changes when relevant.

The exact arrow syntax depends on the notation / renderer. In PlantUML, arrow style influences whether the message is drawn as a synchronous or asynchronous call. Check renderer documentation rather than guessing.

## Activation bars

Activation shows the period during which a participant is executing an interaction. It can clarify nested calls, but excessive activation bars can make a diagram noisy. A diagram does not need to expose every function call.

## Combined fragments

| Fragment | Meaning | Modeling guidance |
| --- | --- | --- |
| alt | Alternative guarded paths | Each operand has a guard; paths are alternatives. |
| opt | Optional interaction | Use for a condition that may or may not occur. |
| loop | Repeated interaction | State the condition or useful bound. |
| par | Concurrent operands | Use only when work can overlap. |
| break | Early termination | Show the condition that exits the enclosing interaction. |
| critical | Critical region | Use only when atomic / exclusive behavior is part of the model. |

A fragment is part of the semantic model, not just a box to visually group messages.

## Synchronous and asynchronous boundaries

Example request / background job pattern:
1. Client submits a request.
2. API authenticates, validates, and authorizes the caller.
3. Application records the operation and enqueues work durably.
4. API returns an acknowledgment with an operation identifier.
5. Worker processes the message later.
6. Client checks status or receives a notification.

Do not draw worker completion before the initial request response if the operation is genuinely asynchronous.

## Failure paths

Where relevant, show:
- Validation rejection.
- Authorization denial.
- Timeout from an external dependency.
- Retry with idempotency / deduplication.
- Compensation or partial completion.
- Failure notification and state reconciliation.

Do not invent guarantees such as exactly-once delivery. Many message systems provide at-least-once delivery; the design may need idempotent consumers.

## Distinguish adjacent diagram types

| Question | Better diagram |
| --- | --- |
| Who uses the system and for what goal? | Use-case diagram |
| How do participants exchange messages over time? | Sequence diagram |
| What is the business activity / decision flow? | Activity diagram |
| How does one entity change state? | State machine |
| What are the system's components and relationships? | C4 / component diagram |
| What data entities and relationships exist? | ERD |

## Sources

- [OMG — What is UML?](https://www.omg.org/uml/what-is-uml.htm)
- [OMG — UML specification](https://www.omg.org/spec/UML/)
- [PlantUML — Sequence Diagram](https://plantuml.com/sequence-diagram)
