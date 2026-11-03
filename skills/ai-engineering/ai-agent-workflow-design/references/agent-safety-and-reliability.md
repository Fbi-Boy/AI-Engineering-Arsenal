# Agent Safety and Reliability

## Tool contract
Each tool should declare:
- Purpose and allowed task classes.
- Typed input and output schema.
- Identity / authorization requirements.
- Read versus write behavior.
- Reversibility and external impact.
- Timeout, retry, and cost limit.
- Idempotency and reconciliation strategy.
- Audit event and sensitive-data policy.

Enforce validation and permissions in trusted application code. A natural-language tool description is not an access-control mechanism.

## Approval tiers
Use risk-based controls:
- Read-only or reversible local actions may run within an approved scope.
- Changes to user data, external accounts, repositories, or cloud resources require explicit scope and appropriate review.
- Financial, public, destructive, credential, or irreversible actions require a strong confirmation step and execution-time authorization.

An approval should bind to the exact action, target, and relevant arguments. Changes to the action require renewed approval.

## Retries and side effects
- Use idempotency keys when the downstream system supports them.
- Distinguish "request failed" from "request outcome unknown".
- Reconcile uncertain outcomes before retrying non-idempotent actions.
- Use compensating actions only when their semantics are defined and safe.
- Never blindly repeat payment, publication, deletion, or messaging actions.

## Observability and privacy
Trace task boundaries, model / tool spans, handoffs, guardrail decisions, approvals, retries, and outcomes. Capture identifiers and sanitized status rather than secrets or full private payloads. Define retention, access, sampling, and incident review.
