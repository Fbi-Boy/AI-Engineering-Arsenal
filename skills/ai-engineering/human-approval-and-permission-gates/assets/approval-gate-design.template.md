# Human Approval and Permission Gate Design

## Context and ownership
- Application / agent runtime:
- Policy authority:
- Approval owner(s):
- Audit owner:
- Applicable policy / standards:

## Action inventory
| Tool / action | Target scope | Side effect | Reversibility | Risk | Required control |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Authorization
- Actor identity:
- Role / attributes:
- Resource ownership / tenant checks:
- Policy engine / enforcement point:
- Deny behavior:

## Approval payload
- Human-readable purpose:
- Target and environment:
- Material arguments:
- Expected effects / data scope:
- Expiry:
- Approver eligibility:

## Lifecycle and execution
- Fingerprint / canonicalization:
- Policy version binding:
- One-time consumption:
- Revocation / cancellation:
- Execution-time revalidation:
- Idempotency / reconciliation:

## Audit and privacy
| Event | Required evidence | Redaction | Retention |
| --- | --- | --- | --- |
| Request | | | |
| Policy decision | | | |
| Approval decision | | | |
| Execution attempt / result | | | |

## Test matrix
| Case | Expected decision / behavior | Evidence |
| --- | --- | --- |
| Missing approval | | |
| Changed arguments | | |
| Expired / replayed approval | | |
| Role revoked while pending | | |
| Approval service unavailable | | |
| Duplicate execution | | |

## Open decisions
- Risk thresholds:
- Exception process:
- Independent approver policy:
- Unverified assumptions:
