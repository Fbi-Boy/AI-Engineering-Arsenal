# Evaluation Reliability and Governance

## Reproducibility
Record:
- Application commit and workflow / prompt version.
- Model provider, model identifier, and version / snapshot where available.
- Tool schema, tool permissions, retrieval index and configuration.
- Temperature / sampling settings and seed where supported.
- Dataset, rubric, grader, and reference-data versions.
- Runtime, region, environment, and dependency versions.
- Execution time, repeat count, token usage, and cost.

A model alias may change over time. Re-run relevant baselines after provider or model updates.

## Calibration and bias
- Compare model graders with independent expert labels.
- Review false positives, false negatives, and systematic subgroup differences.
- Test whether graders reward verbosity, style, or keyword overlap rather than correctness.
- Include adversarial outputs that exploit obvious rubric wording.
- Track inter-rater agreement where multiple human annotators participate.
- Adjudicate disagreements and version rubric changes.

## Statistical care
Report sample size and score distribution, not only a mean. Use confidence intervals or other uncertainty summaries when they are appropriate for the metric and sample design. Avoid declaring small score differences meaningful without sufficient evidence. Repeated stochastic trials should be independent where feasible and budgeted.

## Safety evaluation
Test both model and application controls:
- Instruction hierarchy conflicts and prompt injection.
- Tool permission and unauthorized target attempts.
- Cross-user / cross-tenant data exposure.
- Unsafe side effects and approval bypass.
- Sensitive output, secret leakage, and refusal boundaries.
- Uncertainty, abstention, and recovery after tool failure.

Use safe synthetic targets. Do not probe real third-party systems without authorization.

## Data governance
- Maintain data ownership, purpose, access, retention, and deletion policies.
- Keep training, development, calibration, and held-out evaluation partitions separate where appropriate.
- Prevent benchmark leakage and repeated prompt tuning against the final holdout.
- Remove unnecessary personal / confidential content from traces.
- Require review before adding production examples to a shared evaluation dataset.
