# Textual Use-Case Specification Guide

A diagram provides an overview. A textual specification explains the behavior well enough to review requirements and derive acceptance criteria.

## Recommended fields

| Field | Guidance |
| --- | --- |
| ID / name | Stable identifier and verb-oriented goal name. |
| Scope | System or subsystem boundary. |
| Level | User goal, summary, or subfunction; keep levels explicit. |
| Primary actor | Role whose goal initiates the interaction. |
| Supporting actors | External people or systems that provide a service. |
| Stakeholders and interests | What each party needs protected or achieved. |
| Trigger | Event that starts the use case. |
| Preconditions | Facts that must be true before the main scenario begins. |
| Main success scenario | Numbered actor intent and system response steps. |
| Alternate flows | Valid variations that still achieve the goal. |
| Exception flows | Failure, invalid input, denial, timeout, or unavailable service. |
| Postconditions | State or outcome guaranteed after success or failure. |
| Business rules | Confirmed policy constraints or references. |
| Related requirements | Source IDs for traceability. |
| Open questions | Missing decisions and responsible owner. |

## Write the main flow

Use alternating actor intent and system response where helpful:
1. Actor requests a goal-oriented outcome.
2. System provides the expected response.
3. Actor supplies the next relevant decision or information.
4. System confirms the outcome.

Keep steps at the actor/system interaction level. Do not describe database queries, internal method calls, or pixel-level UI instructions unless the user specifically requests implementation detail.

## Alternate and exception flows

An alternate flow describes a valid variation, such as selecting a different date range.

An exception flow describes an unsuccessful or interrupted interaction, such as invalid input, missing permission, or external service timeout.

For each flow, state:
- The condition that branches from the main scenario.
- What the actor or system does.
- Whether the goal is achieved, retried, canceled, or left pending.
- Any relevant state change or guarantee.

## Preconditions and postconditions

Avoid circular statements:
- Weak precondition: "The user is allowed to view the page."
- Better precondition: "The user is authenticated; the system has an established authorization policy for the requested record."

Postconditions should describe observable guarantees, not vague success labels.

## Keep policy explicit

Do not infer permissions from role titles. For example, a "Lecturer" actor does not automatically have authority to edit finalized attendance records. Record the rule's source or mark it open for an authorized decision.

## Traceability

Where possible, link:
- Actor goal -> stakeholder need.
- Use case -> functional requirement.
- Main / alternate flow -> acceptance criteria.
- Failure / security flow -> quality or security requirement.

A use case is a model of expected behavior; it is not proof that the behavior is implemented.
