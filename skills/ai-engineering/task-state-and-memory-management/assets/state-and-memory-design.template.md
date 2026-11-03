# Task State and Memory Design

## Context
- Application / runtime:
- Task types and lifetime:
- User / tenant / project model:
- Source-of-truth systems:

## Information inventory
| Category | Example fields | Owner / scope | Sensitivity | Retention | Source of truth |
| --- | --- | --- | --- | --- | --- |
| Execution state | | | | | |
| Conversation history | | | | | |
| Checkpoint / artifacts | | | | | |
| User / project memory | | | | | |
| Audit records | | | | | |

## Task state model
- State transitions:
- Terminal states:
- Cancellation behavior:
- Checkpoint schema / version:
- Resume and reconciliation:
- Concurrency / locking:

## Memory governance
- Consent / policy basis:
- Provenance and confidence:
- Correction / export:
- Deletion / revocation:
- Backup / cache / derived copy handling:

## Security and operations
- Authentication / authorization:
- Encryption and key ownership:
- Secret exclusion:
- Access audit:
- Recovery objectives:
- Monitoring / alerts:

## Validation
| Scenario | Expected result | Evidence |
| --- | --- | --- |
| Restart during work | | |
| Approval pause / resume | | |
| Duplicate event | | |
| Stale checkpoint | | |
| Access revocation | | |
| Deletion propagation | | |

## Open decisions
- Policy owner:
- Storage / runtime choice:
- Retention values:
- Migration / compatibility:
- Unverified assumptions:
