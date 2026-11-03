"""Deterministic multi-skill workflow planning over explicit task drafts.

This module validates task dependencies and routes each task to existing skill
metadata. It does not decompose free-form requests, execute skills, or authorize
external actions; task drafts may be authored by a user or a future model adapter.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Sequence

from .models import SkillManifest
from .routing import RouteDecision, RoutingConfig, route_task


@dataclass(frozen=True, slots=True)
class TaskDraft:
    """One explicit unit of work supplied to the planner."""

    task_id: str
    description: str
    depends_on: tuple[str, ...] = ()
    acceptance_criteria: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class PlannedTask:
    """A validated task plus its advisory skill-routing decision."""

    task_id: str
    description: str
    depends_on: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    route: RouteDecision


@dataclass(frozen=True, slots=True)
class WorkflowPlan:
    """Plan result; only ready plans have a complete executable ordering."""

    status: Literal["ready", "needs_clarification", "invalid"]
    tasks: tuple[PlannedTask, ...]
    execution_order: tuple[str, ...]
    parallel_groups: tuple[tuple[str, ...], ...]
    issues: tuple[str, ...]
    explanation: str


def plan_workflow(
    drafts: Sequence[TaskDraft],
    skills: Sequence[SkillManifest],
    routing_config: RoutingConfig | None = None,
) -> WorkflowPlan:
    """Validate a task DAG, route each task, and compute stable parallel waves."""
    issues: list[str] = []
    ids = [draft.task_id for draft in drafts]
    if not drafts:
        return WorkflowPlan("invalid", (), (), (), ("workflow must contain at least one task",),
                            "No tasks were supplied.")

    seen: set[str] = set()
    for draft in drafts:
        if not draft.task_id or draft.task_id.strip() != draft.task_id:
            issues.append(f"task id must be non-empty and have no surrounding whitespace: {draft.task_id!r}")
        if draft.task_id in seen:
            issues.append(f"duplicate task id: {draft.task_id}")
        seen.add(draft.task_id)
        if not draft.description.strip():
            issues.append(f"task {draft.task_id!r} has an empty description")
        if not draft.acceptance_criteria or any(not item.strip() for item in draft.acceptance_criteria):
            issues.append(f"task {draft.task_id!r} must have non-empty acceptance criteria")
        if len(set(draft.depends_on)) != len(draft.depends_on):
            issues.append(f"task {draft.task_id!r} repeats a dependency")
        if draft.task_id in draft.depends_on:
            issues.append(f"task {draft.task_id!r} cannot depend on itself")
        for dependency in draft.depends_on:
            if dependency not in ids:
                issues.append(f"task {draft.task_id!r} depends on unknown task {dependency!r}")

    if issues:
        return WorkflowPlan("invalid", (), (), (), tuple(issues),
                            "Task definitions or dependency references are invalid.")

    by_id = {draft.task_id: draft for draft in drafts}
    remaining = set(by_id)
    completed: set[str] = set()
    waves: list[tuple[str, ...]] = []
    while remaining:
        ready = tuple(
            draft.task_id for draft in drafts
            if draft.task_id in remaining and set(draft.depends_on) <= completed
        )
        if not ready:
            cycle_members = ", ".join(sorted(remaining))
            return WorkflowPlan(
                "invalid", (), (), (),
                (f"dependency cycle detected among: {cycle_members}",),
                "The dependency graph contains a cycle and cannot be ordered.",
            )
        waves.append(ready)
        completed.update(ready)
        remaining.difference_update(ready)

    planned: list[PlannedTask] = []
    needs_clarification = False
    for draft in drafts:
        decision = route_task(draft.description, list(skills), routing_config)
        if decision.status != "selected":
            needs_clarification = True
        planned.append(PlannedTask(
            draft.task_id, draft.description, draft.depends_on,
            draft.acceptance_criteria, decision,
        ))

    order = tuple(task_id for wave in waves for task_id in wave)
    status: Literal["ready", "needs_clarification"] = (
        "needs_clarification" if needs_clarification else "ready"
    )
    explanation = (
        "Dependency graph is valid; one or more tasks need skill-routing clarification."
        if needs_clarification else
        "All tasks have a selected skill and the dependency graph is valid."
    )
    return WorkflowPlan(status, tuple(planned), order, tuple(waves), (), explanation)
