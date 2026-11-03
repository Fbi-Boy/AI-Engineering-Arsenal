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
- **In Review** — implementation and evaluation cases are submitted for review.
- **Ready** — required review and validation gates passed, including evaluation in a target agent runtime.
- **Deprecated** — no longer recommended; replacement or reason is documented.

Do not mark a skill Ready based only on the presence of a SKILL.md file. Writing evaluation cases is not the same as running them.

## Current packages

The following packages have been submitted for review. "In Review" does not mean runtime evaluation or stakeholder approval has passed.

| Skill | Status | Purpose | Package |
| --- | --- | --- | --- |
| requirements-discovery | In Review | Discover stakeholder needs, software requirements, constraints, and open decisions | [requirements-discovery/](project-planning/requirements-discovery/) |
| project-brief | In Review | Turn an idea or discovery output into a concise project initiation brief | [project-brief/](project-planning/project-brief/) |
| task-breakdown | In Review | Decompose agreed scope into traceable, verifiable work items and dependencies | [task-breakdown/](project-planning/task-breakdown/) |
| change-impact-analysis | In Review | Trace proposed changes to affected requirements, architecture, data, tests, and operations | [change-impact-analysis/](project-planning/change-impact-analysis/) |
| codebase-understanding | In Review | Map an existing repository, stack, architecture, entry points, and feature paths from evidence | [codebase-understanding/](software-maintenance/codebase-understanding/) |
| code-review | In Review | Review diffs for actionable correctness, security, regression, and maintainability findings | [code-review/](software-maintenance/code-review/) |
| debugging-and-root-cause-analysis | In Review | Investigate failures from sanitized evidence through hypotheses, root cause, and regression prevention | [debugging-and-root-cause-analysis/](software-maintenance/debugging-and-root-cause-analysis/) |
| user-stories | In Review | Create and refine outcome-oriented backlog stories with traceability | [user-stories/](requirements-engineering/user-stories/) |
| use-case-modeling | In Review | Model actors, system boundaries, goal-oriented use cases, and scenarios | [use-case-modeling/](requirements-engineering/use-case-modeling/) |
| sequence-diagram-modeling | In Review | Model time-ordered interactions, alternatives, asynchronous flows, and failures | [sequence-diagram-modeling/](requirements-engineering/sequence-diagram-modeling/) |
| acceptance-criteria | In Review | Write observable acceptance conditions for requirements and user stories | [acceptance-criteria/](quality-engineering/acceptance-criteria/) |
| test-plan-design | In Review | Plan risk-based verification, traceability, test levels, environments, and release exit criteria | [test-plan-design/](quality-engineering/test-plan-design/) |
| automated-test-authoring | In Review | Author deterministic automated tests from requirements using appropriate test levels, fixtures, and assertions | [automated-test-authoring/](quality-engineering/automated-test-authoring/) |
| architecture-decision-record | In Review | Document significant architecture decisions, options, rationale, and consequences | [architecture-decision-record/](architecture/architecture-decision-record/) |
| system-architecture-design | In Review | Create C4-oriented system architecture proposals and quality trade-off analysis | [system-architecture-design/](architecture/system-architecture-design/) |
| api-design | In Review | Design secure, evolvable HTTP API contracts and OpenAPI documentation | [api-design/](backend-engineering/api-design/) |
| database-erd-design | In Review | Model relational entities, attributes, keys, relationships, and constraints | [database-erd-design/](database-engineering/database-erd-design/) |
| database-schema-review | In Review | Review existing relational schemas, integrity, indexes, and migration safety | [database-schema-review/](database-engineering/database-schema-review/) |
| frontend-feature-implementation | In Review | Implement user-facing frontend features within the existing stack, with accessibility and responsive verification | [frontend-feature-implementation/](frontend-engineering/frontend-feature-implementation/) |
| frontend-testing | In Review | Verify UI behavior, accessibility, responsive states, browser interactions, and critical user journeys | [frontend-testing/](frontend-engineering/frontend-testing/) |
| backend-feature-implementation | In Review | Implement server-side features with validation, authorization, integrity, and integration safeguards | [backend-feature-implementation/](backend-engineering/backend-feature-implementation/) |
| rag-system-design | In Review | Design secure retrieval-augmented generation pipelines with grounded answers, provenance, freshness, and evaluation | [rag-system-design/](ai-engineering/rag-system-design/) |
| ai-agent-workflow-design | In Review | Design bounded agent workflows with tools, state, handoffs, approvals, guardrails, and observability | [ai-agent-workflow-design/](ai-engineering/ai-agent-workflow-design/) |
| ai-evaluation-design | In Review | Design representative datasets, metrics, calibrated graders, safety evaluations, and regression gates for AI systems | [ai-evaluation-design/](ai-engineering/ai-evaluation-design/) |
| mcp-tool-integration | In Review | Integrate MCP clients and servers with version-aware schemas, authorization, consent, and operational controls | [mcp-tool-integration/](ai-engineering/mcp-tool-integration/) |
| performance-analysis | In Review | Diagnose and improve software performance through workload measurement, profiling, and controlled experiments | [performance-analysis/](software-maintenance/performance-analysis/) |
| technical-documentation | In Review | Create and maintain accurate software documentation using reader-focused structure and docs-as-code validation | [technical-documentation/](documentation-engineering/technical-documentation/) |
| backend-testing | In Review | Verify server behavior, authorization, persistence, transactions, integrations, and data integrity | [backend-testing/](backend-engineering/backend-testing/) |
| security-review | In Review | Review code and system changes for trust-boundary, identity, data-protection, dependency, and configuration risks | [security-review/](security-engineering/security-review/) |
| ci-cd-pipeline-design | In Review | Design secure CI/CD stages, artifact promotion, workflow permissions, environment gates, and recovery | [ci-cd-pipeline-design/](devops-platform/ci-cd-pipeline-design/) |
| release-readiness-review | In Review | Assess release evidence, quality and security gates, operations, recovery, risks, and approvals | [release-readiness-review/](release-engineering/release-readiness-review/) |

