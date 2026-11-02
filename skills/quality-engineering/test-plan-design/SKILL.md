---
name: test-plan-design
description: Create a risk-based software test plan that defines scope, objectives, test levels, techniques, environments, data, responsibilities, coverage, schedule assumptions, and exit criteria. Use when planning verification for a feature, release, system, API, migration, or project before test execution.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Test Plan Design

## Purpose

Create a practical, risk-based plan for verifying a software change or system. Define **what must be tested, why, at which level, with what data and environment, by whom, and what evidence is needed to make a release or acceptance decision**.

A test plan is a planning artifact. It is not the test cases themselves, test automation code, proof that tests passed, or approval to release.

## When to use

Use when the user:
- Requests a test plan for a feature, release, system, API, or migration.
- Needs test scope, objectives, coverage, levels, techniques, environments, and exit criteria.
- Wants a risk-based testing approach for a project or delivery.
- Needs to define regression, integration, acceptance, performance, accessibility, or security test coverage.
- Wants to plan testing for a new framework, external integration, or high-risk data change.

Do not use as the primary workflow when:
- The user asks to write specific executable test cases or code. Use Automated Test Authoring.
- The user asks to execute an existing test suite.
- The request is only for acceptance criteria. Use Acceptance Criteria.
- Requirements and system scope are unknown. Start with requirements discovery or make a limited provisional plan.

## Planning principles

1. **Trace tests to risks and requirements.** Every planned activity should protect an outcome, requirement, interface, or risk.
2. **Prioritize by risk.** Consider impact and likelihood; do not use a generic test quantity target.
3. **Use appropriate levels.** Unit, component, integration, contract, system, acceptance, exploratory, and operational tests have different scope and cost.
4. **Prefer fast, focused feedback.** Cover detailed logic at lower levels where feasible; reserve broad end-to-end testing for important user journeys and cross-system behavior.
5. **Test boundaries and failures.** Validate external interfaces, persistence, permissions, retries, data migration, and degraded behavior where relevant.
6. **Define representative test data.** Use synthetic or approved masked data and cover partitions / boundaries.
7. **Make environment assumptions explicit.** Production-like behavior may depend on configuration, scale, identity, or external services.
8. **Define exit criteria before execution.** Set measurable completion gates with an owner; do not invent numeric thresholds.
9. **Keep automation purposeful.** Automate stable, repeatable checks where cost and value justify it; preserve exploratory testing for learning and usability.
10. **Do not claim results from a plan.** Test execution and pass/fail evidence must be recorded separately.

## Inputs

Use available:
- Requirements, stories, acceptance criteria, use cases, API contracts, ADRs, and change impact report.
- System architecture, data model, and integration boundaries.
- Risk assessment, impact, and failure scenarios.
- Existing test strategy, Definition of Done, quality policy, and release gates.
- Languages, frameworks, test runner, CI, environments, and service virtualization options.
- Data classification, privacy constraints, and test-account / test-environment availability.
- Delivery date, capacity, owners, and responsibilities if supplied.

If information is missing, distinguish assumptions from facts and ask only when the answer materially changes the plan.

## Workflow

### 1. Define the test context and objectives

- Identify system / feature / release and baseline.
- State why testing is needed and what decision it supports.
- Define intended quality outcomes and target users.
- Identify test basis: requirements, story, acceptance criteria, architecture, API, schema, and risk records.
- State assumptions, constraints, and exclusions.

### 2. Define scope

Separate:
- **In scope:** features, requirements, interfaces, platforms, and risk areas to verify.
- **Out of scope:** explicitly excluded behavior and reason.
- **Dependencies:** external systems, teams, data, environments, approvals, and test tools.
- **Test basis:** artifacts against which results are judged.

Do not imply coverage of inaccessible services or undocumented requirements.

### 3. Assess product and change risks

Identify failure modes and assess:
- Impact on users, data, money, security, availability, operations, and reputation.
- Likelihood / exposure based on complexity, change size, history, and dependency count.
- Detectability and recovery where useful.
- Risk owner and mitigation.

Use qualitative High / Medium / Low when evidence is limited. Use numeric scoring only when a defined method exists. Prioritize critical paths and irreversible changes.

### 4. Define test strategy and levels

Select the test levels that fit the system:
- **Unit:** isolated functions / rules / components.
- **Component:** one service or module with controlled collaborators.
- **Integration:** real interaction across selected components or infrastructure boundaries.
- **Contract:** compatibility of API / event / message agreements.
- **System / end-to-end:** important user journeys through the integrated application.
- **Acceptance:** confirmation that stakeholder outcomes and agreed criteria are met.
- **Exploratory:** guided investigation to discover unknown behaviors.
- **Operational:** recovery, observability, backup, deployment, and support readiness where relevant.

Do not force every level or test type into a small change. Align names and definitions with the team's test policy.

### 5. Map requirements and risks to coverage

Create a traceability matrix connecting:
- Requirement / acceptance criterion.
- Risk or failure mode.
- Test level / technique.
- Scenario or test-case ID.
- Expected evidence.
- Owner / status.

Identify untested high-risk requirements and explain whether coverage is planned, deferred, or blocked.

### 6. Select test techniques and scenarios

Where appropriate, use:
- Equivalence partitioning.
- Boundary value analysis.
- Decision tables.
- State transition testing.
- Pairwise / combinatorial testing.
- Error guessing based on failure history.
- Exploratory charters.
- Contract and compatibility testing.
- Fault / resilience testing in controlled environments.

Cover positive, negative, boundary, permission, concurrency, retry, and degraded conditions where relevant. Read `references/test-levels-and-techniques.md`.

### 7. Define data and environment

