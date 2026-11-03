# Persistent workflow state v0.1

## Scope

The optional `SQLiteStateStore` persists a ready workflow plan, task metadata,
JSON-compatible task outputs, and an append-only state-transition history.
It uses Python's standard-library `sqlite3`; no third-party runtime dependency
is added. Persistence is opt-in: constructing and calling the store are explicit
application actions. The executor does not silently open a database or persist
anything.

## Basic use

```python
from ai_engineering_runtime import SQLiteStateStore

store = SQLiteStateStore("var/aea-state.sqlite3")
workflow_id = store.create_workflow(ready_plan, workflow_id="build-api-001")

if store.claim_task(workflow_id, "requirements"):
    # Invoke the already-authorized handler in the application.
    result = {"artifact": "requirements.md", "approved": True}
    store.complete_task(workflow_id, "requirements", result)

snapshot = store.load_workflow(workflow_id)
```

A task can be claimed only while it is `pending`, and only after every declared
dependency is `completed`. The claim is serialized in a SQLite
`BEGIN IMMEDIATE` transaction. Repeated claims return `False`; they do not
invoke a handler. A task must be `running` before `complete_task` or
`fail_task` can transition it.

## Serialization and schema

Only JSON-safe values are accepted for outputs: null, strings, booleans,
integers, finite floats, lists, and dictionaries with string keys. Tuples,
custom objects, non-string keys, NaN, and infinities are rejected before the
database is changed. The store deliberately does not use `pickle`.

Schema version is tracked with SQLite `PRAGMA user_version`. Version 1
creates workflow, task, and event tables with foreign keys and an event index.
The store uses parameterized SQL, a configurable busy timeout, and WAL mode
for file-backed databases. Keep the database file in an application-controlled
directory with appropriate filesystem permissions and backups.

## Restart and interruption policy

After process restart, call `load_workflow(workflow_id)` to inspect saved
workflow/task state and history. Call `recover_interrupted()` during an
application-controlled recovery procedure to change any persisted `running`
tasks to `interrupted` and the corresponding workflow to
`needs_reconciliation`.

Interrupted work is **not** returned to `pending` and is never automatically
retried. A process may have stopped after an external side effect occurred but
before its result was committed. An operator or application-specific
reconciliation process must determine the real-world outcome before deciding
what to do next.

## Guarantees and limitations

SQLite transactions prevent two concurrent callers from successfully claiming
the same pending task. They do not provide exactly-once execution of external
side effects. A crash between a handler's external action and recording its
result leaves an unknown outcome. Design handlers to be idempotent where
possible and use external idempotency keys or reconciliation for side effects.

This release is a persistence primitive, not automatic executor integration.
Applications explicitly coordinate `claim_task`, handler invocation, and
`complete_task`/`fail_task`. The store does not authenticate users, enforce
permissions, sandbox handlers, encrypt database contents, retry work, or
provide distributed locking across multiple database files.
