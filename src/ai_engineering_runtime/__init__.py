"""Provider-neutral foundations for discovering, routing, planning, and executing agent tasks."""

from .executor import (
    ExecutionApproval,
    ExecutionEvent,
    ExecutionReport,
    TaskExecutionContext,
    execute_workflow,
)
from .models import RegistryIssue, RegistryReport, SkillManifest
from .planning import PlannedTask, TaskDraft, WorkflowPlan, plan_workflow
from .registry import load_registry
from .routing import (
    RouteCandidate,
    RouteDecision,
    RoutingConfig,
    route_from_registry,
    route_task,
)

__all__ = [
    "RegistryIssue",
    "RegistryReport",
    "SkillManifest",
    "RouteCandidate",
    "RouteDecision",
    "RoutingConfig",
    "TaskDraft",
    "PlannedTask",
    "WorkflowPlan",
    "ExecutionApproval",
    "ExecutionEvent",
    "ExecutionReport",
    "TaskExecutionContext",
    "load_registry",
    "route_from_registry",
    "route_task",
    "plan_workflow",
    "execute_workflow",
]
__version__ = "0.1.0"
