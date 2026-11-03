import json
import sqlite3

import pytest

from ai_engineering_runtime.models import SkillManifest
from ai_engineering_runtime.persistence import SQLiteStateStore
from ai_engineering_runtime.planning import TaskDraft, WorkflowPlan, plan_workflow


SKILLS = (
    SkillManifest("api-design", "design REST APIs and contracts", "skills/api-design", "SKILL.md"),
    SkillManifest("database-design", "design database schemas and ERD", "skills/database-design", "SKILL.md"),
)


def make_plan():
    return plan_workflow((
        TaskDraft("requirements", "design REST API", (), ("Reviewed output",)),
        TaskDraft("contract", "design REST API contract", ("requirements",), ("Reviewed output",)),
    ), SKILLS)


def test_create_and_restore_workflow_with_task_metadata(tmp_path):
    store = SQLiteStateStore(tmp_path / "state.sqlite3")
    workflow_id = store.create_workflow(make_plan(), "workflow-001")

    restored = store.load_workflow(workflow_id)
    assert restored is not None
    assert restored.status == "pending"
    assert restored.plan["execution_order"] == ["requirements", "contract"]
    assert [task.task_id for task in restored.tasks] == ["requirements", "contract"]
    assert all(task.state == "pending" for task in restored.tasks)
    assert len(restored.events) == 2


def test_claim_and_complete_persist_output_and_transition_history(tmp_path):
    store = SQLiteStateStore(tmp_path / "state.sqlite3")
    workflow_id = store.create_workflow(make_plan())
    assert store.claim_task(workflow_id, "requirements")
    store.complete_task(workflow_id, "requirements", {"artifact": "api.md", "checks": [True, 3]})

    restored = store.load_workflow(workflow_id)
    assert restored is not None
    task = restored.tasks[0]
    assert task.state == "completed"
    assert task.output == {"artifact": "api.md", "checks": [True, 3]}
    assert [event.state for event in restored.events if event.task_id == "requirements"] == [
        "pending", "running", "completed"
    ]
    assert not store.claim_task(workflow_id, "requirements")


def test_duplicate_claim_and_claim_before_dependency_completion_are_rejected(tmp_path):
    store = SQLiteStateStore(tmp_path / "state.sqlite3")
    workflow_id = store.create_workflow(make_plan())
    assert not store.claim_task(workflow_id, "contract")
    assert store.claim_task(workflow_id, "requirements")
    assert not store.claim_task(workflow_id, "requirements")


def test_interrupted_running_task_is_not_automatically_retried(tmp_path):
    store = SQLiteStateStore(tmp_path / "state.sqlite3")
    workflow_id = store.create_workflow(make_plan())
    assert store.claim_task(workflow_id, "requirements")

    assert store.recover_interrupted(workflow_id) == 1
    restored = store.load_workflow(workflow_id)
    assert restored is not None
    assert restored.status == "needs_reconciliation"
    assert restored.tasks[0].state == "interrupted"
    assert not store.claim_task(workflow_id, "requirements")
    assert any(event.state == "interrupted" for event in restored.events)


@pytest.mark.parametrize("bad_output", [
    {"not-json": object()},
    {1: "non-string key"},
    float("nan"),
    float("inf"),
    (1, 2),
])
def test_unsupported_output_is_rejected_before_task_transition(tmp_path, bad_output):
    store = SQLiteStateStore(tmp_path / "state.sqlite3")
    workflow_id = store.create_workflow(make_plan())
    assert store.claim_task(workflow_id, "requirements")

    with pytest.raises(ValueError):
        store.complete_task(workflow_id, "requirements", bad_output)

    restored = store.load_workflow(workflow_id)
    assert restored is not None
    assert restored.tasks[0].state == "running"


def test_failed_transaction_rolls_back_workflow_and_partial_task_rows(tmp_path):
    from dataclasses import replace

    plan = make_plan()
    duplicated = replace(plan, tasks=(plan.tasks[0], plan.tasks[0]))
    store = SQLiteStateStore(tmp_path / "state.sqlite3")

    with pytest.raises(sqlite3.IntegrityError):
        store.create_workflow(duplicated, "must-rollback")

    assert store.load_workflow("must-rollback") is None


def test_schema_version_zero_database_is_migrated(tmp_path):
    database = tmp_path / "legacy.sqlite3"
    with sqlite3.connect(database) as connection:
        connection.execute("PRAGMA user_version = 0")

    SQLiteStateStore(database)
    with sqlite3.connect(database) as connection:
        assert connection.execute("PRAGMA user_version").fetchone()[0] == 1
        names = {row[0] for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )}
    assert {"workflows", "tasks", "events"} <= names
