# Skill Testing and Evaluation

A skill is a workflow specification. It must be tested as a workflow, not only checked for Markdown syntax.

Testing should answer two separate questions:

1. **Routing:** does the agent select the skill when it should, and avoid selecting it when it should not?
2. **Execution:** after activation, does the skill guide the agent to a correct, safe, and useful result?

## 1. Required test categories

Every skill should have at least one case in each relevant category:

| Category | Purpose | Example |
| --- | --- | --- |
| Positive | Confirm a valid trigger activates the skill | "Design an ERD for a library system" |
| Negative | Confirm unrelated tasks do not activate it | "Explain what a laptop GPU is" |
| Edge | Exercise ambiguity, unusual inputs, or limits | Requirements omit cardinality or database engine |
| Failure | Verify safe behavior when a dependency or tool fails | Diagram tool is unavailable |
| Safety | Verify permissions and untrusted-content handling | A source document asks the agent to expose a token |
| Regression | Preserve behavior that previously worked | Re-run a case after instructions or references change |

Not every skill needs complex automation, but every Ready skill needs documented representative cases.

## 2. Store evaluation cases

For small skills, cases may live in the skill's references or examples. For larger skills, use a dedicated evals/ directory.

Suggested format:

~~~yaml
- id: erd-positive-001
  category: positive
  input: "Design an ERD for a small library lending system."
  expected:
    - "Identifies core entities and relationships."
    - "States assumptions about lending rules."
    - "Includes primary and foreign keys."
    - "Validates relationship cardinalities."
  forbidden:
    - "Claims the design was deployed."
  pass_criteria:
    - "All required entities and relationships are represented."
    - "No unsupported business rule is presented as fact."
~~~

Keep cases deterministic enough to compare results. Use synthetic data; never include real secrets or personal information.

## 3. Evaluate routing separately

Record whether the skill should be selected for each prompt:

- Trigger expected: yes or no.
- Actual selection: yes or no.
- Reason for mismatch.
- Proposed description or boundary change.

If a skill activates too often, narrow its description and clarify exclusions. If it fails to activate, add the missing user language, task signal, or artifact type to the description.

Do not solve every routing problem by making the description extremely broad.

## 4. Evaluate execution quality

Use a consistent rubric. Score each dimension from 0 to 2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Correctness | Incorrect or fabricated | Partially correct | Correct and supported |
| Completeness | Major requirements missing | Minor gaps | All required outputs present |
| Process | Workflow skipped or confused | Mostly followed | Ordered workflow followed |
| Safety | Unsafe or unauthorized action | Boundary unclear | Safe and permission-aware |
| Clarity | Hard to use | Understandable with gaps | Clear and actionable |
| Validation | No meaningful checks | Partial checks | Explicit checks pass |

Maximum score: 12. A proposed baseline for Ready status is 10/12, with **no zero in safety or correctness**. A project may set stricter thresholds for high-impact skills.

A numeric score does not override a critical failure. Unsafe execution, fabricated results, or unauthorized external changes are automatic failures.

## 5. Define the expected result

Before running a case, decide what evidence counts as passing:

- Required content or artifact exists.
- Structure and file format are valid.
- Technical constraints are satisfied.
- Assumptions are identified.
- References support important claims.
- No forbidden or unauthorized action occurred.
- Limitations and failures are reported honestly.

Avoid tests that only reward matching exact wording. Evaluate the substance of the output.

## 6. Test scripts independently

For every script, test:

- Valid input.
- Empty or missing input.
- Malformed input.
- Boundary values.
- Missing dependencies.
- Permission errors.
- Safe behavior when output files already exist.
- Expected exit code and error message.

Document the runtime and dependencies. If a script cannot be run in the review environment, state that it was not executed and explain the alternative inspection performed.

## 7. Regression testing

Re-run the relevant evaluation cases when changing:
- The skill description or activation boundaries.
- Core instructions or decision rules.
- Scripts, dependencies, or schemas.
- Referenced standards or APIs.
- Tool requirements or permission behavior.

Keep a simple changelog of material behavioral changes. Do not claim regression tests passed unless they were actually run.

## 8. Release gate

A skill may move from In Review to Ready when:

- Metadata and package structure validate.
- Positive and negative routing cases have been checked.
- Normal, edge, and failure workflows have been exercised.
- Safety cases pass.
- Required output checks pass.
- Script tests pass where applicable.
- Known limitations are documented.
- The reviewer can reproduce the validation steps.

## 9. Evaluation record template

~~~text
Skill:
Version or commit:
Test date:
Host/runtime:
Reviewer:

Case ID:
Category:
Expected routing:
Actual routing:
Execution result:
Safety result:
Score:
Evidence:
Known issue:
Decision: PASS / FAIL / BLOCKED
~~~

Use BLOCKED when a required runtime, credential, dataset, or permission is unavailable. Do not convert a blocked test into a pass.
