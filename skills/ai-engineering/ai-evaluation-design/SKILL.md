---
name: ai-evaluation-design
description: Design repeatable evaluations for LLM applications and AI agents using representative datasets, task-specific metrics, human review, calibrated model graders, safety tests, regression comparisons, and reproducible evidence.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# AI Evaluation Design

## Purpose
Design an evaluation system that measures whether an AI application meets its intended quality, reliability, safety, and operational requirements. Convert vague expectations into testable tasks, representative examples, scoring rules, human review procedures, and repeatable comparisons.

A written evaluation plan or dataset is not evidence that a model or application passed. Execution, scoring, analysis, and approval must be recorded separately.

## When to use
Use when the user needs to:
- Evaluate prompts, models, RAG applications, agents, tool use, or generated artifacts.
- Build datasets, rubrics, graders, acceptance thresholds, or regression suites.
- Compare model / prompt / retrieval / workflow versions.
- Measure factuality, groundedness, task completion, tool correctness, latency, cost, or safety.
- Establish evaluation gates before release or provider / model upgrades.

Do not use as the primary workflow for conventional deterministic unit tests or generic test planning without an AI-specific system under evaluation.

## Required inputs
Collect the task definition, target users, expected behavior, unacceptable failures, production-like input distribution, reference data, domain experts, output contract, candidate system versions, data constraints, runtime limits, and evaluation decision owner. Identify whether ground truth exists and who can author it.

## Workflow
1. **Define the evaluation question.** State which product or engineering decision the evaluation will inform.
2. **Decompose quality dimensions.** Separate task success, correctness, relevance, completeness, groundedness, instruction following, tool selection, safety, latency, cost, and user experience as relevant.
3. **Build representative datasets.** Include common cases, long-tail cases, difficult boundaries, ambiguity, multilingual / format diversity, and realistic failure conditions.
4. **Establish reference quality.** Use trusted answer keys, source passages, expected actions, structured outcomes, or expert-labeled rubrics. Document uncertainty and annotator guidance.
5. **Choose metrics and graders.** Combine exact checks, deterministic validators, retrieval metrics, human judgment, and model-based graders according to the property being measured.
6. **Calibrate evaluators.** Compare graders with expert labels, inspect disagreements, measure consistency, and revise rubric wording before relying on the score.
7. **Design adversarial and safety cases.** Include prompt injection, data exfiltration, permission violations, unsafe tool use, refusal boundaries, and instruction conflicts relevant to the application.
8. **Define execution protocol.** Record model / provider, prompt, tool set, retrieval configuration, decoding parameters, dataset version, number of repeats, seeds where supported, environment, and cost budget.
9. **Analyze uncertainty.** Report sample size, score distribution, confidence intervals or uncertainty where suitable, and failure examples. Avoid over-interpreting small differences.
10. **Compare versions.** Use matched datasets and consistent conditions; separate quality changes from latency / cost changes and environmental drift.
11. **Set acceptance gates.** Define minimum outcomes, critical safety requirements, regression tolerances, owner, and exception process before running.
12. **Create the report.** Explain what ran, what passed / failed, where failures cluster, known biases, and release implications.
13. **Maintain the evaluation suite.** Version datasets and rubrics, add production-derived examples only with approval, and periodically review stale or contaminated cases.

## Evaluation principles
- Evaluate the application on representative tasks, not only the underlying model on public benchmarks.
- Use multiple metrics when no single metric captures the desired property.
- Prefer deterministic programmatic checks for exact constraints and structured outputs.
- Use human evaluation for subjective or high-impact judgments and to calibrate model graders.
- Model graders can be biased, inconsistent, or exploitable; validate them against expert-rated examples.
- Do not grade answers solely by lexical similarity when semantically correct alternatives exist.
- Evaluate retrieval and generation separately in RAG systems.
- Evaluate tool selection, arguments, side effects, handoffs, and end-to-end task completion in agent systems.
- Include unanswerable and ambiguous prompts to test uncertainty and appropriate abstention.
- Preserve failures and disagreement examples; aggregate scores alone hide important behavior.
- Avoid data leakage, benchmark contamination, duplicate near-identical examples, and train / eval overlap.
- Version every relevant system component and evaluation artifact.
- Treat model outputs as stochastic; use repeated runs where variability affects the decision.

