"""Conservative synchronous execution for explicitly registered task handlers.

The executor never interprets SKILL.md instructions as code. Callers provide
trusted Python handlers explicitly and must provide an approval attestation.
This is an application-level opt-in, not authentication or a replacement for
the future permission and policy enforcement layer.
"""
from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable, Literal, Mapping

from .planning import WorkflowPlan


TaskState = Literal["pending", "running", "completed", "failed", "blocked"]
WorkflowExecutionStatus = Literal[
    "awaiting_approval", "not_started", "completed", "failed", "blocked"
]


@dataclass(frozen=True, slots=True)
class ExecutionApproval:
    """Caller attestation required before any handler is invoked.

    The runtime does not authenticate approver identity. Applications must
    obtain this object only after their own approval and authorization checks.
    """

    approved_by: str
    reason: str

    def __post_init__(self) -> None:
        if not self.approved_by.strip():
            raise ValueError("approved_by must not be empty")
        if not self.reason.strip():
            raise ValueError("approval reason must not be empty")


@dataclass(frozen=True, slots=True)
class TaskExecutionContext:
    """Read-only view of a task and outputs from completed dependencies."""

    task_id: str
    description: str
    acceptance_criteria: tuple[str, ...]
    dependency_outputs: Mapping[str, object]


TaskHandler = Callable[[TaskExecutionContext], object]


@dataclass(frozen=True, slots=True)
class ExecutionEvent:
    """One observable state transition for a task."""

    task_id: str
    state: TaskState
    detail: str


@dataclass(frozen=True, slots=True)
class ExecutionReport:
    """In-memory result of one synchronous workflow execution."""

    status: WorkflowExecutionStatus
    events: tuple[ExecutionEvent, ...]
    outputs: Mapping[str, object]
    issues: tuple[str, ...]


def _preflight(plan: WorkflowPlan, handlers: Mapping[str, TaskHandler]) -> tuple[str, ...]:
    issues: list[str] = []
    if plan.status != "ready":
        issues.append(f"workflow plan must be ready; received {plan.status!r}")
        return tuple(issues)
    if not plan.tasks:
        issues.append("workflow plan must contain at least one task")
        return tuple(issues)

    task_ids = [task.task_id for task in plan.tasks]
    if len(task_ids) != len(set(task_ids)):
        issues.append("workflow plan contains duplicate task IDs")
        return tuple(issues)

    expected = set(task_ids)
    if len(plan.execution_order) != len(expected) or set(plan.execution_order) != expected:
        issues.append("execution_order must contain every task ID exactly once")
        return tuple(issues)

    positions = {task_id: index for index, task_id in enumerate(plan.execution_order)}
    task_by_id = {task.task_id: task for task in plan.tasks}
    for task in plan.tasks:
        if task.route.selected is None:
            issues.append(f"task {task.task_id!r} has no selected skill")
            continue
        handler = handlers.get(task.route.selected.name)
        if not callable(handler):
            issues.append(
                f"no callable handler registered for skill {task.route.selected.name!r} "
                f"(task {task.task_id!r})"
            )
        for dependency in task.depends_on:
            if dependency not in expected:
                issues.append(
                    f"task {task.task_id!r} depends on unknown task {dependency!r}"
                )
            elif positions.get(dependency, len(expected)) >= positions[task.task_id]:
                issues.append(
                    f"dependency {dependency!r} must appear before task {task.task_id!r}"
                )

    return tuple(issues)


def execute_workflow(
    plan: WorkflowPlan,
    handlers: Mapping[str, TaskHandler],
    *,
    approval: ExecutionApproval | None = None,
) -> ExecutionReport:
    """Execute ready plans sequentially through explicitly registered handlers.

    A failed task blocks only its dependents; independent tasks continue.
    Handler exceptions are captured as failed task events. No handler is invoked
    unless a caller-supplied approval attestation is present and preflight passes.
    """
    pending_events = tuple(
        ExecutionEvent(task_id, "pending", "Waiting to be executed.")
        for task_id in plan.execution_order
    )

    if approval is None:
        return ExecutionReport(
            "awaiting_approval", pending_events, MappingProxyType({}),
            ("explicit ExecutionApproval is required before execution",),
        )

    issues = _preflight(plan, handlers)
    if issues:
        return ExecutionReport(
            "not_started", pending_events, MappingProxyType({}), issues
        )

    task_by_id = {task.task_id: task for task in plan.tasks}
    outputs: dict[str, object] = {}
    states: dict[str, TaskState] = {}
    events: list[ExecutionEvent] = list(pending_events)

    for task_id in plan.execution_order:
        task = task_by_id[task_id]
        blocked_by = tuple(
            dependency for dependency in task.depends_on
            if states.get(dependency) != "completed"
        )
        if blocked_by:
            states[task_id] = "blocked"
            events.append(ExecutionEvent(
                task_id, "blocked",
                "Dependencies did not complete: " + ", ".join(blocked_by),
            ))
            continue

        skill_name = task.route.selected.name  # guaranteed by preflight
        dependency_outputs = MappingProxyType({
            dependency: outputs[dependency] for dependency in task.depends_on
        })
        context = TaskExecutionContext(
            task_id=task.task_id,
            description=task.description,
            acceptance_criteria=task.acceptance_criteria,
            dependency_outputs=dependency_outputs,
        )
        events.append(ExecutionEvent(task_id, "running", f"Invoking registered handler for {skill_name}."))
        try:
            output = handlers[skill_name](context)
        except Exception as exc:  # handler boundary: preserve failure, do not crash the runner
            states[task_id] = "failed"
            events.append(ExecutionEvent(
                task_id, "failed", f"Handler raised {type(exc).__name__}: {exc}"
            ))
        else:
            states[task_id] = "completed"
            outputs[task_id] = output
            events.append(ExecutionEvent(task_id, "completed", "Handler completed successfully."))

    if any(state == "failed" for state in states.values()):
        status: WorkflowExecutionStatus = "failed"
    elif any(state == "blocked" for state in states.values()):
        status = "blocked"
    else:
        status = "completed"

    return ExecutionReport(
        status, tuple(events), MappingProxyType(dict(outputs)), ()
    )
