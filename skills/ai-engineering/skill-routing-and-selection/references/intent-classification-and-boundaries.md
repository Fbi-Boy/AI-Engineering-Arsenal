# Intent Classification and Skill Boundaries

## Parse the request
Identify:
- **Action:** discover, design, implement, review, test, optimize, document, deploy, or decide.
- **Object:** requirement, architecture, endpoint, schema, UI, service, test, model, agent, pipeline, release, or document.
- **Output:** report, design, code, diagram, test suite, PR, decision, or external action.
- **Lifecycle stage:** plan, build, verify, deliver, operate, or maintain.
- **Constraints:** stack, platform, audience, permission, security, deadline, and cost.

## Domain ownership guide
| Request outcome | Primary domain | Common specialist boundary |
| --- | --- | --- |
| Understand stakeholder needs | Requirements Engineering | Do not implement before behavior is understood |
| Choose architecture | Architecture | Produce decision evidence, not code |
| Design API / ERD / schema | Contract / Data Design | Distinguish design from migration execution |
| Change frontend / backend behavior | Implementation | Inspect the existing stack and contracts |
| Author or run tests | Quality Engineering | Separate plan, code, and execution |
| Find defects in a diff | Code Review | General correctness, regression, maintainability |
| Find security weakness | Security Engineering | Threat paths, controls, safe validation |
| Design RAG / agent / MCP | AI Engineering | State, retrieval, tool and policy boundaries |
| Measure bottlenecks | Performance Engineering | Workload, baseline, profile, experiment |
| Prepare CI / release | DevOps / Release | Pipeline design versus approval / deployment |
| Explain or guide a reader | Documentation | Tutorial / how-to / reference / explanation |

## Lifecycle distinctions
- Design is a proposal; implementation changes source.
- A test plan defines coverage; test authoring creates executable checks; test execution produces results.
- Code review inspects a change; security review examines threats and controls.
- CI/CD design defines automation; a release readiness review assesses evidence; deployment changes a target environment.
- Technical documentation records verified behavior; it is not a substitute for product decisions.

## Catalog discipline
Only use a package and description present in the current catalog. If package status is Proposed, Draft, or In Review, report that status accurately. Catalog status does not guarantee the active runtime has loaded that skill.