## Initial domain taxonomy

The following domains define intended coverage beyond the current packages. Items not listed in the current package table are candidates, not implemented skills.

| Domain | Candidate skill packages |
| --- | --- |
| Project planning | scope planning, estimation, roadmap, release planning |
| System analysis | process analysis, functional / non-functional requirements, domain modeling |
| Software architecture | component design, deployment architecture, design trade-off analysis |
| UI/UX engineering | design brief, user flows, wireframes, design-system audit, accessibility review |
| Frontend engineering | frontend scaffolding, component design, state management, responsive UI, frontend testing |
| Backend engineering | service implementation, authentication patterns, background jobs, backend testing |
| Database engineering | SQL generation, migration authoring, query optimization, data migration planning |
| AI engineering | LLM integration, retrieval-augmented generation, agent workflow design, tool integration, evaluation design |
| Quality assurance | test planning, test-case generation, automated testing, bug triage, regression analysis |
| Security engineering | threat modeling, secure code review, dependency risk review, secrets hygiene |
| DevOps and platform | CI/CD design, containerization, deployment planning, observability, infrastructure review |
| Documentation engineering | README authoring, API documentation, architecture documentation, changelog and release notes |

## Suggested implementation order

Build the library in vertical slices. Prioritize complete, reviewed, evaluated skills over shallow prompt files. The order is a proposal and may change as project needs and evaluation results emerge.

### Phase 1 — Requirements and planning

1. requirements-discovery
2. project-brief
3. user-stories
4. use-case-modeling
5. acceptance-criteria
6. task-breakdown
7. change-impact-analysis

### Phase 2 — Core system and data design

8. system-architecture-design
9. architecture-decision-record
10. api-design
11. database-erd-design
12. database-schema-review
13. sequence-diagram-modeling

### Phase 3 — Implementation and maintenance workflows

14. frontend-feature-implementation
15. backend-feature-implementation
16. codebase-understanding
17. code-review
18. debugging-and-root-cause-analysis

### Phase 4 — Quality, safety, and delivery

19. test-plan-design
20. automated-test-authoring
21. frontend-testing
22. backend-testing
23. security-review
24. ci-cd-pipeline-design
25. release-readiness-review

### Phase 5 — Advanced capabilities

26. rag-system-design
27. ai-agent-workflow-design
28. ai-evaluation-design
29. mcp-tool-integration
30. performance-analysis
31. technical-documentation

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
