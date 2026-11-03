# Dependency Graphs and Critical Path

## Task model
Each node should identify:
- Stable task ID.
- Bounded objective and accountable owner.
- Input artifacts and required versions.
- Output artifact and location.
- Acceptance criteria and validation method.
- Dependencies and gate conditions.
- Risk classification, permissions, and stop conditions.
- Estimated effort / duration and confidence when evidence exists.

## Dependency edges
An edge A → B means B requires a validated output or decision from A. Do not add edges merely because tasks are related. State the exact artifact or decision that releases the dependency.

Prefer a directed acyclic graph for the normal execution plan. If work requires iteration, model an explicit loop with:
- Maximum number of attempts.
- Entry and exit criteria.
- Owner for retry decision.
- State preserved between attempts.
- Escalation when the limit is reached.

## Critical path
The critical path is the longest dependency-constrained chain that determines earliest possible completion under the stated assumptions. Identify:
- Tasks on the critical path.
- Gating decisions and external dependencies.
- Tasks with low schedule confidence.
- Available slack only when duration and dependency estimates are credible.

Do not claim dates or a quantified critical path from unknown effort and capacity.

## Integration gates
Use integration steps for shared contracts, data models, schema compatibility, API behavior, common files, and end-to-end acceptance. Validate the actual artifact versions, not just task status.
