# Risk-Based Test Coverage and Traceability

## Risk model

For each risk, capture:
- Failure mode / uncertainty.
- Affected user, data, system, or business outcome.
- Likelihood / exposure.
- Impact if it occurs.
- Detectability / recovery where useful.
- Existing controls.
- Risk owner and residual risk.

Use qualitative levels when evidence is limited. If a numeric matrix is used, document the scale and avoid false precision.

## Typical high-risk areas

Depending on the system, consider:
- Authentication and authorization.
- Financial calculation, payments, balances, and refunds.
- Personal / sensitive data access, sharing, retention, and deletion.
- Multi-tenant and cross-owner boundaries.
- Data migration, destructive operations, and reconciliation.
- Concurrency, duplicate requests, idempotency, and race conditions.
- External API / message contract failures.
- Backup, restore, and disaster recovery.
- Accessibility for critical user journeys.
- Compatibility and upgrade paths.

Do not assume all these apply to every feature.

## Traceability matrix

| Requirement / outcome | Risk / failure mode | Test level / technique | Case ID / evidence | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| FR-001 | R-002: unauthorized record access | Integration / security | TC-014 | High | Planned |

Trace in both directions when useful:
- Requirement to planned verification.
- High-risk failure mode to mitigating test / control.
- Failed test to affected requirement / release decision.

A listed test case is not proof of execution. Record execution state and evidence separately.

## Prioritization

A practical priority order:
1. Safety, security, legal / policy, and data-integrity risks.
2. Core user journeys and business-critical workflows.
3. High-change / high-complexity areas and external boundaries.
4. Regression-prone areas and historically unstable components.
5. Lower-impact cosmetic and convenience behavior.

Balance risk with test cost, detectability, and release context. The product / risk owner makes acceptance decisions.

## Coverage measures

Possible measures include:
- Requirement coverage.
- Risk coverage.
- Branch / line coverage.
- API operation / schema coverage.
- Platform / browser matrix coverage.
- User journey coverage.

State exactly which metric is reported and how exclusions are treated. High code coverage does not prove that tests assert the correct behavior or that requirements are covered.

## Exit criteria and residual risk

Good exit criteria answer:
- Which tests must complete?
- Which severity of open defects is acceptable?
- What evidence is mandatory?
- Which risks remain, and who accepts them?
- What happens if an environment / dependency is unavailable?

Do not invent a zero-defect policy or coverage percentage. Obtain project-specific thresholds and acceptance authority.
