import pytest

from ai_engineering_runtime.executor import (
    ExecutionApproval,
    execute_workflow,
)
from ai_engineering_runtime.models import SkillManifest
from ai_engineering_runtime.planning import TaskDraft, plan_workflow


SKILLS = (
    SkillManifest("api-design", "design REST APIs and contracts", "skills/api-design", "SKILL.md"),
    SkillManifest("database-design", "design database schemas and ERD", "skills/database-design", "SKILL.md"),
)
APPROVAL = ExecutionApproval("test-suite", "unit test execution")


def task(task_id, description, dependencies=()):
    return TaskDraft(task_id, description, tuple(dependencies), ("Output is reviewed",))


def make_plan(*tasks):
    return plan_workflow(tasks, SKILLS)


def handlers(api=None, database=None):
    return {
        "api-design": api or (lambda context: {"task": context.task_id}),
        "database-design": database or (lambda context: {"task": context.task_id}),
    }


def test_requires_approval_before_invoking_any_handler():
    called = []
    plan = make_plan(task("api", "design REST API"))
    report = execute_workflow(
        plan, {"api-design": lambda context: called.append(context.task_id)}
    )
    assert report.status == "awaiting_approval"
    assert called == []
    assert report.events[0].state == "pending"


def test_executes_tasks_in_dependency_order_and_passes_dependency_outputs():
    plan = make_plan(
        task("requirements", "design REST API"),
        task("contract", "design REST API contract", ("requirements",)),
    )
    seen = []

    def api(context):
        seen.append(context.task_id)
        if context.task_id == "contract":
            assert context.dependency_outputs["requirements"] == {"approved": True}
        return {"approved": True}

    report = execute_workflow(plan, {"api-design": api}, approval=APPROVAL)
    assert report.status == "completed"
    assert seen == ["requirements", "contract"]
    assert [event.state for event in report.events if event.task_id == "contract"] == [
        "pending", "running", "completed"
    ]


def test_failed_task_blocks_dependents_but_independent_task_continues():
    plan = make_plan(
        task("api", "design REST API"),
        task("contract", "design REST API contract", ("api",)),
        task("database", "design database schema"),
    )
    called = []

    def api(context):
        called.append(context.task_id)
        if context.task_id == "api":
            raise RuntimeError("simulated failure")
        return "ok"

    report = execute_workflow(plan, handlers(api=api), approval=APPROVAL)
    assert report.status == "failed"
    assert called == ["api", "database"]
    assert any(event.task_id == "contract" and event.state == "blocked" for event in report.events)
    assert "database" in report.outputs


def test_missing_handler_fails_preflight_without_running_anything():
    plan = make_plan(task("api", "design REST API"))
    called = []
    report = execute_workflow(
        plan, {"database-design": lambda context: called.append("called")},
        approval=APPROVAL,
    )
    assert report.status == "not_started"
    assert called == []
    assert "no handler registered" in report.issues[0]


def test_non_ready_plan_is_not_executed():
    plan = make_plan(task("unknown", "prepare a catering menu"))
    called = []
    report = execute_workflow(
        plan, {"api-design": lambda context: called.append("called")},
        approval=APPROVAL,
    )
    assert report.status == "not_started"
    assert called == []
    assert "must be ready" in report.issues[0]


def test_handler_error_is_recorded_without_aborting_independent_tasks():
    plan = make_plan(
        task("api", "design REST API"),
        task("database", "design database schema"),
    )

    def fail(_context):
        raise ValueError("bad handler input")

    report = execute_workflow(plan, handlers(api=fail), approval=APPROVAL)
    failed = [event for event in report.events if event.state == "failed"]
    assert len(failed) == 1
    assert "ValueError" in failed[0].detail
    assert "database" in report.outputs


def test_approval_requires_a_reason_and_approver():
    with pytest.raises(ValueError):
        ExecutionApproval("", "because")
    with pytest.raises(ValueError):
        ExecutionApproval("reviewer", " ")
