# Skill Invocation and Handoff Contract

## Handoff packet
Pass a minimal structured packet to each specialist:

| Field | Meaning |
| --- | --- |
| task_id / step_id | Stable parent and child identifiers |
| objective | One bounded task and observable outcome |
| scope | Included and excluded responsibilities |
| input_artifacts | URI / path, version, checksum where available, and provenance |
| constraints | Stack, policies, compatibility, security, and time / cost bounds |
| permissions | Exact allowed operations and targets |
| dependencies | Validated prerequisite step IDs |
| expected_output | Artifact type, location, schema, and required sections |
| acceptance | Observable criteria and validation method |
| stop_conditions | Ambiguity, risk, permission denial, or missing dependency |
| reporting | Required evidence, status, and unresolved decisions |

## Output packet
A specialist should return:
- task_id / step_id and status.
- artifact references and versions.
- summary of work performed.
- evidence and validation actually run.
- assumptions and unsupported claims.
- warnings, risks, and open questions.
- external actions attempted / completed, if any, with authorized evidence.
- recommended next skill or owner.

## Handoff validation
The orchestrator checks:
1. Required fields and output schema.
2. Artifact existence and accessibility in the active runtime.
3. Provenance and source version.
4. Acceptance criteria.
5. Security / privacy and scope compliance.
6. Consistency with upstream artifacts.
7. No unsupported PASS, approval, or completion claim.

## Repair loop
If validation fails, return a focused defect list to the producing skill. Specify the exact artifact, section, acceptance criterion, and evidence needed. Limit correction cycles. Escalate persistent disagreement to the owner rather than endlessly prompting.

## Ownership
The producing skill owns domain correctness of its artifact. The orchestrator owns routing, integration, and cross-artifact consistency. The project owner owns scope decisions and acceptance. Runtime code owns authentication and permission enforcement.
