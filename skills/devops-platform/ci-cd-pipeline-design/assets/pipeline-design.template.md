# CI/CD Pipeline Design

## Repository and delivery context
- Repository / main stack:
- CI platform and runner:
- Deployment target / environment topology:
- Branch and release strategy:
- Owners and approval authority:

## Stage design
| Stage | Trigger | Jobs / commands | Inputs | Outputs / evidence | Gate |
| --- | --- | --- | --- | --- | --- |
| Change validation | | | | | |
| Tests | | | | | |
| Build | | | | | |
| Security / provenance | | | | | |
| Deploy / promote | | | | | |
| Post-deploy | | | | | |

## Workflow security
| Workflow / job | Token permissions | Secrets / identity | Trusted inputs | Approval |
| --- | --- | --- | --- | --- |
| | | | | |

## Artifact flow
- Artifact format and immutable identifier:
- Source commit and build metadata:
- Storage / retention:
- Verification / provenance:
- Promotion path:

## Reliability and recovery
- Concurrency policy:
- Health checks:
- Rollback / roll-forward:
- Failure notification / owner:
- Emergency path:

## Validation
| Check | PASS / FAIL / BLOCKED / NOT RUN | Evidence |
| --- | --- | --- |
| Workflow syntax | | |
| Static security review | | |
| Test / build execution | | |
| Deployment rehearsal | | |

## Open decisions
- Platform / runner:
- Permission approvals:
- Secret ownership:
- Environment protection:
- Costs / retention:
