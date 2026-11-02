# Backend Feature Plan — [Feature]

> **Status:** Proposed  
> **Date:** YYYY-MM-DD  
> **Repository / ref:** [Repo and branch / commit]  
> **Runtime / framework:** [Observed]  
> **Source requirement:** [Story / FR / acceptance criteria]

## 1. Behavior and boundary

[What server-side behavior is required? What is included / excluded?]

## 2. Repository evidence

| Area | Current pattern | Evidence / path |
| --- | --- | --- |
| Routes / transport | [Observed] | [Path] |
| Domain / service layer | [Observed] | [Path] |
| Persistence / schema | [Observed] | [Path] |
| Auth / validation | [Observed] | [Path] |
| Tests / scripts | [Observed] | [Path / command] |

## 3. Request and response contract

- Inputs: [Path / query / body / event]
- Outputs: [Response / event / job status]
- Errors: [Validation / auth / conflict / dependency]

## 4. Authorization and data boundaries

[Function, object, tenant, property, data sensitivity, ownership, audit.]

## 5. Domain and persistence changes

[Invariants, transaction scope, constraints, concurrency, migration dependency.]

## 6. Integrations and side effects

| Side effect | Timeout / retry | Idempotency / duplicate behavior | Failure / compensation |
| --- | --- | --- | --- |
| [API / queue / email] | [Policy / TBD] | [Rule / TBD] | [Behavior] |

## 7. Proposed code changes

| Path / module | Responsibility | Change | Risk |
| --- | --- | --- | --- |
| [Path] | [Layer] | [Behavior] | [Risk] |

## 8. Verification plan

| Check | Command / test | Expected evidence | Status |
| --- | --- | --- | --- |
| Unit / domain | [Command] | [Assertion] | Not run |
| Integration | [Command] | [Result] | Not run |
| Auth / security | [Method] | [Evidence] | Not run |
| Lint / type / build | [Command] | [Result] | Not run |

## 9. Open decisions and dependencies

- [Question / owner / dependency]

> This plan does not authorize production migrations, data changes, credential changes, or deployment.
