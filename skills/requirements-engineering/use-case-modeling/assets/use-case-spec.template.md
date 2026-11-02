# Use-Case Model — [System / Subsystem]

> **Version:** 0.1  
> **Status:** Draft / Proposed / Reviewed  
> **Date:** YYYY-MM-DD  
> **Model scope:** [Current / Target / Release]  
> **Source baseline:** [Requirements / brief / repository]

## 1. System boundary

**Subject:** [System or subsystem name]

**Inside the boundary:**
- [Capability / service]

**Outside the boundary:**
- [Actors / external systems]

**Explicit exclusions:**
- [Out-of-scope item]

## 2. Actor register

| Actor ID | Actor role | Primary goals | Source / authority | Status |
| --- | --- | --- | --- | --- |
| ACT-001 | [External role / system] | [Goals] | [Evidence] | Proposed |

## 3. Use-case register

| Use-case ID | Name | Primary actor | Goal / outcome | Related requirement |
| --- | --- | --- | --- | --- |
| UC-001 | [Verb phrase] | ACT-001 | [Outcome] | [FR / US / TBD] |

## 4. UML use-case diagram

[Insert diagram or PlantUML source here. Keep actors outside the subject boundary and use UML relationship semantics.]

## 5. Detailed specification

### UC-001 — [Use-case name]

- **Scope:** [System / subsystem]
- **Level:** [User goal / summary / subfunction]
- **Primary actor:** [Role]
- **Supporting actors:** [Roles / systems]
- **Stakeholder interests:** [Needs]
- **Trigger:** [Event]
- **Preconditions:** [Facts required before start]

#### Main success scenario

1. [Actor intent]
2. [System response]
3. [Actor intent]
4. [System response and observable outcome]

#### Alternate flows

- **A1 — [Condition]:** [Variation and result]

#### Exception flows

- **E1 — [Failure condition]:** [System response, state guarantee, and recovery path]

#### Postconditions

- Success: [Observable guarantee]
- Failure / cancellation: [State guarantee]

#### Business rules and permissions

- [Confirmed rule with source, or unresolved question]

#### Related requirements / acceptance criteria

- [ID] — [Link / description]

Repeat for selected important use cases.

## 6. Assumptions and open questions

| ID | Question / assumption | Impact | Decision owner |
| --- | --- | --- | --- |
| Q-001 | [Item] | [Impact] | [Role / TBD] |

## 7. Model validation

- [ ] Actors are external roles or systems.
- [ ] Use cases describe meaningful goals.
- [ ] System boundary is explicit.
- [ ] Relationships use correct UML semantics.
- [ ] Important alternate and exception flows are specified.
- [ ] Permissions are sourced or marked open.
- [ ] Use cases trace to stakeholder needs or requirements.

## 8. Review record

| Reviewer / role | Decision | Date | Notes |
| --- | --- | --- | --- |
| [Role] | Pending | — | — |
