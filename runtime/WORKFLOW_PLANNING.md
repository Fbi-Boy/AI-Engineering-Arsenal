# Multi-skill workflow planning v0.1

## Purpose

The planner turns an **explicit list of task drafts** into a validated dependency
DAG, assigns an advisory skill-routing decision to each task, and computes stable
execution waves. Tasks in the same wave have no unresolved dependencies between
them and may be considered for parallel execution by a future executor.

## Input contract

Each task draft contains:
- `id`: unique, non-empty task identifier.
- `description`: task text used by the lexical skill router.
- `depends_on`: zero or more task IDs that must complete first.
- `acceptance_criteria`: one or more non-empty completion checks.

The caller is responsible for decomposing a natural-language request into these
drafts. Version 0.1 does not claim automatic semantic decomposition. A future
model adapter may propose drafts, but validation remains deterministic.

## Outcomes

- `ready`: dependency graph is valid and every task has a selected skill.
- `needs_clarification`: graph is valid, but at least one task has an ambiguous
  or missing skill match. The caller must resolve this before execution.
- `invalid`: malformed task data, unknown dependencies, duplicate IDs, or a
  dependency cycle was found.

Execution order is stable relative to input order. Parallel groups are topological
waves. A group is a scheduling hint, not a promise that tasks are safe to run
concurrently; a future executor must also account for shared resources and side
effects.

## Safety boundary

Planning is advisory. It does not execute skill instructions, call an LLM,
access a browser, read/write user project files, authorize tools, or perform
external side effects. A selected skill is a routing suggestion, not permission.
Approval and policy enforcement belong to later runtime layers.
