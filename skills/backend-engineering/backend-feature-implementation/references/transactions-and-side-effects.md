# Transactions, Consistency, and External Side Effects

## Keep the consistency boundary explicit

A database transaction can make a group of writes atomic within one transactional database. It does not automatically include a remote API, email provider, payment gateway, or message broker.

Before coding, identify:
- Which records must change together?
- Which invariants must never be partially applied?
- Which external side effects occur?
- What happens when an external call succeeds but the local transaction fails?
- What happens when the local write succeeds but the response is lost?
- Can a request be retried safely?

## Transaction scope

- Keep transactions focused and bounded.
- Avoid holding locks while waiting on slow or unreliable external networks unless there is a justified design.
- Use appropriate isolation and concurrency controls for the domain.
- Handle commit and rollback failures.
- Ensure tests verify atomicity and invariant preservation.

## Idempotency

For a retryable operation, define:
- The operation's natural idempotency.
- Key scope and format, where an explicit key is needed.
- Key retention period.
- Same key with same payload behavior.
- Same key with conflicting payload behavior.
- Concurrent duplicate handling.
- What response is returned when the original operation is already complete.

Do not assume a request is safe to retry just because it is an HTTP POST or a job message.

## Outbox and durable handoff

When a local state change must reliably produce an event:
1. Store the domain change and an outbox record in the same transaction.
2. A separate dispatcher publishes the event.
3. Mark publication progress and handle retry / duplicate delivery.
4. Consumers process messages idempotently.
5. Monitor backlog and failed delivery.

Use this pattern only when it fits the existing architecture and delivery guarantees.

## Sagas and compensation

A multi-service workflow may not have one global ACID transaction. Model:
- Each local step.
- Durable progress state.
- Failure point.
- Compensation or forward recovery.
- Idempotency of each step.
- Manual intervention conditions.

Compensation is a business action, not always a perfect reversal. For example, a refund may be a new transaction rather than deleting an original charge.

## Background jobs

Distinguish:
- Accepted / queued.
- Started / processing.
- Succeeded.
- Failed / retryable.
- Failed permanently / dead-lettered.
- Canceled where supported.

An API response acknowledging a queued task does not prove that the job has completed.
