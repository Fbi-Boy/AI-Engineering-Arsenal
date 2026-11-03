# Agent Orchestration Patterns

## Choose an execution shape
- **Deterministic workflow:** known steps, strict order, application-owned branching, and predictable state transitions.
- **Single agent with tools:** bounded reasoning and tool selection within a constrained task.
- **Router and specialists:** a router assigns tasks to narrowly scoped specialists when task classes differ materially.
- **Sequential handoff:** one role completes a defined output before another role takes ownership.
- **Parallel specialists:** independent tasks run concurrently and are reconciled by a coordinator.
- **Human-in-the-loop:** the workflow pauses for review or approval before a gated action.

Complexity is justified only when it improves outcome quality, maintainability, speed, or safety.

## Handoff contract
For every handoff define:
- Why the current role is handing off.
- Receiving role and permitted responsibilities.
- Required input artifacts and provenance.
- Expected output schema and acceptance criteria.
- State ownership and cancellation behavior.
- How errors and incomplete work return to the coordinator.

Do not pass the entire conversation when a minimal structured task packet is sufficient.

## State model
Represent durable workflow state separately from conversational context:
- Task ID, status, owner, and timestamps.
- Current step and validated checkpoint.
- Input and output artifact references.
- Tool calls, approval decisions, and idempotency keys.
- Retry / compensation status.
- Cancellation and expiration state.

Define transitions such as pending, running, awaiting approval, blocked, completed, failed, cancelled, and expired. Prevent terminal or cancelled tasks from executing further actions.

## Bounded loops
Set limits for model turns, tool invocations, elapsed time, input / output tokens, external requests, and spend. Define when to ask the user, when to retry, and when to stop.

## Parallelism
Parallelize only independent work. Define shared-resource locking, output schema, conflict resolution, cancellation, and aggregation. Do not parallelize writes whose order affects data integrity without a concurrency design.
