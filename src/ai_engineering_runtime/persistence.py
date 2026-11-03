"""SQLite-backed durable workflow state with conservative task claiming.

This module stores metadata and JSON-compatible outputs only. It never uses
pickle, executes handlers, or automatically retries interrupted work.
"""
from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
from typing import Any, Mapping
from uuid import uuid4

from .planning import WorkflowPlan

_SCHEMA_VERSION = 1

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _json_value(value: Any, path: str = "$") -> None:
    """Reject values JSON would silently coerce or encode non-portably."""
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if value != value or value in (float("inf"), float("-inf")):
            raise ValueError(f"non-finite number at {path} is not JSON-safe")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _json_value(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"object key at {path} must be a string")
            _json_value(item, f"{path}.{key}")
        return
    raise ValueError(f"unsupported JSON value at {path}: {type(value).__name__}")


def _encode_json(value: Any) -> str:
    _json_value(value)
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True)


def _plan_payload(plan: WorkflowPlan) -> dict[str, Any]:
    tasks = []
    for task in plan.tasks:
        selected = task.route.selected
        tasks.append({
            "task_id": task.task_id,
            "description": task.description,
            "depends_on": list(task.depends_on),
            "acceptance_criteria": list(task.acceptance_criteria),
            "route": {
                "status": task.route.status,
                "selected": None if selected is None else {
                    "name": selected.name,
                    "description": selected.description,
                    "directory": selected.directory,
                    "manifest_path": selected.manifest_path,
                },
                "candidates": [{
                    "skill": {
                        "name": candidate.skill.name,
                        "description": candidate.skill.description,
                        "directory": candidate.skill.directory,
                        "manifest_path": candidate.skill.manifest_path,
                    },
                    "score": candidate.score,
                    "matched_terms": list(candidate.matched_terms),
                    "reasons": list(candidate.reasons),
                } for candidate in task.route.candidates],
                "query_terms": list(task.route.query_terms),
                "explanation": task.route.explanation,
            },
        })
    return {
        "status": plan.status,
        "tasks": tasks,
        "execution_order": list(plan.execution_order),
        "parallel_groups": [list(group) for group in plan.parallel_groups],
        "issues": list(plan.issues),
        "explanation": plan.explanation,
    }


@dataclass(frozen=True, slots=True)
class StoredTask:
    task_id: str
    state: str
    metadata: Mapping[str, Any]
    output: Any
    error: str | None


@dataclass(frozen=True, slots=True)
class StoredEvent:
    sequence: int
    task_id: str
    state: str
    detail: str
    created_at: str


@dataclass(frozen=True, slots=True)
class WorkflowSnapshot:
    workflow_id: str
    status: str
    plan: Mapping[str, Any]
    tasks: tuple[StoredTask, ...]
    events: tuple[StoredEvent, ...]
    created_at: str
    updated_at: str