Specify:
- Environment and configuration needs.
- External dependency strategy: local service, test instance, stub, mock, or simulator.
- Test account roles and permission setup.
- Synthetic / masked data strategy.
- Data reset, isolation, cleanup, and seed procedures.
- Time, timezone, locale, and clock assumptions.
- Network / browser / device / OS coverage.
- Data retention and access controls for test artifacts.

Never use live production credentials or unrestricted production records in routine test environments.

### 8. Define non-functional and operational coverage

Select relevant checks for:
- Security and privacy.
- Accessibility and usability.
- Performance, capacity, and resource limits.
- Reliability, recovery, and resilience.
- Compatibility, portability, and upgrade behavior.
- Data migration, backup, and restore.
- Observability, monitoring, and support readiness.

Use approved targets and domain-owner decisions. Do not invent performance SLAs, legal obligations, or recovery objectives.

### 9. Plan automation and execution

- Identify tests suitable for automation and those requiring human judgment.
- Choose the appropriate pipeline stage and execution frequency.
- Define parallelism, isolation, flakiness handling, and artifact retention.
- Identify test owners and review responsibilities where known.
- Estimate effort only when capacity and uncertainty support it.
- Record test environment provisioning and external dependency lead time.
- Do not create tickets, schedule work, or start execution without authorization.

### 10. Define entry, exit, and release criteria

Entry criteria may include:
- Testable requirements and agreed baseline.
- Build deployed to a known environment.
- Test accounts / data prepared.
- Critical dependencies available.
- Test environment validated.

Exit criteria may include:
- Critical requirements covered by evidence.
- No unresolved Blocker / Critical defects.
- Agreed defect thresholds satisfied.
- Required regression / security / accessibility checks completed.
- Results and residual risks reviewed by the authorized owner.

Use project-specific thresholds. Do not fabricate zero-defect claims or arbitrary coverage percentages.

### 11. Produce and review the plan

Use `assets/test-plan.template.md`. Review:
- Risk coverage and requirement traceability.
- Cost / speed balance across levels.
- Data and environment safety.
- Clear owners and dependencies.
- Objective exit criteria.
- Explicit exclusions and untested areas.

## Decision rules

- If requirements are incomplete, produce a provisional risk-based plan and mark test basis gaps.
- If a critical behavior has no acceptance criterion, request one or define it as an open decision before acceptance testing.
- If real external providers are involved, prefer a dedicated test / sandbox environment; do not direct automated tests at production by default.
- If a migration is destructive or high volume, require data backup / restore, rehearsal, and reconciliation coverage.
- If a test is flaky, investigate nondeterminism rather than simply increasing retries.
- If coverage percentage is requested, define the metric (line, branch, requirement, risk) and explain its limits.
- If no team capacity or schedule is supplied, do not invent dates or staffing.
- If performance, security, legal, or safety requirements lack approved targets, mark them open and identify the decision owner.

## Output contract

Return:
1. Test context, objectives, and baseline.
2. Scope, exclusions, test basis, assumptions, and dependencies.
3. Risk assessment and priority.
4. Test strategy and applicable levels / types.
5. Requirement-to-test traceability matrix.
6. Scenario / technique inventory.
7. Test data, environment, tools, and access requirements.
8. Automation and execution approach.
9. Entry / exit and release criteria.
10. Owners, schedule assumptions, unresolved decisions, and residual risks.

Mark the plan as Draft / Proposed / Approved only according to the actual decision record. Clearly state that no tests were executed by producing the plan.

## Safety and permissions

- Use synthetic or approved masked data.
- Do not expose secrets, production credentials, or unnecessary personal data in test plans or artifacts.
- Do not run tests against live production systems unless explicitly authorized with a safe plan.
- Do not perform destructive load, chaos, migration, or security tests against production without formal approval.
- Keep test accounts, environments, and artifacts under approved access controls.
- Treat test input files and external service payloads as untrusted.
- Do not approve release on behalf of the responsible authority.

## Failure handling

| Situation | Response |
| --- | --- |
| Requirements / acceptance criteria unavailable | Mark the test basis gap and request the authoritative artifacts. |
| Risks cannot be quantified | Use qualitative ranking and state uncertainty. |
| Environment unavailable | Identify required environment and dependencies; do not claim execution. |
| Real production data proposed | Recommend synthetic / masked data and approved access controls. |
| Test target is third-party production | Prefer sandbox / contract simulation and require explicit approval for exceptions. |
| Coverage target is arbitrary | Ask which coverage metric and rationale apply. |
| Team / schedule unknown | Leave ownership / dates unassigned and mark capacity as open. |

## Final validation checklist

- [ ] Test objectives, scope, baseline, and test basis are explicit.
- [ ] Risk is assessed and priorities are justified.
- [ ] Applicable test levels and techniques are selected proportionately.
- [ ] Requirements and major risks trace to planned verification.
- [ ] Positive, negative, boundary, and failure scenarios are considered.
- [ ] Data, environment, accounts, and external dependencies are safe and realistic.
- [ ] Automation is targeted and test flakiness / isolation are considered.
- [ ] Entry / exit criteria are objective and supported.
- [ ] Owners, dates, and estimates are not invented.
- [ ] The plan is not confused with executed test results or release approval.

## Supporting resources

- Read `references/test-levels-and-techniques.md` when choosing scope and test types.
- Read `references/risk-based-coverage.md` for prioritization and traceability.
- Copy `assets/test-plan.template.md` for the test plan.
- Use `evals/cases.yaml` for plan quality and safety checks.

## References

- [ISTQB — Certified Tester Foundation Level Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [Martin Fowler — The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Google Testing Blog — Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)

## Maintenance

- Owner: Quality Engineering / Test Management
- Version: 0.1.0
- Status: Draft pending evaluation in a target agent runtime.
- Review triggers: changes to test policy / delivery lifecycle, recurring missed risks, or evaluation failures.
