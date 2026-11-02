# C4 Model Guide for Software Architecture

The C4 model is a notation-independent way to describe software architecture at different levels of zoom. Its core static views are System Context, Container, Component, and Code. Supporting views include System Landscape, Dynamic, and Deployment diagrams.

## Choose the smallest useful view

| View | Main question | Typical audience | Include |
| --- | --- | --- | --- |
| System Context | What is the system and who / what does it interact with? | Technical and non-technical | System, users, external systems |
| Container | What are the major applications, services, and data stores? | Delivery and engineering | Containers, responsibilities, high-level relationships |
| Component | What are the main components inside one container? | Developers and architects | Components, responsibilities, internal dependencies |
| Code | How is one component implemented? | Developers | Classes or other code-level structures |
| Dynamic | How do selected elements collaborate at runtime? | Developers and reviewers | Ordered interactions for one scenario |
| Deployment | Where do software elements run? | Platform and operations | Deployment nodes, environments, mapped software |

Not every system needs every diagram. Context and container views often provide enough shared understanding for an initial design.

## Terminology discipline

In C4, a **container** is an application or data store that executes code or stores data. It is not necessarily a Docker container.

A component is a cohesive grouping of related functionality inside a container. A component diagram should not simply reproduce every source folder or class.

A person is an actor represented as a role or persona. An external software system is outside the system boundary when it is not owned by the system being modeled.

## Relationship quality

For every relationship, identify:
- Source and destination.
- Direction where it matters.
- Purpose and data exchanged.
- Protocol / technology only when known or needed.
- Trust boundary and failure behavior where relevant.

Use relationship labels such as "reads attendance", "submits correction", or "publishes event". Avoid unexplained arrows.

## Model existing systems responsibly

When reverse-engineering:
1. Inspect accessible repository structure and key entry points.
2. Identify runtime processes, data stores, and external integrations from evidence.
3. Use README, dependency manifests, configuration examples, deployment files, and tests as supporting evidence.
4. Label uncertain responsibilities and inferred relationships.
5. Avoid assuming that a folder name equals a runtime component.
6. State which parts of the repository were not inspected.

## When a different diagram is better

- Use a use-case diagram for actor goals and functional scope.
- Use a sequence diagram for time-ordered interactions.
- Use an ERD for entities and relationships.
- Use an activity diagram for workflow and decision flow.
- Use a deployment diagram for runtime placement.

## Sources

- [C4 model — official site](https://c4model.com/)
- [C4 model diagrams](https://c4model.com/diagrams)
- [C4 system context diagram](https://c4model.com/diagrams/system-context)
