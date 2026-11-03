# State Models and Resumption

## Separate state categories
- **Execution state:** current task status, step, dependency, retry, approval, and cancellation.
- **Conversation history:** user / assistant exchanges and runtime continuation context.
- **Checkpoint:** validated intermediate outputs and state required to resume.
- **Artifact store:** documents, source diffs, reports, and other deliverables.
- **Audit log:** immutable or appropriately protected record of consequential events.
- **Preference memory:** user-authorized stable preferences with provenance and correction path.

Do not combine these merely because a runtime exposes one session object.

## Task state schema
A useful record may include task ID, owner / tenant, state version, status, current step, checkpoint reference, input and output artifact references, dependency versions, pending approval IDs, idempotency keys, event sequence, created / updated / expiry times, and cancellation flag.

## Resume model
When an execution pauses:
1. Persist validated state and exact interruption / pending action.
2. Persist the state version and artifact references.
3. Wait for the authorized event (approval, user input, tool result, or recovery).
4. Re-check identity, permissions, action arguments, expiry, and current resource state.
5. Resume from the same logical task and checkpoint.
6. Reconcile duplicate or uncertain side effects.
7. Mark completion only after output and postconditions are verified.

A paused run is not a completed run. An idle session alone does not prove the last task succeeded.

## Concurrency
Use optimistic version checks, leases, or compare-and-swap where appropriate. Define lease expiry and owner recovery. A stale worker must not overwrite newer state or execute a cancelled task.

## Event sourcing and projections
Where event replay is needed, record validated events with stable IDs and sequence numbers. The current-state projection can be rebuilt from events, but external side effects must not be blindly replayed. Use idempotency keys and external receipts.
