---
name: agent-observability-and-run-management
description: Design observability and operational run management for AI agent workflows, including run lifecycle events, distributed traces, metrics, redacted logs, status reporting, failure classification, cancellation, and incident diagnostics.
metadata:
  author: AI Engineering Arsenal
  version: "0.1.0"
---

# Agent Observability and Run Management

## Purpose
Make AI agent and multi-skill workflows understandable, diagnosable, and operable. Define how a run is identified, followed, paused, resumed, cancelled, failed, measured, and reported without confusing activity telemetry with security audit evidence or exposing private content.

A completed run event does not automatically prove every requested action succeeded. Inspect step outcomes and acceptance evidence.

## When to use
Use when:
- An assistant executes multi-step, long-running, delegated, or tool-driven tasks.
- Operators need run status, progress, tracing, failure diagnosis, or cost visibility.
- A task must survive disconnection, pause for approval, resume, or cancel.
- Teams need to troubleshoot agent latency, tool errors, loops, or unexpected behavior.

Do not use as a substitute for durable state design, access control, or a formal audit / compliance system.

## Required inputs
Identify agent runtime, workflow / run lifecycle, deployment topology, available events and telemetry, task and step identifiers, tool inventory, data classification, privacy / retention policy, operational owners, incident process, and existing service objectives. Do not invent SLOs or assume every runtime emits the same event schema.

## Workflow
1. **Define operational questions.** Identify what operators and users need to know: status, current step, blocked dependency, tool error, approval wait, latency, token / cost use, and final outcome.
2. **Map the run lifecycle.** Model queued, accepted, running, awaiting approval / input, resuming, completed, failed, cancelled, timed out, and expired states as applicable.
3. **Establish identifiers.** Define stable run, task, step, agent, handoff, tool-call, approval, trace, and correlation IDs. Avoid exposing internal IDs as secrets or using high-cardinality values as metric labels.
4. **Define events.** Specify lifecycle events, ordering, timestamps, state versions, actor / owner, status reason, and references to artifacts. Design for duplicates, delayed delivery, reconnect, and missing events.
5. **Instrument traces.** Create spans for root run, specialist / skill step, model call, tool call, handoff, guardrail, approval, and external dependency. Propagate trace context across services where supported.
6. **Define metrics.** Measure run counts and outcomes, step duration, queue / approval wait, tool success / error, retries, timeouts, token use, cost, and resource saturation. Define units and aggregation.
7. **Design logs and redaction.** Record structured operational evidence without raw secrets, private prompts, full user payloads, or unnecessary personal data.
8. **Separate telemetry from audit.** Use telemetry for diagnosis and performance; preserve authorization / approval / side-effect decisions in an access-controlled audit record with its own integrity and retention requirements.
9. **Implement progress reporting.** Show meaningful states and completed deliverables, not opaque spinner / percent claims. Derive progress from task plan and verified step completion.
10. **Handle pause / resume / cancel.** Persist reference to resumable state; reconcile after stream or process disconnection; check cancellation before queued actions; distinguish approval pause from failure.
11. **Set alerting and runbooks.** Define alerts only when an owned objective and actionable response exist. Document diagnostic queries, escalation, replay, and safe recovery.
12. **Validate observability.** Test missing / duplicate / out-of-order events, trace breaks, redaction, sampling, retry loops, status accuracy, and cancellation.
13. **Report operations.** Use the run report template; identify observed facts, missing telemetry, limitations, and unresolved operational ownership.

## Design principles
- Use traces, metrics, and logs for complementary views; no single signal is sufficient for every operational question.
- Propagate causal context across asynchronous and distributed boundaries where the platform supports it.
- Keep run and step status tied to validated workflow state, not merely the last emitted event.
- Distinguish a run finishing from each deliverable meeting acceptance criteria.
- Record approval wait as a normal paused state, not a generic error.
- Use bounded sampling and privacy-safe attributes; avoid recording secrets or full sensitive content.
- Keep audit evidence separate from mutable / sampled telemetry.
- Use low-cardinality dimensions for metrics; put detailed identifiers in traces or logs with access control.
- Make event handling idempotent and tolerant of delayed or duplicated delivery.
- Provide cancellation visibility and prevent queued work from running after cancellation.
- Treat token / cost and latency estimates as measured usage, not invented precision.
- Define SLOs, alert thresholds, retention, and escalation with the accountable service owner.

