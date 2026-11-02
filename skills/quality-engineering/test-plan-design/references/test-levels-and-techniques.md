# Test Levels and Test Techniques

Use the project's terminology and test policy where established. Names can vary between organizations; scope and purpose matter more than labels.

## Test levels

| Level | Focus | Typical scope | Example |
| --- | --- | --- | --- |
| Unit | Small isolated behavior | Function / class / pure rule | Calculate an attendance percentage. |
| Component | One module / service | Component with controlled collaborators | Test a service using a fake repository. |
| Integration | Interaction across boundaries | Database, filesystem, API, message broker | Verify persistence and retrieval against a test database. |
| Contract | Agreement between consumers and providers | API / event / message schema and behavior | Verify provider response matches OpenAPI contract. |
| System / end-to-end | Integrated user-visible flow | Whole application or critical journey | Student requests correction and views the result. |
| Acceptance | Fitness for stakeholder need | Agreed outcome and acceptance conditions | Product owner confirms a workflow against approved criteria. |
| Exploratory | Discover unknown behavior | Time-boxed charter and learning | Probe concurrent edits and unusual data combinations. |
| Operational | Readiness and recovery | Deployment / monitoring / backup / restore | Rehearse restore in a controlled environment. |

## Scope and feedback cost

A useful test portfolio balances:
- Fast isolated tests for detailed logic and many boundary conditions.
- Integration tests for important data / network / serialization seams.
- A small number of high-value end-to-end journeys.
- Exploratory testing for unknown risks and human judgment.

Do not blindly enforce a fixed percentage of each type. A system with complex integrations may need more contract / integration tests; a library may rely heavily on unit and compatibility tests.

## Test design techniques

### Equivalence partitioning
Divide input space into groups expected to behave similarly; choose representative values from each partition.

### Boundary value analysis
Test values at and around meaningful limits: minimum, maximum, just below, just above, empty, and overflow where applicable.

### Decision tables
List combinations of conditions and expected actions. Useful for permissions, eligibility, pricing, and business rules.

### State transition testing
Model states, events, valid transitions, and invalid transitions. Test both allowed paths and forbidden transitions.

### Pairwise / combinatorial testing
Cover interactions between parameters when exhaustive combinations are too numerous. Use risk knowledge to select deeper combinations.

### Error guessing
Use defect history, domain knowledge, and common implementation hazards to propose targeted checks. Do not confuse a guess with evidence of a defect.

### Exploratory testing
Use a charter with objective, boundaries, time box, data, notes, and findings. Preserve reproducible steps for defects discovered.

## Test doubles and external dependencies

Choose deliberately:
- Stub: returns controlled responses.
- Mock: verifies selected interaction expectations.
- Fake: lightweight working implementation suitable for tests.
- Simulator / service virtualization: models an external system boundary.
- Dedicated sandbox: real service instance with safe test data.

Test doubles should reflect important contract behavior. Avoid mocks that merely repeat the implementation's assumptions and therefore cannot detect contract drift.

## Flakiness and isolation

- Avoid dependence on execution order or shared mutable fixtures.
- Control clocks, randomness, concurrency, and network conditions where possible.
- Prefer deterministic waits / event synchronization over arbitrary sleep calls.
- Quarantine flaky tests only with an owner and remediation plan.
- Do not use automatic retry as a substitute for fixing nondeterminism.
- Record environment and failure artifacts for investigation.

## Sources

- [ISTQB CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [Martin Fowler — Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Google Testing Blog — Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)
