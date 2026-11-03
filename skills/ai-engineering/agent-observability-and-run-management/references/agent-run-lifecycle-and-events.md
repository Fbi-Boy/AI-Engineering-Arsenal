# Agent Run Lifecycle and Events

## Lifecycle model
Common states include:
- **queued:** accepted but not yet scheduled.
- **running:** work is actively executing.
- **awaiting_input:** user or external input is required.
- **awaiting_approval:** a defined action is paused for review.
- **resuming:** a previously paused task is continuing.
- **completed:** runtime execution ended; verify deliverable acceptance separately.
- **failed:** execution ended with an error.
- **cancelled:** requested / authorized cancellation took effect.
- **timed_out:** a defined time budget expired.
- **expired:** resumable state or approval is no longer valid.

Use runtime-specific names only when their semantics are confirmed. Keep a mapping to the application's canonical status model.

## Event envelope
A useful event envelope may include:
- event_id and event_type.
- run_id, task_id, step_id, parent_step_id.
- trace_id and span_id where supported.
- sequence number / state version.
- occurred_at and received_at.
- actor / service identity.
- status, reason code, and outcome.
- artifact or approval reference.
- redaction / classification metadata.

Do not place sensitive payloads into event metadata.

## Event handling
- Treat events as potentially duplicated, delayed, or delivered out of order.
- Deduplicate by stable event ID or idempotency key.
- Use sequence / state version to reject stale transitions.
- Reconcile against an authoritative run-state store after a gap.
- Do not infer success from event absence or a quiet stream.
- Preserve a separate record of in-flight external side effects.

## Pause, resume, and cancellation
An approval pause is intentional. Preserve the interruption and resumable state. Resume the same logical task after a decision rather than creating a duplicate task. On cancellation, revoke pending actions and ensure workers check cancellation immediately before any new side effect.

## Progress semantics
Derive progress from accepted tasks and their verified outputs. Report counts or named milestones with a clear denominator. Do not invent a smooth percentage from token count, elapsed time, or spinner activity. A completed runtime turn can still leave the requested business outcome incomplete.
