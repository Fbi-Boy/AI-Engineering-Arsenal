# Skill Authoring Workflow

Use this workflow whenever a new skill is proposed or an existing skill is substantially redesigned.

## 1. Discover a real recurring task

Start from a task, not from a technology name.

Good candidates have one or more of these characteristics:

- The same multi-step process is repeated across projects.
- Quality depends on following a known standard or sequence.
- Important steps are often forgotten when handled through an ordinary prompt.
- The task requires a predictable output format or validation process.
- The workflow combines several tools in a repeatable order.

Avoid creating a skill for a one-off question, a vague role such as "be a senior developer", or a capability the agent cannot access.

Record the problem in one paragraph. Include who performs the task, what triggers it, what a successful result looks like, and what currently goes wrong.

## 2. Write a skill design brief

Before writing SKILL.md, answer these questions:

| Area | Questions |
| --- | --- |
| Purpose | What concrete job does this skill complete? |
| Trigger | What words, files, context, or user intent indicate it should run? |
| Non-goals | Which similar tasks must not activate it? |
| Inputs | What information is required, optional, or inferable? |
| Outputs | What artifacts or decisions must be returned? |
| Tools | Which tools are genuinely required, and which are optional? |
| Constraints | What standards, platform limits, or user requirements apply? |
| Risks | Could the task change files, spend money, publish content, or affect external systems? |
| Validation | How can correctness be checked independently? |

Do not silently fill essential gaps with guesses. Ask for missing information when it changes architecture, safety, cost, or the validity of the result. Otherwise, state reasonable assumptions.

## 3. Define scope and activation

Write a concise description that identifies both the capability and its trigger.

A strong description says what the skill does and when to use it. A weak description says only "helps with programming" or "expert software engineer".

Document exclusions. For example, a database design skill may create logical and physical schemas but should not automatically deploy a production database or modify credentials.

A skill should not compete with another skill for the same broad task. If overlap is unavoidable, define the hand-off rule and keep the responsibilities distinct.

## 4. Design the workflow before writing prose

Express the task as ordered stages. A common pattern is:

1. Understand the request and identify the expected deliverable.
2. Inspect supplied files, repository context, and relevant constraints.
3. Identify missing inputs and record assumptions.
4. Consult authoritative references when the task depends on standards or changing technical details.
5. Produce the artifact or perform the authorized action.
6. Validate the result against explicit acceptance criteria.
7. Explain decisions, limitations, and any remaining work.

Adapt the stages to the task. Do not force irrelevant steps into every skill.

For each stage, define:
- The action the agent should take.
- The information it needs.
- The decision or condition that changes the next step.
- The expected intermediate result.
- The recovery path if the step fails.

## 5. Decide what resources are justified

Use instructions for judgment and workflow. Use references for detailed knowledge. Use scripts for deterministic checks or transformations. Use assets for reusable static material.

Do not add a script merely to make the package look advanced. Do not copy large external documentation into the repository when a maintained official link and a concise explanation are sufficient.

For each external reference, record its title, publisher, URL, and the date it was last checked when freshness matters.

## 6. Define the output contract

Tell the agent exactly what the user should receive.

Examples of output requirements:

- Required sections and their order.
- File formats and naming conventions.
- Whether diagrams must include source text as well as images.
- Whether assumptions and unresolved questions must be listed.
- Whether generated code must include tests.
- Whether results should be created in the repository or only proposed.

Prefer observable requirements over vague words such as "professional", "complete", or "high quality".

## 7. Establish safety boundaries

Classify actions by impact:

- **Read-only:** inspect documentation, list files, analyze code.
- **Local reversible:** create draft files or temporary artifacts.
- **Local destructive:** overwrite or delete user files.
- **External or high-impact:** publish, deploy, send messages, change permissions, incur costs, or modify production systems.

The skill may guide the agent through all categories, but authorization must come from the user and the host runtime. Never treat the existence of a tool as permission to use it.

When approval is required, explain the intended action and its likely impact before proceeding. Prefer dry runs and previews for risky changes.

## 8. Write SKILL.md

Use the repository template. Keep instructions direct, ordered, and easy to follow.

Prefer:
- Imperative steps.
- Explicit decision rules.
- Small input/output examples.
- Named validation checks.
- Clear failure and fallback behavior.

Avoid:
- Repeating the same rule in multiple sections.
- Unverifiable claims about expertise.
- Instructions such as "do everything perfectly".
- Hidden assumptions about installed tools or credentials.
- Long background chapters that belong in references.

## 9. Review the package locally

Check metadata, naming, links, examples, dependencies, and scripts. Run validators where available. Test the workflow with at least one normal case, one edge case, and one out-of-scope case before requesting review.

## 10. Maintain the skill

A skill has ongoing maintenance responsibilities. Identify likely change triggers:

- A referenced API or framework changes.
- A host changes how tools are exposed.
- A standard or security recommendation is updated.
- Evaluation cases reveal repeated failures.
- Users report confusing activation or output behavior.

Record a maintainer or ownership area when possible. Mark obsolete skills Deprecated rather than leaving misleading instructions active.

## Acceptance criteria for a new skill

A proposal is ready for review when:

- The task is real, repeatable, and narrowly scoped.
- Trigger and exclusion conditions are clear.
- Inputs and outputs are defined.
- The workflow is executable and ordered.
- Tool requirements and authorization boundaries are explicit.
- References and scripts have a clear reason to exist.
- At least three representative evaluation cases are documented.
- The package passes the review checklist.
