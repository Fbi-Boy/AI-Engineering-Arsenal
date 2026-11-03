# Evaluation Datasets and Metrics

## Dataset design
Each example should define, where relevant:
- Stable ID and dataset version.
- Task / capability category.
- Input and required context.
- Expected behavior, answer, structured output, or allowed outcome set.
- Source provenance and labeling method.
- Difficulty / risk tags.
- Annotation confidence and adjudication status.
- Privacy and retention classification.

Sample the distribution deliberately:
- Common high-volume workflows.
- High-impact and rare failures.
- Boundary values and malformed input.
- Ambiguous, conflicting, and unanswerable cases.
- Different languages, formats, and user intents.
- Adversarial and misuse attempts.

Use production traces only where approved, redacted, and governed. Synthetic cases are useful but should not be mistaken for a representative production distribution.

## Metrics by quality dimension
| Dimension | Possible method | Limitation |
| --- | --- | --- |
| Exact structure / schema | Deterministic validator | Does not prove semantic correctness |
| Task completion | Outcome checklist or expert label | Requires a clear task contract |
| Retrieval quality | Recall@k, precision@k, MRR, nDCG | Depends on relevance labels |
| Groundedness | Evidence support rubric / citation checks | Automated graders need calibration |
| Semantic quality | Human rubric / calibrated model grader | May vary by evaluator |
| Tool use | Correct tool, arguments, permission, observed result | A plausible trace may still fail user intent |
| Safety | Hard constraints and expert review | Average scores can conceal critical failures |
| Performance | Latency percentiles, token / tool counts, cost | Depends on controlled environment |

## Grader selection
- Exact checks for schema, format, required fields, and deterministic rules.
- Programmatic scoring for numeric outcomes, validators, and allowed state transitions.
- Human review for nuance, domain correctness, high-impact decisions, and grader calibration.
- Model-based scoring for scalable rubric assessment only after agreement checks with human ratings.
- Pairwise comparison for preference decisions where an absolute rubric is difficult, with blinded ordering where feasible.

## Metric interpretation
Define numerator, denominator, aggregation, thresholds, exclusions, and missing-result handling. Report per-category results and failure examples. Do not combine incomparable measures into a single arbitrary score.