## Decision rules
- If runtime event semantics are unknown, inspect the current SDK / provider version and document gaps.
- If a stream disconnects, query durable run state before declaring failure or success.
- If approval is pending, report awaiting approval and retain a resumable checkpoint.
- If cancellation is requested, stop future side effects and reconcile in-flight operations.
- If trace payloads contain sensitive data, redact or avoid capture rather than relying only on dashboard access control.
- If a metric needs unique task IDs as labels, redesign labels to avoid unbounded cardinality.
- If alerts have no owner or response, do not create a noisy alert; document a diagnostic dashboard or owner decision.
- If an event says completed but output validation fails, keep the business task incomplete.
- If audit and telemetry requirements conflict, keep the required audit record in a separately controlled system.

## Output contract
Return:
1. Run lifecycle and state model.
2. Event schema and identifier / correlation strategy.
3. Trace topology and spans.
4. Metrics, units, aggregation, and cardinality controls.
5. Structured logging, redaction, sampling, and retention.
6. Status / progress presentation semantics.
7. Pause, resume, cancellation, and recovery behavior.
8. Alerts, dashboards, runbooks, and owners.
9. Validation scenarios, instrumentation gaps, and limitations.

## Safety and permissions
- Never log credentials, tokens, cookies, private keys, or full authorization headers.
- Minimize prompt, completion, tool-argument, and tool-result capture; redact private content by default.
- Restrict access to traces and audit logs according to data sensitivity.
- Do not expose one user's run history to another.
- Define deletion / retention across logs, traces, exports, and backups.
- Never treat telemetry as permission to replay a tool action.
- Do not execute destructive recovery or replay without current authorization.

## Failure handling
| Situation | Response |
| --- | --- |
| Stream disconnected | Fetch authoritative run state and last validated checkpoint. |
| Event missing or out of order | Reconcile using sequence / state version rather than guessing. |
| Duplicate event | Process idempotently; do not duplicate downstream actions. |
| Trace context lost | Record a correlation gap and repair propagation at the boundary. |
| Approval pending | Surface awaiting approval and preserve resumable state. |
| Cancellation during tool call | Stop queued actions and reconcile the in-flight outcome. |
| Sensitive payload in telemetry | Restrict access, redact / purge according to policy, and review capture configuration. |
| Runtime lacks usage metrics | Mark cost / token observability incomplete; do not estimate as fact. |

## Validation checklist
- [ ] Run lifecycle states and authoritative source are explicit.
- [ ] Identifiers correlate runs, steps, tools, approvals, and artifacts.
- [ ] Events tolerate duplication, delays, disconnection, and reordering.
- [ ] Trace spans cover major workflow boundaries.
- [ ] Metrics use defined units and bounded cardinality.
- [ ] Logs / traces are redacted and access-controlled.
- [ ] Audit decisions are stored separately from diagnostic telemetry.
- [ ] UI status reflects verified task state and approval pauses.
- [ ] Cancellation prevents future queued side effects.
- [ ] Runbooks, alerts, and owners are actionable.
- [ ] Telemetry claims match data actually collected.

## Supporting resources
- Read `references/agent-run-lifecycle-and-events.md` for run states, event semantics, and recovery.
- Read `references/tracing-metrics-and-privacy.md` for trace topology, metrics, logs, redaction, and audit separation.
- Copy `assets/agent-run-observability-plan.template.md` for an instrumentation and operations plan.
- Use `evals/cases.yaml` for run visibility, reliability, and privacy evaluation.

## References
- [OpenAI — Integrations and Observability](https://developers.openai.com/api/docs/guides/agents/integrations-observability)
- [OpenAI — Tracing](https://developers.openai.com/api/docs/guides/agents-api/tracing)
- [OpenAI — Results and State](https://developers.openai.com/api/docs/guides/agents/results)
- [OpenTelemetry — Signals](https://opentelemetry.io/docs/concepts/signals/)
- [OpenTelemetry — Context Propagation](https://opentelemetry.io/docs/concepts/context-propagation/)

## Maintenance
- Owner: AI Engineering / SRE / Platform Observability
- Version: 0.1.0
- Status: Draft pending target-runtime evaluation.
- Review triggers: runtime events / SDK updates, privacy policy changes, operational incidents, or evaluation regressions.
