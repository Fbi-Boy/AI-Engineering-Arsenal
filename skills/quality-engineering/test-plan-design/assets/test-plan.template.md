# Software Test Plan — [Project / Feature / Release]

> **Status:** Draft / Proposed / Approved  
> **Version:** 0.1  
> **Date:** YYYY-MM-DD  
> **Test owner:** [Role / TBD]  
> **System / baseline:** [Name, branch / release / commit]  
> **Decision supported:** [Feature acceptance / release readiness / migration approval]

## 1. Objectives

[What quality risks and user outcomes must testing address?]

## 2. Test basis and scope

**Test basis**
- [Requirement / story / acceptance criteria / API / architecture / ADR]

**In scope**
- [Feature / interface / platform / data / risk]

**Out of scope**
- [Boundary and reason]

## 3. Assumptions and constraints

| ID | Assumption / constraint | Impact | Owner / evidence |
| --- | --- | --- | --- |
| A-001 | [Item] | [Impact] | [Role / source] |

## 4. Risk assessment

| Risk ID | Failure mode | Likelihood | Impact | Priority | Mitigation / test coverage |
| --- | --- | --- | --- | --- | --- |
| R-001 | [Failure] | [High / Medium / Low / TBD] | [High / Medium / Low / TBD] | [Priority] | [Test / control] |

## 5. Test strategy and levels

| Level / type | Purpose | Scope | Environment / tool | Included? |
| --- | --- | --- | --- | --- |
| Unit | [Purpose] | [Rule / module] | [Runner] | Yes / No + reason |
| Integration | [Purpose] | [Boundary] | [Environment] | Yes / No + reason |
| Contract | [Purpose] | [Interface] | [Tool] | Yes / No + reason |
| System / E2E | [Purpose] | [Journey] | [Environment] | Yes / No + reason |
| Acceptance | [Purpose] | [Outcome] | [Owner] | Yes / No + reason |
| Exploratory | [Purpose] | [Risk charter] | [Environment] | Yes / No + reason |
| Operational / NFR | [Purpose] | [Quality] | [Tool] | Yes / No + reason |

## 6. Requirement / risk traceability

| Requirement / outcome | Risk | Planned test / case ID | Level / technique | Evidence required | Status |
| --- | --- | --- | --- | --- | --- |
| FR-001 | R-001 | TC-001 | Integration | [Result / artifact] | Planned |

## 7. Data and environment

[Environment topology, test accounts / roles, synthetic or masked data, reset strategy, external dependencies, timezone / locale, and access controls.]

## 8. Test techniques and scenario inventory

- [Positive / happy path]
- [Negative / validation]
- [Boundary / equivalence partition]
- [State transition / decision table]
- [Authorization / tenant boundary]
- [Integration / timeout / retry]
- [Migration / backup / recovery]
- [Accessibility / performance / exploratory]

Remove irrelevant items and add context-specific scenarios.

## 9. Automation and execution approach

[Which checks run in CI, locally, nightly, or manually; tooling; isolation; flakiness policy; artifact retention.]

## 10. Roles, dependencies, and schedule

| Activity | Owner / role | Dependency | Target / estimate | Status |
| --- | --- | --- | --- | --- |
| [Activity] | [Role / TBD] | [Dependency] | [Date / TBD] | Planned |

Do not assign people or dates without agreement.

## 11. Entry criteria

- [ ] [Build / baseline available]
- [ ] [Environment and data ready]
- [ ] [Test basis / acceptance criteria reviewed]

## 12. Exit criteria and release decision

- [ ] [Required test level / coverage evidence]
- [ ] [Defect severity threshold approved]
- [ ] [Residual risk owner / decision recorded]
- [ ] [Required security / accessibility / operational checks completed]

**Threshold source / approver:** [Policy / role / TBD]

## 13. Defect management and reporting

[Severity definitions, triage path, evidence capture, retest, regression, and status reporting.]

## 14. Risks, exclusions, and open decisions

| ID | Item | Impact | Owner / next action |
| --- | --- | --- | --- |
| Q-001 | [Open item] | [Impact] | [Role / TBD] |

> This plan defines intended verification only. It does not claim test execution, passing results, or release approval.
