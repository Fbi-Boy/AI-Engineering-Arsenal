# AI Engineering Arsenal — Skill Handbook

This handbook defines how to design, author, validate, secure, test, review, and maintain reusable AI agent skills in this repository.

The goal is not to collect long prompts. The goal is to build small, dependable capabilities that help an agent complete real engineering work with less repetition and more consistent results.

## 1. What is a skill?

A skill is a packaged, reusable workflow for a clearly defined task. It normally contains:

- A discovery manifest: the skill name and a precise description of when it should be used.
- Instructions: the workflow the agent should follow.
- Optional references: technical material the agent can consult when needed.
- Optional scripts: deterministic helpers for work better performed by code.
- Optional assets: templates, schemas, fixtures, and other static resources.

A skill does not create new model intelligence by itself, train a model, or grant tools or permissions. It teaches an agent how to use its available context and tools to perform a repeatable task. Tool access must be provided by the host environment and governed separately.

## 2. Repository layout

The repository separates the rules for making skills from the skills themselves:

~~~text
AI-Engineering-Arsenal/
├── README.md
├── skill-handbook/
│   ├── README.md
│   ├── skill-anatomy.md
│   ├── authoring-workflow.md
│   ├── quality-security.md
│   ├── testing-evaluation.md
│   └── templates/
│       ├── SKILL.template.md
│       └── review-checklist.md
└── skills/
    └── README.md
~~~

Each actual skill package is stored in its own directory under skills/. For example:

~~~text
skills/
└── database/
    └── design-erd/
        ├── SKILL.md
        ├── references/
        ├── scripts/
        └── assets/
~~~

Do not put every skill's instructions into one giant document. Keep the handbook centralized, but keep each executable skill package independently discoverable and maintainable.

## 3. Core design principles

1. **One coherent responsibility.** A skill should solve one related class of tasks, not attempt to be an entire software department.
2. **Explicit activation.** Its description must state the task signals that should trigger it and the situations that should not.
3. **Progressive disclosure.** Keep essential instructions in SKILL.md and move large or infrequently used material into references/.
4. **Workflow before verbosity.** Explain what the agent must do, in what order, how to decide, and what to produce. Avoid motivational filler.
5. **Evidence over invention.** Prefer official documentation and primary sources. Mark assumptions and unknowns.
6. **Safe execution.** Separate analysis from actions that change files, accounts, infrastructure, or external systems. Request authorization when required.
7. **Testable outcomes.** Define inputs, expected outputs, failure handling, and quality checks.
8. **Portable by default.** Follow the open Agent Skills format where practical. Document host-specific features instead of assuming every agent supports them.

## 4. Skill lifecycle

Every skill should pass through these stages:

1. **Discover:** identify a repeated task, its users, frequency, and failure cost.
2. **Specify:** define purpose, triggers, exclusions, input requirements, output contract, tools, and safety boundaries.
3. **Design:** split the work into a clear workflow and decide which references or scripts are justified.
4. **Author:** create the package using the approved template.
5. **Validate:** check metadata, paths, links, script behavior, and package structure.
6. **Evaluate:** run normal, edge, ambiguous, and out-of-scope cases.
7. **Review:** inspect correctness, security, clarity, and maintainability in a pull request.
8. **Release:** merge the reviewed change and record its version/status in the catalog.
9. **Maintain:** update the skill when tools, standards, or source documentation change.

A draft is not production-ready merely because its Markdown file exists.

## 5. Handbook sections

- [Skill anatomy](skill-anatomy.md) — package structure, metadata, and progressive disclosure.
- [Authoring workflow](authoring-workflow.md) — a repeatable method for turning a task into a skill.
- [Quality and security](quality-security.md) — safety, reliability, permissions, and source handling.
- [Testing and evaluation](testing-evaluation.md) — validation cases, evaluation rubrics, and regression checks.
- [Skill template](templates/SKILL.template.md) — the starting point for a new skill.
- [Review checklist](templates/review-checklist.md) — the required pre-merge review.

Some companion pages are introduced in separate pull requests so that each section has a focused change history.

## 6. Definition of ready

A skill may be marked **Ready** only when:

- Its name and description are valid and unambiguous.
- Its scope and non-goals are documented.
- Its workflow is actionable and ordered.
- Required inputs, output format, and failure behavior are defined.
- References and scripts are relevant, safe, and maintained.
- Positive, negative, edge, and regression cases have been evaluated.
- No secrets or unnecessary permissions are embedded in the package.
- A reviewer can understand how to use and verify it without asking the author to explain missing steps.

Use **Draft**, **In Review**, **Ready**, or **Deprecated** as lifecycle labels. Do not call an untested skill production-ready.

## 7. Primary references

- [Agent Skills — Specification](https://agentskills.io/specification)
- [Agent Skills — Overview](https://agentskills.io/home)
- [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI Developers — Skills](https://developers.openai.com/plugins/concepts/skills)

The open specification defines the portable package format. Host documentation defines additional behavior that may differ between products and runtimes.
