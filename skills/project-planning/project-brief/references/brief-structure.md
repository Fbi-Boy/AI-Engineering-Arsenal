# Project Brief Structure Guide

A project brief should be the smallest document that supports the next real decision. It is not a full requirements specification, a sprint backlog, a delivery contract, or a technical design.

## Recommended sections

| Section | Purpose | Review question |
| --- | --- | --- |
| Executive summary | Align the reader on the project in a few sentences. | Can someone explain the project after reading only this section? |
| Problem / opportunity | Explain the current need and why action may be worthwhile. | Is the problem evidenced and distinct from the proposed solution? |
| Outcomes | State the change expected for users or the organization. | Can each outcome be observed? |
| Stakeholders | Identify affected groups and decision owners. | Who contributes, who decides, and who is affected? |
| Scope | Bound the first delivery or discovery effort. | What is included and explicitly excluded? |
| Capabilities / deliverables | Describe high-level results, not detailed tasks. | Are outputs connected to outcomes? |
| Constraints | Record mandatory limits such as platform or policy. | Is each constraint sourced and genuinely mandatory? |
| Assumptions | Make uncertain beliefs visible. | What would change if the assumption is false? |
| Risks / dependencies | Show conditions that may affect success. | Is there an owner or next action for material items? |
| Governance | State who reviews and approves decisions. | Is the approval status supported by evidence? |
| Next steps | Recommend the next learning or delivery activity. | Is each next step actionable without overcommitting? |

## Level of detail

### Small prototype or learning project

Use a short brief:
- Problem and target user.
- One or two expected outcomes.
- MVP scope and exclusions.
- Main assumptions and risks.
- What the prototype should help validate.
- A clear decision after the prototype.

Avoid a formal governance structure unless the context requires it.

### Team product or business application

Add:
- Stakeholder roles and decision authority.
- Primary workflows and system boundary.
- Success measures and their owners.
- Integration, data, security, and operational dependencies.
- First-release scope and future candidates.
- Review cadence and approval needs.

### High-risk or multi-team initiative

Add stronger governance:
- Explicit accountable sponsor and decision forum.
- Risk owners and review gates.
- Data protection, security, safety, and compliance review dependencies.
- Migration, operational readiness, and support considerations.
- Decision log and change-control expectations.

Do not claim that this document alone satisfies a formal governance or compliance framework.

## Keep outcomes distinct from outputs

| Outcome | Output / deliverable |
| --- | --- |
| Students can confirm attendance with fewer manual corrections. | Attendance web application. |
| Support staff can resolve requests with traceable decisions. | Ticket management module. |
| Operators can detect service degradation earlier. | Monitoring dashboard and alert rules. |

A project can deliver its planned output without achieving the intended outcome. Capture both where relevant.

## Describe measures responsibly

For each proposed measure, capture:
- Name and definition.
- Baseline, if available.
- Target, if agreed.
- Measurement window.
- Data source.
- Owner.

Do not invent a percentage, response time, adoption target, or financial benefit. Mark missing fields as TBD and identify who can confirm them.

## Scope language

Prefer concrete statements:
- In scope: "A student can view their attendance record for the current semester."
- Out of scope: "The first release will not support attendance appeals."
- Constraint: "The solution must integrate with the campus identity provider." (only when confirmed)
- Proposal: "A mobile-first responsive web interface is proposed for the first release."

Avoid vague boundaries such as "all campus processes" or "complete digital transformation".
