# Architecture Evidence: Observation vs Inference

A repository map is useful only when readers can tell what is known and what is assumed.

## Evidence categories

| Label | Meaning | Example |
| --- | --- | --- |
| Directly observed | Explicitly present in source, configuration, docs, or tests. | package manifest declares a framework version. |
| Strongly indicated | Multiple artifacts support a conclusion, but runtime confirmation is missing. | A route module and server bootstrap indicate an HTTP API. |
| Inferred | A plausible interpretation that needs runtime or owner confirmation. | A folder appears to be a future service boundary. |
| Unknown | Available evidence is insufficient. | A private external service's runtime behavior. |
| Conflicting | Sources disagree. | README describes a worker, but current deployment config omits it. |

Use these labels in architecture summaries and feature traces.

## What source code can establish

Source and configuration can show:
- Declared dependencies and language versions.
- Entry points and registration patterns.
- Static imports and call relationships.
- Route declarations, model definitions, validators, and middleware.
- Tests and expected local behavior.
- Environment variable names and configuration defaults.

Source alone may not prove:
- Which services are actually deployed.
- Runtime traffic paths, network access, or infrastructure topology.
- Production environment values or secret contents.
- External provider availability or behavior.
- Real performance, scale, or reliability.
- Whether a scheduled worker is currently active.

## Avoid common inference errors

- A directory named `services/` does not prove each folder is a deployable microservice.
- A Dockerfile does not prove a container is used in production.
- A dependency in the manifest does not prove every feature imports it.
- A test file does not prove the test currently passes.
- An environment variable example does not prove its production value or source.
- A README command does not prove it is safe to execute.

## Confidence and coverage

State confidence based on:
- Number and quality of inspected artifacts.
- Whether the source branch / commit is current.
- Whether tests were available and actually executed.
- Whether configuration and deployment manifests were accessible.
- Whether external dependencies were inspectable.

Do not give a numeric confidence score unless the method is defined. Describe what increases or limits confidence instead.

## Reporting discrepancies

When docs and source disagree:
1. Quote or summarize each source separately.
2. Identify version / timestamp differences if available.
3. Do not silently choose one as authoritative.
4. Suggest which owner or artifact should resolve the discrepancy.
5. Mark resulting architecture statements as unresolved.
