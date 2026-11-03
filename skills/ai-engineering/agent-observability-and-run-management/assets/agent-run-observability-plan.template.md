# Agent Run Observability Plan

## Runtime and workflow
- Runtime / SDK version:
- Workflow / agent:
- Service owner:
- Data classification:
- Run-state source of truth:

## Lifecycle and identifiers
- Canonical states:
- Event source:
- Run / task / step IDs:
- Correlation / trace context:
- Event ordering / deduplication:
- Pause / resume / cancel:

## Trace design
| Span | Parent | Key attributes | Redaction / sampling |
| --- | --- | --- | --- |
| Root run | | | |
| Skill / specialist | | | |
| Model call | | | |
| Tool call | | | |
| Approval / guardrail | | | |
| Validation | | | |

## Metrics
| Metric | Unit | Labels | Cardinality risk | Owner / alert |
| --- | --- | --- | --- | --- |
| Run outcome | | | | |
| Step duration | | | | |
| Tool error rate | | | | |
| Approval wait | | | | |
| Usage / cost | | | | |

## Privacy and audit
- Redaction:
- Trace access:
- Retention / deletion:
- Audit system:
- Sensitive fields excluded:

## Operations
- Dashboard:
- Alert conditions:
- Runbooks:
- Reconciliation procedure:
- Incident owner:

## Validation
| Scenario | Expected status / evidence | Result |
| --- | --- | --- |
| Stream disconnect | | |
| Duplicate / out-of-order event | | |
| Approval wait and resume | | |
| Cancellation with queued action | | |
| Secret redaction | | |
| Run complete but artifact invalid | | |

## Open decisions
- SLO / alert thresholds:
- Runtime-specific event mapping:
- Retention period:
- Instrumentation gaps:
