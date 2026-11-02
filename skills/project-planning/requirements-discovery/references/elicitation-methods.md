# Requirements Elicitation Methods

Use the lightest technique that can reliably reveal the missing information. Methods can be combined; none is mandatory for every project.

## 1. Document and artifact analysis

**Use when:** the user provides policies, forms, spreadsheets, manuals, tickets, process diagrams, existing requirements, or an existing codebase.

**How:**
1. Identify the artifact's owner, date, purpose, and likely completeness.
2. Extract stated needs, rules, roles, inputs, outputs, exceptions, and constraints.
3. Separate current-state behavior from desired future-state behavior.
4. Record unclear, contradictory, outdated, or missing information.
5. Trace findings to the file, page, section, ticket, or code location.

**Watch for:** old documents presented as current policy; implementation behavior that may be a defect rather than an intended requirement.

## 2. Stakeholder interviews

**Use when:** goals, priorities, responsibilities, or pain points are unclear.

Ask open questions first:
- What are you trying to accomplish?
- What happens today, step by step?
- Where does the current process fail or slow down?
- What information do you need before acting?
- What should happen in the normal case and in an exception?
- How would you know the new system has succeeded?

Probe concrete examples rather than accepting abstract answers. Ask for the last real occurrence, the decision made, the information used, and the result.

**Watch for:** leading questions, assumed solutions, and treating one stakeholder's opinion as universal.

## 3. Contextual inquiry and observation

**Use when:** work is operational, complex, regulated, or difficult for users to describe.

Observe the actual workflow with permission. Note actors, tools, handoffs, data, waiting time, workarounds, and exceptions. Do not record sensitive information that is not necessary.

Distinguish observed behavior from the reason someone believes it occurs.

## 4. Workshops and collaborative mapping

**Use when:** several stakeholder groups need a shared understanding.

Useful workshop outputs include:
- Stakeholder map.
- Current-state and future-state workflow.
- User journey or service blueprint.
- Domain vocabulary and glossary.
- Prioritized problem list.
- Decision log and unresolved conflicts.

Make disagreements visible. A workshop is not proof of consensus unless participants explicitly agree.

## 5. Scenarios, use cases, and user stories

**Use when:** requirements concern user goals and interactions.

A scenario should identify the actor, trigger, preconditions, main flow, alternate flows, failure paths, and observable outcome.

A user story may use:

> As a [user role], I want [capability], so that [benefit].

A story is not complete without relevant acceptance criteria. Do not force every requirement into user-story syntax; system, interface, data, quality, and regulatory constraints may need other forms.

## 6. Prototyping and examples

**Use when:** stakeholders struggle to explain an interface, workflow, report, or interaction.

Use sketches, wireframes, sample reports, clickable prototypes, or examples to provoke feedback. Label prototypes as exploratory. Do not treat an unapproved mockup as a committed design requirement.

## 7. Surveys and structured questionnaires

**Use when:** information must be collected from a larger group or compared consistently.

Use clear, neutral wording and provide a way to report an answer not covered by the options. Use interviews or follow-up questions to investigate surprising responses.

Avoid surveys when the problem is still poorly understood; broad surveys can collect opinions without explaining the underlying need.

## 8. Selecting a method

| Situation | Useful starting method |
| --- | --- |
| Existing process or application | Artifact analysis + contextual inquiry |
| Unclear goals or priorities | Stakeholder interview |
| Multiple groups with conflicting needs | Facilitated workshop + decision log |
| Interface or interaction is unclear | Scenario + low-fidelity prototype |
| Many users need comparable input | Structured survey followed by targeted interviews |
| High operational or safety impact | Interviews + observation + formal review by domain owners |

## 9. Practical discovery sequence

1. Review available evidence.
2. Identify stakeholders and their relationship to the system.
3. Ask about goals and current pain points.
4. Map the normal workflow and important exceptions.
5. Identify information, decisions, interfaces, and constraints.
6. Draft requirements and open questions.
7. Validate the interpretation with the relevant stakeholders.

## Source note

This reference is a practical summary, not a reproduction of a proprietary body of knowledge. The requirements engineering process and terminology are informed by ISO/IEC/IEEE 29148:2018 and IEEE's public overview of requirements management. Select methods based on context; the standard does not mandate one universal interview or workshop script.

- [ISO/IEC/IEEE 29148:2018 — Requirements engineering](https://www.iso.org/standard/72089.html)
- [IEEE Standards Association — 29148-2018](https://standards.ieee.org/ieee/29148/6937/)
- [IEEE Technology Navigator — Requirements management](https://technav.ieee.org/topic/requirements-management/)
