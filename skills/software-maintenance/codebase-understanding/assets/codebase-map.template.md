# Codebase Map — [Repository / Project]

> **Repository:** [Owner / name / URL]  
> **Ref inspected:** [Branch / commit / tag]  
> **Date:** YYYY-MM-DD  
> **Inspection scope:** [Apps / packages / paths]  
> **Coverage:** Overview / Targeted feature trace / Partial

## 1. Executive overview

[What the project appears to do, based on evidence. Mark inference explicitly.]

## 2. Stack and tooling

| Area | Technology / version | Evidence | Confidence |
| --- | --- | --- | --- |
| Language | [Observed] | [Manifest / config path] | Direct / Inferred |
| Framework | [Observed] | [Manifest / imports] | Direct / Inferred |
| Runtime / build | [Observed] | [Scripts / config] | Direct / Inferred |
| Database / storage | [Observed] | [Config / migrations] | Direct / Inferred |
| Tests / quality | [Observed] | [Scripts / config] | Direct / Inferred |
| Deployment | [Observed / unknown] | [Manifest / docs] | Direct / Inferred / Unknown |

## 3. Top-level structure

| Path | Responsibility | Evidence | Notes |
| --- | --- | --- | --- |
| [Folder / file] | [Purpose] | [Key files / symbols] | [Unknowns] |

## 4. Architecture and boundaries

[Describe apps, packages, services, data stores, and external integrations. Distinguish logical modules from actual deployment units.]

## 5. Entry points and runtime flow

| Entry point | Trigger | Main path | Output / side effect |
| --- | --- | --- | --- |
| [Route / main / job] | [Trigger] | [Files / symbols] | [Result] |

## 6. Feature trace — [Target]

1. [User / external trigger]
2. [Route / handler]
3. [Validation / authorization]
4. [Domain / service logic]
5. [Persistence / external call]
6. [Response / event / UI update]
7. [Tests that cover the flow]

## 7. Developer workflow

| Task | Discovered command | Source | Executed? / Result |
| --- | --- | --- | --- |
| Install | [Command] | [Manifest / docs] | Not run |
| Dev | [Command] | [Source] | Not run |
| Test | [Command] | [Source] | Not run |
| Lint / type-check | [Command] | [Source] | Not run |
| Build | [Command] | [Source] | Not run |

## 8. Security and operational observations

[Visible auth / permissions, config and secrets patterns, logging, migrations, CI, support, and known gaps. Do not expose secret values.]

## 9. Unknowns and coverage limits

| Item | Why unknown | What would confirm it |
| --- | --- | --- |
| [Question] | [Evidence gap] | [File / runtime / owner] |

## 10. Next useful inspection

[Smallest set of files, tests, or owners to consult for the user's next objective.]

> This map describes the inspected ref and artifacts only. It is not a security audit or proof of runtime behavior.
