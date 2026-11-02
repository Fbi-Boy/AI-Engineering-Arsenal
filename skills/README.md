# Skills Catalog

This directory contains the actual reusable skill packages. Each skill must be self-contained, have one SKILL.md at its package root, and follow the standards in the [Skill Handbook](../skill-handbook/README.md).

A category is an organizing label, not a skill by itself. Add a directory only when a concrete workflow has been designed and evaluated.

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
- **Ready** — required review and validation gates passed.
- **Deprecated** — no longer recommended; replacement or reason is documented.

Do not mark a skill Ready based only on the presence of a SKILL.md file.

## Initial domain taxonomy

The following domains define the intended coverage of AI Engineering Arsenal. Each item is a candidate capability, not an implemented skill.

| Domain | Candidate skill packages |
| --- | --- |
| Project planning | requirements discovery, project brief, scope planning, estimation, roadmap, task breakdown |
| System analysis | use-case modeling, user stories, acceptance criteria, process analysis, functional/non-functional requirements |
| Software architecture | architecture decision records, C4 diagrams, component design, API architecture, design trade-off analysis |
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

### Phase 2 — Core software design

6. use-case-modeling
7. system-architecture-design
8. api-design
9. database-erd-design
10. database-schema-review

### Phase 3 — Implementation workflows

11. frontend-feature-implementation
12. backend-feature-implementation
13. codebase-understanding
14. code-review
15. debugging-and-root-cause-analysis

### Phase 4 — Quality, safety, and delivery

16. test-plan-design
17. automated-test-authoring
18. security-review
19. ci-cd-pipeline-design
20. release-readiness-review

### Phase 5 — Advanced capabilities

21. rag-system-design
22. ai-agent-workflow-design
23. mcp-tool-integration
24. performance-analysis
25. technical-documentation

Priorities may change based on actual project demand, evaluation results, and maintenance cost.

## Adding a skill

1. Open a design brief using the [authoring workflow](../skill-handbook/authoring-workflow.md).
2. Create one package under the most relevant domain.
3. Use the [SKILL.md template](../skill-handbook/templates/SKILL.template.md).
4. Add references, scripts, assets, and evaluation cases only where needed.
5. Run the checks in the [review checklist](../skill-handbook/templates/review-checklist.md).
6. Open a focused pull request. Do not combine unrelated skills into one large PR.
7. Update this catalog with the new package, status, and a one-line purpose after it is accepted.

## Catalog entry format

When a skill is ready, add it to the appropriate domain using this format:

| Skill | Status | Purpose | Package |
| --- | --- | --- | --- |
| requirements-discovery | In Review | Discover and document stakeholder needs, software requirements, constraints, and open decisions | [requirements-discovery/](project-planning/requirements-discovery/) |

Remove the example row when the first real package is added.

## Scope rule

The library may cover the full software project lifecycle, but each individual skill must stay focused. Use an orchestrator or task planner to coordinate multiple skills; do not make every skill responsible for selecting and executing the entire library.
