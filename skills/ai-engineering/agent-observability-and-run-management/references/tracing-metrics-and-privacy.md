# Tracing, Metrics, and Privacy

## Trace topology
Consider spans for:
- Root workflow / run.
- Planner and routing decision.
- Specialist skill invocation / handoff.
- Model request and response.
- Tool call and external service.
- Guardrail and approval decision.
- Artifact validation and integration gate.

Propagate trace context through HTTP, queue, and background-worker boundaries when supported. Record parent-child causality and relevant versions.

## Metrics
Potential metrics include:
- Run starts, completions, failures, cancellations, and pauses.
- Step duration and queue / approval wait.
- Tool calls by bounded tool name and outcome.
- Retry, timeout, and validation-failure counts.
- Token / request usage and measured cost.
- Resource saturation and dependency latency.

Define unit, aggregation, labels, and owner. Keep high-cardinality run IDs out of metric labels; use traces or logs for detailed lookup.

## Structured logs
Use stable event names, severity, service / version, run and step correlation IDs, state version, and reason codes. Prefer references and hashes to full private payloads.

## Privacy controls
- Redact credentials, authorization headers, tokens, cookies, private keys, and secrets.
- Avoid full prompts, completions, tool arguments, browser pages, and user documents unless explicitly required and approved.
- Consider user / tenant data, source code, internal URLs, and generated files sensitive.
- Restrict trace access and define retention / deletion for exports, replicas, and backups.
- Test redaction with synthetic secret patterns.

## Telemetry versus audit
Telemetry is optimized for diagnosis and may be sampled or expired. Audit evidence records access, policy, approval, and consequential action decisions under separate integrity and retention controls. Never make a sampled trace the only evidence of an authorization or approval decision.

## Alerts and runbooks
Alert only on symptoms with an agreed objective, actionable threshold, and responsible owner. Link each alert to a runbook with diagnosis, safe mitigations, escalation, and recovery constraints.
