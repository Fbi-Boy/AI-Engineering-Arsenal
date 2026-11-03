# Approval Lifecycle and Bypass Resistance

## Approval request contents
A request should display:
- Requester identity.
- Tool / operation and plain-language purpose.
- Exact target resource and environment.
- Material arguments and their human-readable effect.
- Data / records affected and expected external side effect.
- Risk tier, reversibility, and recovery information.
- Expiry and decision policy.

## Bind the decision
Associate approval with a canonical action record including:
- Unique action ID.
- Authenticated requester and approver identity.
- Tool name and version.
- Target and resource identifier.
- Canonicalized material arguments or secure digest.
- Relevant resource version / precondition.
- Policy version and decision timestamp.
- Expiry and one-time consumption status.

Do not put raw secrets in approval records. Ensure canonicalization cannot collapse materially different actions into the same digest.

## Lifecycle
pending → approved / rejected / expired / revoked → consumed / execution_failed / completed.

A rejection is terminal for that action. A changed argument, target, actor, policy version, resource state, or expired decision requires a new review. Use an idempotent decision endpoint and an atomic consume operation to prevent replay.

## Execution-time checks
Immediately before side effect:
1. Authenticate the current caller / worker identity.
2. Re-evaluate resource and operation permission.
3. Verify approval status, approver authority, expiry, and exact action fingerprint.
4. Verify target resource version / preconditions.
5. Atomically consume the approval if permitted.
6. Execute with idempotency key where supported.
7. Record the actual outcome independently.

## Bypass tests
Test direct endpoint calls without UI, argument tampering, alternate target IDs, role downgrade during wait, approval reuse, replay after expiry, duplicate callbacks, stale resource state, queue execution after cancellation, and approval-service timeout.

## Audit events
Record request, policy result, approval decision, execution attempt, and execution result as distinct events. Redact sensitive arguments and apply retention / access policy.
