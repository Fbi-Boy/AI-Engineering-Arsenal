# Code Review Finding Severity Guide

Severity should reflect the consequence and likelihood of the issue in the affected context, not the reviewer's frustration or code-style preference.

## Blocker

A finding that makes the change unsafe to merge under normal policy:
- Broad data loss or corruption.
- Critical authentication / authorization bypass.
- Remote code execution or severe secret exposure.
- Major outage or irreversible destructive behavior.
- A mandatory compatibility or compliance control is broken.

State the exact trigger and why it blocks the merge.

## High

A material defect likely to affect important functionality or a significant subset of users:
- Incorrect business rule or calculation.
- Object-level access flaw in a meaningful path.
- Transaction / consistency bug causing material incorrect state.
- Critical workflow reliably fails under common conditions.

## Medium

A defect or risk with narrower conditions or bounded impact:
- Important edge case fails.
- Error recovery is incomplete.
- Compatibility or performance issue affects a particular usage pattern.
- Missing validation causes inconsistent state under a specific condition.

## Low

A limited issue with small user or maintenance impact:
- Minor behavior mismatch.
- Non-critical error message issue.
- Small maintainability issue that creates a plausible future defect.

Do not use Low to report purely subjective style preferences.

## Question

Use when correctness depends on missing evidence, product policy, runtime behavior, or an assumption that the author / owner must confirm.

A question is not a proven defect. Explain what evidence or decision would resolve it.

## Suggestion

Use for optional design / maintainability improvement when the current code is not demonstrably wrong. Keep suggestions separate from required fixes.

## Confidence

Confidence describes evidence quality:
- High: direct code path or test demonstrates the issue.
- Medium: source strongly indicates the issue; runtime evidence is absent.
- Low: plausible concern needing investigation.

Do not combine severity and confidence. A potentially severe issue may have low confidence and should be framed as a question until verified.
