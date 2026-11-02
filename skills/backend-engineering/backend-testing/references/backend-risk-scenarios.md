# Backend Risk Scenarios

## Authorization and data isolation
Consider:
- Anonymous request to protected operation.
- Authenticated user without the required role / scope.
- User accessing another user's resource.
- Cross-tenant identifier substitution.
- Mass assignment of protected fields.
- Permission change or ownership transfer during a workflow.
- Expired or revoked credentials.

For denied behavior, assert both the expected response and the absence of unauthorized state changes.

## Integrity and state
Consider:
- Invalid state transition.
- Duplicate request and retry.
- Concurrent modification and stale version.
- Partial writes and transaction rollback.
- Missing related record and constraint violation.
- Boundary numeric values, decimal precision, and timezone changes.
- Pagination stability and large result limits.

## External side effects
Consider:
- Provider timeout before acknowledgement.
- Provider accepted a request but response was lost.
- Duplicate webhook delivery.
- Invalid signature or untrusted callback.
- Queue retry and dead-letter handling.
- Out-of-order events and replay.
- Compensation when one of multiple operations fails.

Make retry semantics explicit. A test must not assume a non-idempotent operation is safe to repeat.

## API contracts
Check:
- Required and optional fields.
- Type, range, format, and unknown-field behavior.
- Stable error structure and status semantics.
- Authentication and authorization behavior.
- Version compatibility and backward-compatible changes.
- No secret or internal stack trace in public responses.

## Test prioritization
Prioritize failures that could expose data across users, corrupt state, duplicate a charge, lose a durable event, bypass authorization, or break a critical consumer contract.
