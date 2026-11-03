---
name: performance-analysis
description: Investigate and improve software performance using measurable workloads, baselines, profiling, latency distributions, resource analysis, controlled experiments, and safe validation.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Performance Analysis

## Purpose
Diagnose performance behavior from measurements and improve user-visible latency, throughput, resource efficiency, scalability, or cost without compromising correctness, security, or reliability. A recommendation must identify measured evidence, expected effect, trade-offs, and a validation method.

## When to use
Use for performance investigation, profiling, benchmarking, capacity analysis, latency / throughput / memory / CPU / I/O analysis, database tuning, frontend performance, or performance regression review. Do not use for uncontrolled production load generation or generic bug fixing without performance evidence.

## Required inputs
Identify the affected system and user journey, workload, environment, baseline, approved targets, traffic and data distribution, dependencies, recent changes, host / container limits, available tools, and permitted test scope. If targets are undocumented, measure baseline rather than invent an SLO.

## Workflow
1. **Define the symptom.** Record user impact, affected path, environment, timeframe, and recent changes.
2. **Model the workload.** Describe request mix, arrival rate, concurrency, payload / dataset sizes, cache state, and dependency behavior.
3. **Capture a baseline.** Record version, environment, configuration, sample count, warm-up, and exact measurement method.
4. **Choose metrics.** Measure suitable latency distributions (p50 / p95 / p99), throughput, error rate, CPU, memory, I/O, queues, database / network time, and cost.
5. **Instrument and profile.** Use traces, profiles, query plans, browser timelines, and system metrics to identify where time and resources are spent.
6. **Form hypotheses.** Distinguish CPU, I/O, lock contention, allocation, algorithmic complexity, cache behavior, queueing, and external dependency limits.
7. **Design controlled experiments.** Change one material factor where feasible; hold workload and environment steady; record run-to-run variance.
8. **Prioritize changes.** Consider impact, evidence confidence, risk, maintainability, cost, and regression potential.
9. **Implement within scope.** Preserve behavior and security; avoid unrelated refactors.
10. **Re-measure.** Compare to the baseline under equivalent conditions and include errors and tail latency, not only average speed.
11. **Check system effects.** Evaluate saturation, concurrency, cache invalidation, autoscaling, cost, and degradation under pressure.
12. **Report.** State measured gains / regressions, uncertainty, tools and commands used, and residual bottlenecks.

## Principles
- Use representative workloads and note local-versus-production differences.
- Prefer distributions and histograms over averages when tail latency matters.
- Separate successful-request latency from failure latency where appropriate.
- Use profiling and sampling appropriate to the suspected bottleneck.
- Inspect query plans, cardinality, locks, and round trips before suggesting indexes.
- Distinguish fixed-concurrency throughput from realistic arrival-rate behavior.
- Account for warm-up, JIT, garbage collection, connection pools, and background work.
- Verify correctness and error rates after every optimization.
- Consider end-to-end critical path and user-perceived latency.
- A faster component may not improve system latency if it is not on the critical path.

## Decision rules
- If there is no target, report baseline and request an owner-defined goal before claiming success.
- If evidence points to another bottleneck, follow the evidence.
- If measurement noise is high, stabilize conditions and repeat before ranking small changes.
- If performance changes increase errors, tail latency, or cost, report the trade-off.
- If testing can affect production, use an isolated environment and explicit approval with traffic limits and stop conditions.
- If results cannot be reproduced, label them inconclusive.

## Output contract
Return scope, workload, environment, baseline, target provenance, metrics, profiling evidence, bottleneck and confidence, proposed / implemented changes, comparable before / after results, correctness / resource / cost impact, commands actually run, and limitations.

## Safety and permissions
- Do not run high-volume, stress, soak, or chaos tests against production without explicit authorization and a safety plan.
- Avoid exhausting shared resources or generating uncontrolled traffic.
- Use synthetic / non-sensitive data where feasible.
- Redact customer traces, request bodies, credentials, and private identifiers.
- Check profiler overhead and disclose when instrumentation may distort measurements.
- Obtain approval before paid infrastructure scale-up or load-test spend.

## Failure handling
| Situation | Response |
| --- | --- |
| Workload unknown | Define a representative workload before comparing results. |
| No baseline | Capture a safe baseline; do not claim percentage improvement without it. |
| Tool unavailable | Use available metrics / traces and mark profiling incomplete. |
| Results fluctuate | Repeat controlled runs and report uncertainty. |
| Bottleneck not isolated | Propose targeted instrumentation instead of guessing. |
| Production target proposed | Stop and request an isolated environment or explicit authorization. |

## Validation checklist
- [ ] Workload and environment are measurable and representative.
- [ ] Baseline includes distributions and relevant resource metrics.
- [ ] Bottleneck is supported by profile / trace / query evidence.
- [ ] Experiments control material variables and record variance.
- [ ] Correctness and error rates are checked.
- [ ] Before / after results use comparable conditions.
- [ ] Resource, cost, saturation, and tail-latency trade-offs are stated.
- [ ] No unapproved production load or sensitive data exposure occurred.

## Supporting resources
- Read `references/performance-measurement-and-profiling.md` for workload, metrics, and bottleneck analysis.
- Read `references/benchmarking-and-load-safety.md` for controlled experiments and safe load testing.
- Copy `assets/performance-analysis-report.template.md` for the investigation report.
- Use `evals/cases.yaml` for measurement quality and safety evaluation.

## References
- [Google SRE — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [OpenTelemetry — Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/)
- [OpenTelemetry — Signals](https://opentelemetry.io/docs/concepts/signals/)
- [OpenTelemetry — Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)

## Maintenance
- Owner: Software Engineering / SRE
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: runtime or workload changes, new performance budgets, or evaluation failures.
