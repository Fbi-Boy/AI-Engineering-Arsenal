"""Command-line entry point for inspecting and planning local skills."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from .planning import TaskDraft, plan_workflow
from .registry import load_registry
from .routing import route_from_registry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aea-runtime",
        description="Inspect, route, and plan AI Engineering Arsenal skills (no skill code is executed).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command, help_text in (
        ("list", "list discovered skill packages"),
        ("validate", "validate discovered skill manifests"),
    ):
        child = subparsers.add_parser(command, help=help_text)
        child.add_argument("--skills-dir", default="skills", help="path to the skills directory")

    route = subparsers.add_parser("route", help="rank skills for a task request")
    route.add_argument("--request", required=True, help="user task request to route")
    route.add_argument("--skills-dir", default="skills", help="path to the skills directory")

    plan = subparsers.add_parser("plan", help="validate and schedule an explicit workflow task list")
    plan.add_argument("--input", required=True, help="path to workflow JSON input")
    plan.add_argument("--skills-dir", default="skills", help="path to the skills directory")
    return parser


def _load_task_drafts(path: str) -> tuple[TaskDraft, ...]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or set(payload) != {"tasks"}:
        raise ValueError("workflow JSON must be an object containing only a 'tasks' array")
    if not isinstance(payload["tasks"], list):
        raise ValueError("'tasks' must be an array")
    drafts: list[TaskDraft] = []
    allowed = {"id", "description", "depends_on", "acceptance_criteria"}
    for index, item in enumerate(payload["tasks"]):
        if not isinstance(item, dict) or set(item) - allowed:
            raise ValueError(f"task at index {index} must be an object with supported fields only")
        if not {"id", "description"} <= set(item):
            raise ValueError(f"task at index {index} requires 'id' and 'description'")
        if not isinstance(item["id"], str) or not isinstance(item["description"], str):
            raise ValueError(f"task at index {index}: 'id' and 'description' must be strings")
        dependencies = item.get("depends_on", [])
        criteria = item.get("acceptance_criteria", [])
        if not isinstance(dependencies, list) or not all(isinstance(value, str) for value in dependencies):
            raise ValueError(f"task at index {index}: 'depends_on' must be an array of strings")
        if not isinstance(criteria, list) or not all(isinstance(value, str) for value in criteria):
            raise ValueError(f"task at index {index}: 'acceptance_criteria' must be an array of strings")
        drafts.append(TaskDraft(item["id"], item["description"], tuple(dependencies), tuple(criteria)))
    return tuple(drafts)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "route":
        decision, diagnostics = route_from_registry(args.request, args.skills_dir)
        for candidate in decision.candidates:
            matched = ", ".join(candidate.matched_terms) or "none"
            print(f"{candidate.skill.name}\tscore={candidate.score:.4f}\tmatched={matched}")
        for diagnostic in diagnostics:
            print(f"WARNING: {diagnostic}")
        print(f"STATUS: {decision.status} - {decision.explanation}")
        if decision.selected:
            print(f"SELECTED: {decision.selected.name}")
        return 0 if decision.status == "selected" else 2

    if args.command == "plan":
        try:
            drafts = _load_task_drafts(args.input)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            print(f"ERROR: {exc}")
            return 1
        report = load_registry(args.skills_dir)
        plan = plan_workflow(drafts, report.skills)
        for issue in report.issues:
            print(f"WARNING: registry {issue.path}: {issue.message}")
        for issue in plan.issues:
            print(f"ERROR: {issue}")
        for task in plan.tasks:
            selected = task.route.selected.name if task.route.selected else "UNRESOLVED"
            print(f"TASK: {task.task_id}\tSKILL: {selected}\tROUTE: {task.route.status}")
            if task.route.selected is None:
                print(f"  {task.route.explanation}")
        for index, group in enumerate(plan.parallel_groups, start=1):
            print(f"WAVE {index}: {', '.join(group)}")
        print(f"STATUS: {plan.status} - {plan.explanation}")
        return {"ready": 0, "needs_clarification": 2, "invalid": 1}[plan.status]

    report = load_registry(args.skills_dir)
    if args.command == "list":
        for skill in report.skills:
            print(f"{skill.name}\t{skill.description}")
        if not report.skills:
            print("No valid skill packages discovered.")
    for issue in report.issues:
        print(f"ERROR: {issue.path}: {issue.message}")

    if args.command == "validate":
        print(f"Validated {len(report.skills)} skill package(s); {len(report.issues)} issue(s).")
    return 1 if report.issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
