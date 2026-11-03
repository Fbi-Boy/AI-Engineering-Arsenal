---
name: multi-skill-workflow-planning
description: Build dependency-aware execution plans across multiple AI Engineering Arsenal skills by decomposing outcomes, defining artifacts and acceptance criteria, sequencing work, controlling parallelism, estimating uncertainty, and managing change.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Multi-Skill Workflow Planning

## Purpose
Convert a multi-domain engineering goal into an executable, reviewable plan of bounded skill tasks. The plan must show why each skill is needed, what it consumes and produces, which dependencies gate it, how completion is verified, and how risk, uncertainty, parallelism, and changes are managed.

This skill creates the plan. It does not execute specialist tasks, grant permissions, approve external actions, or claim delivery completion.

## When to use
Use when a project goal requires multiple skill packages, parallel work, dependency management, cross-artifact acceptance, or a clear execution sequence. Do not use for a single small task with no meaningful dependencies.

## Required inputs
Use user goal, scope and constraints, current project baseline, catalog and runtime availability, required deliverables, known dependencies, acceptance criteria, actors / owners, risk / approval boundaries, resources, and dates if supplied. Mark unknown estimates or capacity as unknown.

## Workflow
1. **Define the outcome.** Convert the request into observable deliverables and completion evidence.
2. **Set scope boundaries.** Record inclusions, exclusions, assumptions, and decisions that need an owner.
3. **Decompose deliverables.** Break work into bounded tasks that can be owned and accepted independently.
4. **Map skill ownership.** Select verified skills for each task and distinguish skill work from application / human responsibilities.
5. **Define task contracts.** For each step specify input artifacts, expected output, acceptance criteria, dependencies, risk, permissions, and stop conditions.
6. **Build the dependency graph.** Add a directed edge where an upstream artifact must be validated before downstream work starts. Identify cycles and redesign them as bounded iterations.
7. **Prioritize.** Rank by critical path, risk reduction, user value, uncertainty, and dependency leverage. State the prioritization method.
8. **Schedule safe parallel work.** Parallelize only independent tasks whose resource, write, and evidence scopes do not conflict.
9. **Estimate uncertainty.** Use ranges or qualitative confidence supported by known complexity and capacity; do not invent precise dates.
10. **Define verification gates.** Add review, testing, security, integration, and owner acceptance before high-impact transitions.
11. **Plan change control.** Define how requirement changes invalidate artifacts, dependencies, estimates, and approvals.
12. **Plan recovery.** Define checkpoints, retry policy, rollback / compensation owner, cancellation behavior, and blocked-task handling.
13. **Publish the plan.** Use the workflow plan template and present assumptions, risks, decisions, and the proposed first executable slice.

## Planning rules
- Plan around deliverables and acceptance evidence, not just a list of prompts.
- Each task has one accountable owner, even when multiple people or skills contribute.
- Every dependency edge must have a reason and an artifact or decision that satisfies it.
- Prefer a dependency DAG for ordinary project flows. Any loop must have a fixed iteration limit and exit condition.
- Separate design, implementation, test authoring, test execution, review, release approval, and deployment.
- Keep work packages small enough to validate but large enough to produce a useful result.
- Parallelize independent discovery, reference research, or isolated implementation only when merge / shared-resource risks are managed.
- Serialize schema migrations, shared-file edits, mutable data updates, and actions where ordering affects correctness.
- Reserve an integration task for cross-package consistency and interface mismatches.
- Include explicit owner decisions as tasks; do not hide them as assumptions.
- Plans are living artifacts. Re-baseline after material scope, dependency, risk, or capacity changes.

## Decision rules
- If scope is unclear, add a discovery task before downstream commitments.
- If architecture / API / data decisions are prerequisites, gate implementation on the accepted artifact.
- If two tasks need the same mutable resource, sequence them or define safe isolation.
- If an estimate has weak evidence, use a range or label it unestimated.
- If the critical path contains an unavailable runtime or approval, show the blocker and alternative.
- If a loop cannot be bounded, do not represent it as an executable plan.
- If acceptance criteria are subjective, define a review rubric and owner.
- If the project is too small for multi-skill coordination, recommend a simpler single-skill path.

## Output contract
Return:
1. Goal, deliverables, scope, exclusions, and assumptions.
2. Task / skill breakdown with accountable owners.
3. Dependency graph and critical path.
4. Inputs, outputs, and acceptance criteria per task.
5. Parallel / serial execution schedule and rationale.
6. Risk, approval, resource, and uncertainty register.
7. Integration and verification gates.
8. Change, recovery, cancellation, and escalation rules.
9. Recommended first slice and unresolved owner decisions.

## Safety and permissions
- A planned action is not authorized execution.
- Identify targets and data scope for any external or destructive step.
- Include explicit approval tasks where required; never assume broad project authorization covers every side effect.
- Do not expose secrets or unnecessary personal data in planning artifacts.
- Do not assign an unavailable tool or runtime as if it were ready.
- Preserve cancellation and stop conditions in the plan.

## Failure handling
| Situation | Response |
| --- | --- |
| Requirement gap blocks a dependency | Add discovery / decision task and keep downstream steps pending. |
| Dependency cycle | Split the work or create a bounded iteration with explicit exit criteria. |
| Capacity unknown | Do not invent dates; mark estimate uncommitted. |
| Shared resource conflict | Serialize tasks or define isolated workspaces and integration ownership. |
| Upstream output invalid | Mark descendants blocked and request correction. |
| Scope changed | Recompute affected dependencies, artifacts, approval, and estimates. |

## Validation checklist
- [ ] Deliverables and evidence are observable.
- [ ] Every task has one accountable owner.
- [ ] Every skill is verified as cataloged and runtime-available.
- [ ] Inputs / outputs and acceptance criteria are defined.
- [ ] Dependencies are explicit and acyclic or bounded.
- [ ] Parallel work is safe for write and resource scopes.
- [ ] Estimates and dates are evidence-based or marked unknown.
- [ ] Approval and risk gates are included.
- [ ] Integration, change, and recovery are planned.
- [ ] Execution is not implied by the plan.

## Supporting resources
- Read `references/dependency-graphs-and-critical-path.md` for DAGs, critical path, and dependency gates.
- Read `references/scheduling-risk-and-change-control.md` for parallelism, uncertainty, risk, and re-planning.
- Copy `assets/multi-skill-workflow-plan.template.md` for a task plan.
- Use `evals/cases.yaml` for planning quality and safety evaluation.

## References
- [OpenAI — Orchestration and Handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)
- [OpenAI — Running Agents](https://developers.openai.com/api/docs/guides/agents/running-agents)
- [Google SRE — Managing Critical State](https://sre.google/sre-book/managing-critical-state/)

## Maintenance
- Owner: Engineering Program / Orchestration
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: project lifecycle changes, repeated dependency failures, or evaluation regressions.
