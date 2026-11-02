# UML Use-Case Modeling Concepts

## System boundary

A system boundary names the subject being modeled. Use cases inside the boundary represent behavior the subject provides. Actors remain outside it and interact with the subject.

State whether the diagram covers:
- The whole product.
- A subsystem or service.
- A specific release or increment.
- The current state or a proposed target state.

A boundary is a scope decision, not a deployment boundary unless explicitly modeled that way.

## Actors

An actor is an external role that interacts with the subject. Actors may be:
- Human roles (Student, Administrator, Support Agent).
- External software systems (Campus Identity Provider, Payment Gateway).
- External devices or organizations where they participate in the interaction.

Name actors by role, not by the person currently filling the role. One person can perform multiple roles in different contexts.

Do not draw an internal module as an actor if it belongs inside the system boundary.

## Use cases

A use case represents a goal-oriented service or behavior provided by the system to an actor. Name it with a verb phrase:
- View attendance history.
- Submit correction request.
- Approve correction request.
- Export monthly report.

Avoid naming use cases after screens, tables, buttons, classes, or internal methods.

## Relationships

| Relationship | Meaning | Use when |
| --- | --- | --- |
| Association | Actor participates in a use case. | Show actor-to-use-case participation. |
| Generalization | Specialized actor or use case inherits from a more general one. | There is a genuine "is-a" specialization. |
| `include` | Required reusable behavior is included by a base use case. | The included behavior is always part of the base interaction. |
| `extend` | Conditional or optional behavior extends a base use case at an extension point. | The base use case is meaningful without the extension. |

### Include

An included use case represents behavior that the base use case requires. It is not simply a later step or a shared label.

Example concept:
- "Submit correction request" includes "Validate request data" when validation is always part of submission.

### Extend

An extending use case adds conditional behavior to a base use case.

Example concept:
- "Apply accessibility support" may extend "View report" when a user chooses an optional view mode, provided the behavior is modeled as a genuine extension rather than a simple UI toggle.

### Generalization

Use generalization when a specialized actor or use case shares the behavior of a more general one and adds or specializes behavior. Avoid using it as a visual grouping shortcut.

## What use-case diagrams do not show

A use-case diagram does not show:
- The order of steps in a scenario.
- Message exchange between internal objects.
- Database tables and relationships.
- Screen layout or navigation design.
- Detailed business-process flow.

Use sequence, activity, ER, or UI diagrams for those questions.

## Readability

- Use a small number of goal-oriented use cases per diagram.
- Split large diagrams by subsystem or actor group.
- Keep a shared actor and use-case register across views.
- Add a note for assumptions or unresolved decisions rather than encoding guesses into relationships.

## Example scope

For a campus attendance system:
- Boundary: "Attendance Management System".
- Actors: Student, Lecturer, Attendance Administrator, Campus Identity Provider.
- Candidate use cases: View own attendance, Record attendance, Request correction, Review correction, Authenticate user.
- Permission rules must come from an authorized campus policy; actor names alone do not establish what each role may do.
