# Skills Catalog

This directory contains the actual reusable skill packages. Each skill must be self-contained, have one SKILL.md at its package root, and follow the standards in the [Skill Handbook](../skill-handbook/README.md).

A category is an organizing label, not a skill by itself. Add a directory only when a concrete workflow has been designed with a validation plan and evaluation cases.

## Package convention

~~~text
skills/
└── <domain>/
    └── <skill-name>/
        ├── SKILL.md
        ├── references/    # Optional
        ├── scripts/       # Optional
        ├── assets/        # Optional
        └── evals/         # Optional, recommended for complex skills
~~~

The folder name and SKILL.md frontmatter name should match. Keep each package independently understandable and maintainable.

## Skill status

Use these statuses in the catalog and pull request descriptions:

- **Proposed** — problem identified; design not complete.
- **Draft** — package is being authored.
- **In Review** — implementation and evaluation cases are ready for review.
- **Ready** — required review and validation gates passed, including evaluation in a target agent runtime.
- **Deprecated** — no longer recommended; replacement or reason is documented.

Do not mark a skill Ready based only on the presence of a SKILL.md file. Writing evaluation cases is not the same as running them.

## Current packages

The following packages have been submitted for review. "In Review" does not mean runtime evaluation or stakeholder approval has passed.

| Skill | Status | Purpose | Package |
| --- | --- | --- | --- |
| requirements-discovery | In Review | Discover and document stakeholder needs, software requirements, constraints, and open decisions | [requirements-discovery/](project-planning/requirements-discovery/) |
| project-brief | In Review | Turn a software idea or discovery output into a concise project initiation brief | [project-brief/](project-planning/project-brief/) |
| task-breakdown | In Review | Decompose agreed scope into traceable, independently verifiable work items and dependencies | [task-breakdown/](project-planning/task-breakdown/) |
| acceptance-criteria | In Review | Write observable, testable acceptance conditions for requirements and user stories | [acceptance-criteria/](quality-engineering/acceptance-criteria/) |
| architecture-decision-record | In Review | Document significant architecture decisions, options, rationale, and consequences | [architecture-decision-record/](architecture/architecture-decision-record/) |
| use-case-modeling | In Review | Model actors, system boundaries, goal-oriented use cases, and interaction scenarios | [use-case-modeling/](requirements-engineering/use-case-modeling/) |
| change-impact-analysis | In Review | Trace proposed changes to affected requirements, architecture, data, tests, and operations | [change-impact-analysis/](project-planning/change-impact-analysis/) |

## Initial domain taxonomy

The following domains define intended coverage beyond the current packages. Items not listed in the current package table are candidates, not implemented skills.

| Domain | Candidate skill packages |
| --- | --- |
| Project planning | scope planning, estimation, roadmap |
| System analysis | user stories, process analysis, functional/non-functional requirements |
| Software architecture | C4 diagrams, component design, API architecture, design trade-off analysis |
| UI/UX engineering | design brief, user flows, wireframes, design-system audit, accessibility review |
| Frontend engineering | frontend scaffolding, component design, state management, responsive UI, frontend testing |
| Backend engineering | API design, service implementation, authentication patterns, background jobs, backend testing |
| Database engineering | ERD design, schema design, normalization, SQL generation, migration review, query optimization |
| AI engineering | LLM integration, retrieval-augmented generation, agent workflow design, tool integration, evaluation design |
| Quality assurance | test planning, test-case generation, automated testing, bug triage, regression analysis |
| Security engineering | threat modeling, secure code review, dependency risk review, secrets hygiene |
| DevOps and platform | CI/CD design, containerization, deployment planning, observability, infrastructure review |
| Documentation engineering | README authoring, API documentation, architecture documentation, changelog and release notes |

## Suggested implementation order

Build the library in vertical slices. A few complete, evaluated skills are more useful than dozens of shallow prompt files.

### Phase 1 — Project foundations

1. requirements-discovery
2. project-brief
3. task-breakdown
4. acceptance-criteria
5. architecture-decision-record
6. change-impact-analysis

### Phase 2 — Core software design

7. use-case-modeling
8. system-architecture-design
9. api-design
10. database-erd-design
11. database-schema-review

### Phase 3 — Implementation workflows

12. frontend-feature-implementation
13. backend-feature-implementation
14. codebase-understanding
15. code-review
16. debugging-and-root-cause-analysis

### Phase 4 — Quality, safety, and delivery

17. test-plan-design
18. automated-test-authoring
19. security-review
20. ci-cd-pipeline-design
21. release-readiness-review

### Phase 5 — Advanced capabilities

22. rag-system-design
23. ai-agent-workflow-design
24. mcp-tool-integration
25. performance-analysis
26. technical-documentation

Priorities may change based on actual project demand, evaluation results, and maintenance cost.

## Adding a skill

1. Open a design brief using the [authoring workflow](../skill-handbook/authoring-workflow.md).
2. Create one package under the most relevant domain.
3. Use the [SKILL.md template](../skill-handbook/templates/SKILL.template.md).
4. Add references, scripts, assets, and evaluation cases only where needed.
5. Run the checks in the [review checklist](../skill-handbook/templates/review-checklist.md).
6. Open a focused pull request. Do not combine unrelated skills into one large PR.
7. Register the package here as In Review when its implementation and evaluation cases are submitted.
8. Mark it Ready only after review, required validation, and target-runtime evaluations pass.

## Scope rule

The library may cover the full software project lifecycle, but each individual skill must stay focused. Use an orchestrator or task planner to coordinate multiple skills; do not make every skill responsible for selecting and executing the entire library.
