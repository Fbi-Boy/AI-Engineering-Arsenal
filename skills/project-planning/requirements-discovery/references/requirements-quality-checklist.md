# Requirements Quality Checklist

Use this checklist for individual requirements and for the requirements set as a whole. It is a practical review aid informed by ISO/IEC/IEEE 29148:2018; it is not a claim of formal standards compliance.

## 1. Individual requirement checks

For each requirement, ask:

- **Necessary:** does it support a stakeholder need, business outcome, constraint, or justified quality attribute?
- **Singular / atomic:** does it express one principal obligation rather than combining unrelated behaviors?
- **Clear:** can different readers interpret it in substantially the same way?
- **Unambiguous:** are terms, actors, conditions, and outcomes defined?
- **Feasible:** can the requirement be met within known technical, operational, legal, and resource constraints?
- **Verifiable:** can inspection, analysis, demonstration, or test determine whether it is satisfied?
- **Traceable:** is its source or rationale known?
- **Consistent:** does it conflict with another requirement or approved constraint?
- **Implementation-independent where possible:** does it describe the required behavior rather than prematurely dictate a design?

Example of a weak requirement:

> The application must be fast and easy to use.

Better discovery outcome:

> The application must display the search results within [target time] for [defined dataset size] under [defined load].

If the target time, dataset, or load is not known, do not invent it. Record the missing measure and ask the stakeholder who can define it.

## 2. Quality requirements

For each relevant quality attribute, define the condition and measurement context.

| Attribute | Questions to clarify |
| --- | --- |
| Performance | Which operation? What response time or throughput? Under what data volume, concurrency, and environment? |
| Availability / reliability | Which service period? What uptime, recovery, or failure behavior is required? |
| Security | Which assets, threats, roles, authentication, authorization, and audit events matter? |
| Privacy | Which personal data is processed? What purpose, access, retention, deletion, and consent rules apply? |
| Usability / accessibility | Which user groups, tasks, devices, accessibility needs, and success measures apply? |
| Scalability | What growth dimension matters: users, requests, data, tenants, or geographic reach? |
| Maintainability | What operational or changeability expectations can be measured or reviewed? |
| Compatibility / portability | Which browsers, operating systems, devices, APIs, or environments must be supported? |
| Recoverability | Which failure scenarios, recovery time, and recovery point expectations apply? |

Do not include every attribute by default. Select those relevant to the product and its context.

## 3. Requirement set checks

- [ ] Each stakeholder goal is represented or explicitly excluded.
- [ ] Critical user journeys include alternate and failure flows.
- [ ] Roles and permissions are not conflated.
- [ ] Data creation, validation, access, retention, export, and deletion needs are considered where relevant.
- [ ] External interfaces and dependencies are identified.
- [ ] Quality requirements cover material risks.
- [ ] Constraints are distinguished from preferences.
- [ ] Duplicates and contradictions are identified.
- [ ] Priorities have an owner and rationale.
- [ ] Acceptance checks can be mapped to requirements.
- [ ] Open questions and assumptions remain visible.
- [ ] Requirement IDs remain stable when wording is refined.

## 4. Recommended requirement statement pattern

Use a pattern suited to the requirement:

**Functional behavior**

> When [trigger/condition], the [system/actor] shall [observable behavior] so that [outcome], subject to [relevant rule].

**Quality requirement**

> Under [defined operating condition], the system shall [measurable quality result] as measured by [verification method].

**Constraint**

> The solution shall [mandatory constraint] because [source/authority].

Avoid inserting "shall" into an uncertain proposal just to make it look formal. Mark unconfirmed statements as Proposed or Open.

## 5. Status and priority are different

Suggested status values:
- Draft
- Confirmed
- Proposed
- Open
- Conflict
- Approved
- Deferred
- Rejected

Suggested priority values, only when the project adopts them:
- Must
- Should
- Could
- Won't (this release)

Do not use priority as a substitute for status. A high-priority requirement can still be unconfirmed.

## 6. Validation versus verification

- **Verification:** is the requirement written clearly and well-formed, and can it be checked?
- **Validation:** does it represent the stakeholder's actual need and intended use?

An AI-generated requirements document can be reviewed for quality, but it cannot claim stakeholder validation or approval without evidence from the appropriate people.

## 7. Standard reference and version note

ISO/IEC/IEEE 29148:2018 describes requirements engineering processes and information items across system and software lifecycles. ISO's public catalog currently lists the 2018 edition as published and confirmed in 2024, while also indicating that a revision is under development. Check the catalog before relying on a version-sensitive claim.

- [ISO standard record](https://www.iso.org/standard/72089.html)
- [IEEE standard record](https://standards.ieee.org/ieee/29148/6937/)