class SQLiteStateStore:
    """Explicit opt-in SQLite store for workflow snapshots and task transitions.

    Each public operation opens its own connection and uses a transaction.
    A task can be claimed only once while pending. A process crash after a
    claim leaves the task running; call recover_interrupted() to mark it
    interrupted for manual reconciliation, never to silently retry it.
    """

    def __init__(self, database: str | Path, *, busy_timeout_ms: int = 5000):
        if str(database) == ":memory:":
            raise ValueError("use a file-backed database; in-memory databases cannot survive per-operation connections")
        if busy_timeout_ms < 0:
            raise ValueError("busy_timeout_ms must be non-negative")
        self.database = str(database)
        self.busy_timeout_ms = busy_timeout_ms
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(
            self.database, timeout=self.busy_timeout_ms / 1000,
            isolation_level=None,
        )
        connection.row_factory = sqlite3.Row
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute(f"PRAGMA busy_timeout = {self.busy_timeout_ms}")
        if self.database != ":memory:":
            connection.execute("PRAGMA journal_mode = WAL")
        return connection

    @contextmanager
    def _session(self):
        connection = self._connect()
        try:
            yield connection
        finally:
            connection.close()

    def _initialize(self) -> None:
        with self._session() as connection:
            version = connection.execute("PRAGMA user_version").fetchone()[0]
            if version > _SCHEMA_VERSION:
                raise RuntimeError(
                    f"database schema version {version} is newer than supported {_SCHEMA_VERSION}"
                )
            if version == 0:
                try:
                    connection.executescript("""
                        BEGIN IMMEDIATE;
                        CREATE TABLE workflows (
                            workflow_id TEXT PRIMARY KEY,
                            status TEXT NOT NULL,
                            plan_json TEXT NOT NULL,
                            created_at TEXT NOT NULL,
                            updated_at TEXT NOT NULL
                        );
                        CREATE TABLE tasks (
                            workflow_id TEXT NOT NULL,
                            task_id TEXT NOT NULL,
                            state TEXT NOT NULL,
                            metadata_json TEXT NOT NULL,
                            output_json TEXT,
                            error TEXT,
                            PRIMARY KEY (workflow_id, task_id),
                            FOREIGN KEY (workflow_id) REFERENCES workflows(workflow_id)
                                ON DELETE CASCADE
                        );
                        CREATE TABLE events (
                            sequence INTEGER PRIMARY KEY AUTOINCREMENT,
                            workflow_id TEXT NOT NULL,
                            task_id TEXT NOT NULL,
                            state TEXT NOT NULL,
                            detail TEXT NOT NULL,
                            created_at TEXT NOT NULL,
                            FOREIGN KEY (workflow_id, task_id)
                                REFERENCES tasks(workflow_id, task_id) ON DELETE CASCADE
                        );
                        CREATE INDEX events_workflow_sequence
                            ON events(workflow_id, sequence);
                    """)
                    connection.execute(f"PRAGMA user_version = {_SCHEMA_VERSION}")
                    connection.execute("COMMIT")
                except Exception:
                    connection.execute("ROLLBACK")
                    raise

    def create_workflow(self, plan: WorkflowPlan, workflow_id: str | None = None) -> str:
        if plan.status != "ready" or not plan.tasks:
            raise ValueError("only non-empty ready workflow plans can be persisted")
        identifier = workflow_id or str(uuid4())
        if not identifier.strip():
            raise ValueError("workflow_id must not be empty")
        plan_json = _encode_json(_plan_payload(plan))
        created = _now()
        with self._session() as connection:
            connection.execute("BEGIN IMMEDIATE")
            try:
                connection.execute(
                    "INSERT INTO workflows(workflow_id,status,plan_json,created_at,updated_at) "
                    "VALUES(?,?,?,?,?)",
                    (identifier, "pending", plan_json, created, created),
                )
                for task in plan.tasks:
                    metadata = {
                        "description": task.description,
                        "depends_on": list(task.depends_on),
                        "acceptance_criteria": list(task.acceptance_criteria),
                        "selected_skill": task.route.selected.name,
                    }
                    connection.execute(
                        "INSERT INTO tasks(workflow_id,task_id,state,metadata_json) VALUES(?,?,?,?)",
                        (identifier, task.task_id, "pending", _encode_json(metadata)),
                    )
                    connection.execute(
                        "INSERT INTO events(workflow_id,task_id,state,detail,created_at) "
                        "VALUES(?,?,?,?,?)",
                        (identifier, task.task_id, "pending", "Workflow created.", created),
                    )
                connection.execute("COMMIT")
            except Exception:
                connection.execute("ROLLBACK")
                raise
        return identifier

    def claim_task(self, workflow_id: str, task_id: str) -> bool:
        """Atomically claim a pending task whose dependencies are completed."""
        now = _now()
        with self._session() as connection:
            connection.execute("BEGIN IMMEDIATE")
            try:
                task = connection.execute(
                    "SELECT state, metadata_json FROM tasks WHERE workflow_id=? AND task_id=?",
                    (workflow_id, task_id),
                ).fetchone()
                if task is None or task["state"] != "pending":
                    connection.execute("ROLLBACK")
                    return False
                metadata = json.loads(task["metadata_json"])
                for dependency in metadata["depends_on"]:
                    row = connection.execute(
                        "SELECT state FROM tasks WHERE workflow_id=? AND task_id=?",
                        (workflow_id, dependency),
                    ).fetchone()
                    if row is None or row["state"] != "completed":
                        connection.execute("ROLLBACK")
                        return False
                connection.execute(
                    "UPDATE tasks SET state='running' WHERE workflow_id=? AND task_id=? AND state='pending'",
                    (workflow_id, task_id),
                )
                connection.execute(
                    "INSERT INTO events(workflow_id,task_id,state,detail,created_at) VALUES(?,?,?,?,?)",
                    (workflow_id, task_id, "running", "Task claimed for execution.", now),
                )
                connection.execute(
                    "UPDATE workflows SET status='in_progress',updated_at=? WHERE workflow_id=?",
                    (now, workflow_id),
                )
                connection.execute("COMMIT")
                return True
            except Exception:
                connection.execute("ROLLBACK")
                raise

    def complete_task(self, workflow_id: str, task_id: str, output: Any) -> None:
        output_json = _encode_json(output)  # validate before opening a write transaction
        self._finish_task(workflow_id, task_id, "completed", output_json, None)

    def fail_task(self, workflow_id: str, task_id: str, error: str) -> None:
        if not isinstance(error, str) or not error.strip():
            raise ValueError("error must be a non-empty string")
        self._finish_task(workflow_id, task_id, "failed", None, error)

    def _finish_task(
        self, workflow_id: str, task_id: str, state: str,
        output_json: str | None, error: str | None,
    ) -> None:
        now = _now()
        with self._session() as connection:
            connection.execute("BEGIN IMMEDIATE")
            try:
                cursor = connection.execute(
                    "UPDATE tasks SET state=?,output_json=?,error=? "
                    "WHERE workflow_id=? AND task_id=? AND state='running'",
                    (state, output_json, error, workflow_id, task_id),
                )
                if cursor.rowcount != 1:
                    raise ValueError("task must be in running state before it can finish")
                detail = "Task completed." if state == "completed" else f"Task failed: {error}"
                connection.execute(
                    "INSERT INTO events(workflow_id,task_id,state,detail,created_at) VALUES(?,?,?,?,?)",
                    (workflow_id, task_id, state, detail, now),
                )
                states = [row[0] for row in connection.execute(
                    "SELECT state FROM tasks WHERE workflow_id=?", (workflow_id,)
                )]
                if all(item == "completed" for item in states):
                    workflow_state = "completed"
                elif any(item == "failed" for item in states):
                    workflow_state = "failed"
                else:
                    workflow_state = "in_progress"
                connection.execute(
                    "UPDATE workflows SET status=?,updated_at=? WHERE workflow_id=?",
                    (workflow_state, now, workflow_id),
                )
                connection.execute("COMMIT")
            except Exception:
                connection.execute("ROLLBACK")
                raise

    def recover_interrupted(self, workflow_id: str | None = None) -> int:
        """Mark orphaned running tasks interrupted; never requeue side effects."""
        now = _now()
        changed = 0
        with self._session() as connection:
            connection.execute("BEGIN IMMEDIATE")
            try:
                query = "SELECT workflow_id,task_id FROM tasks WHERE state='running'"
                parameters: tuple[str, ...] = ()
                if workflow_id is not None:
                    query += " AND workflow_id=?"
                    parameters = (workflow_id,)
                rows = connection.execute(query, parameters).fetchall()
                for row in rows:
                    connection.execute(
                        "UPDATE tasks SET state='interrupted',error=? "
                        "WHERE workflow_id=? AND task_id=? AND state='running'",
                        ("Execution outcome unknown after process interruption.", row["workflow_id"], row["task_id"]),
                    )
                    connection.execute(
                        "INSERT INTO events(workflow_id,task_id,state,detail,created_at) VALUES(?,?,?,?,?)",
                        (row["workflow_id"], row["task_id"], "interrupted",
                         "Process interruption detected; manual reconciliation required.", now),
                    )
                    connection.execute(
                        "UPDATE workflows SET status='needs_reconciliation',updated_at=? WHERE workflow_id=?",
                        (now, row["workflow_id"]),
                    )
                    changed += 1
                connection.execute("COMMIT")
            except Exception:
                connection.execute("ROLLBACK")
                raise
        return changed

    def load_workflow(self, workflow_id: str) -> WorkflowSnapshot | None:
        with self._session() as connection:
            workflow = connection.execute(
                "SELECT * FROM workflows WHERE workflow_id=?", (workflow_id,)
            ).fetchone()
            if workflow is None:
                return None
            task_rows = connection.execute(
                "SELECT * FROM tasks WHERE workflow_id=? ORDER BY rowid", (workflow_id,)
            ).fetchall()
            event_rows = connection.execute(
                "SELECT * FROM events WHERE workflow_id=? ORDER BY sequence", (workflow_id,)
            ).fetchall()
        tasks = tuple(StoredTask(
            row["task_id"], row["state"], json.loads(row["metadata_json"]),
            None if row["output_json"] is None else json.loads(row["output_json"]),
            row["error"],
        ) for row in task_rows)
        events = tuple(StoredEvent(
            row["sequence"], row["task_id"], row["state"], row["detail"], row["created_at"]
        ) for row in event_rows)
        return WorkflowSnapshot(
            workflow["workflow_id"], workflow["status"], json.loads(workflow["plan_json"]),
            tasks, events, workflow["created_at"], workflow["updated_at"],
        )