## Decision rules
- If reference answers are unavailable, create expert-authored rubrics or structured outcome labels; do not invent ground truth.
- If an LLM grader is used, calibrate against human ratings and include anti-gaming examples.
- If metrics disagree, report the dimensions independently and inspect representative disagreements.
- If dataset distribution differs from production, mark generalization claims as limited.
- If a safety failure is critical, do not hide it inside an average score; define a hard gate where required.
- If results are stochastic, use repeated runs and uncertainty estimates appropriate to the sample.
- If a provider evaluation interface or API is changing, verify current availability and lifecycle before building a dependency on it.
- If cost or latency cannot be measured in the target environment, mark those dimensions not evaluated.

## Output contract
Return:
1. Decision question, scope, target system, and version identifiers.
2. Quality dimensions and risk model.
3. Dataset design, provenance, sampling, and annotation instructions.
4. Metrics, grader types, calibration, and aggregation method.
5. Safety / adversarial test coverage.
6. Execution protocol and reproducibility controls.
7. Acceptance thresholds and owner / exception policy.
8. Results and failure analysis only when evaluation was actually run.
9. Limitations, bias, uncertainty, and next iteration.

## Safety and permissions
- Do not use sensitive or personal data without documented approval and minimization.
- Do not upload private prompts, datasets, traces, or outputs to unapproved evaluators.
- Keep credentials, private identifiers, and internal data out of evaluation fixtures and reports.
- Treat model graders as untrusted evaluators until calibrated.
- Do not use evaluation output as sole justification for high-impact decisions about people.
- Do not trigger production traffic or spend without an authorized budget.
- Preserve data rights, retention, and deletion policies across datasets and traces.

## Failure handling
| Situation | Response |
| --- | --- |
| Ground truth unavailable | Mark the affected metric unscorable or design expert rubric; do not invent labels. |
| Human / model graders disagree | Inspect examples, calibrate rubric, and report disagreement. |
| Scores fluctuate materially | Increase repeats or sample size where justified and report uncertainty. |
| Dataset is biased or unrepresentative | Restrict claims and redesign sampling / annotation. |
| Evaluator API is deprecated or unavailable | Use a supported current path or portable dataset / runner design; do not assume old API availability. |
| Safety case fails | Record a distinct safety finding; do not average it away. |

## Validation checklist
- [ ] Evaluation questions map to actual product decisions.
- [ ] Dataset is representative, versioned, and governed.
- [ ] Ground truth / rubric provenance is documented.
- [ ] Metrics match the quality dimension being assessed.
- [ ] Model graders are calibrated against human judgment.
- [ ] Safety and unanswerable cases are included.
- [ ] System and evaluation versions are recorded.
- [ ] Repeated runs / uncertainty are handled where relevant.
- [ ] Acceptance thresholds are defined before execution.
- [ ] Results distinguish PASS, FAIL, BLOCKED, and NOT RUN.
- [ ] No sensitive data or unauthorized spend is used.

## Supporting resources
- Read `references/evaluation-datasets-and-metrics.md` for sampling, annotation, metrics, and graders.
- Read `references/evaluation-reliability-and-governance.md` for calibration, uncertainty, safety, and dataset lifecycle.
- Copy `assets/ai-evaluation-plan.template.md` for an evaluation protocol.
- Use `evals/cases.yaml` to evaluate evaluation-design behavior.

## References
- [OpenAI — Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [OpenAI — Evaluate Agent Workflows](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI — Getting Started with Datasets](https://developers.openai.com/api/docs/guides/evaluation-getting-started)
- [Microsoft — RAG Solution Design and Evaluation](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)

## Maintenance
- Owner: AI Engineering / Quality Engineering
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: model / provider updates, changed product behavior, grader drift, data policy changes, or evaluation regressions.
