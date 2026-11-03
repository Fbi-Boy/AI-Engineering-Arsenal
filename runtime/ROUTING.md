# Skill Routing Contract v0.1

The baseline router ranks the metadata of discovered skill packages. It uses
normalized token overlap against the skill name and description; it does not
call an LLM, inspect user files, execute skill instructions, or perform
external actions.

## Outcomes

- `selected`: one skill cleared the minimum score and the lead over the next
  candidate is at least the configured ambiguity margin.
- `ambiguous`: the top candidates are too close; no skill is selected.
- `no_match`: the request has no searchable terms or no candidate cleared
  the minimum relevance threshold.

Every candidate includes a score, matched terms, and reasons. Scores are
heuristic ranking signals, not calibrated probabilities.

## Safety boundary

A route decision is advisory. It is not authorization to execute a skill or
call a tool. Future execution layers must independently validate user intent,
skill compatibility, permissions, approval requirements, and runtime policy.

## Known limitations

Token overlap is language-sensitive and does not understand synonyms,
morphology, context, dependencies, or multi-step intent. Indonesian and
English common stop words are filtered, but the router is not a multilingual
semantic model. Ambiguous and low-confidence results should be clarified or
passed to a future model-backed planner rather than forced into a selection.
