# Root Cause Analysis — [Incident / Defect ID]

> **Status:** Investigating / Likely cause / Root cause confirmed / Resolved  
> **Date:** YYYY-MM-DD  
> **Service / feature:** [Name]  
> **Version / commit:** [Ref]  
> **Environment:** [Dev / Test / Staging / Production]  
> **Owner:** [Role]

## 1. Summary

[What failed, who / what was affected, and current status.]

## 2. Expected vs actual behavior

| Item | Description |
| --- | --- |
| Expected | [Behavior] |
| Actual | [Symptom] |
| Trigger / condition | [Input / event / timing] |
| Scope / impact | [Users / data / workflow / duration] |

## 3. Timeline

| Time (with timezone) | Event | Evidence |
| --- | --- | --- |
| [Timestamp] | [Observation / change / detection] | [Log / trace / deploy] |

## 4. Evidence and reproduction

**Environment / version:** [Details]

**Reproduction steps:**
1. [Step]
2. [Step]

**Evidence:** [Sanitized stack trace, log, trace ID, test, source path.]

**Reproducible:** Yes / No / Intermittent

## 5. Hypothesis matrix

| Hypothesis | Supporting evidence | Contradicting evidence | Test / result | Status |
| --- | --- | --- | --- | --- |
| H-001 | [Evidence] | [Evidence] | [Experiment] | Confirmed / Rejected / Open |

## 6. Root cause and causal chain

**Root cause:** [Confirmed mechanism or explicitly unresolved.]

**Trigger:** [Condition that activated it.]

**Contributing factors:** [Other conditions.]

**Detection gap:** [Why tests / alerts / controls did not detect it sooner.]

## 7. Correction and recovery

| Action | Purpose | Owner | Status | Verification |
| --- | --- | --- | --- | --- |
| [Fix / mitigation] | [Effect] | [Role] | Proposed | [Test / evidence] |

## 8. Prevention

- [ ] Regression test added / planned.
- [ ] Monitoring / alert / log improvement.
- [ ] Documentation / runbook update.
- [ ] Architecture / contract / policy review.
- [ ] Data repair or migration reviewed where relevant.

## 9. Validation results

| Check | Command / method | Result | Evidence |
| --- | --- | --- | --- |
| [Test] | [Command] | Not run / Pass / Fail | [Link / output] |

## 10. Remaining risks and open questions

- [Unknown / owner / next evidence]

> Do not mark the root cause confirmed or the incident resolved without supporting evidence. Production remediation remains subject to the system's authorization and incident process.
