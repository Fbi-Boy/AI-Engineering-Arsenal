"""Command-line entry point for inspecting and routing local skills."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from .registry import load_registry
from .routing import route_from_registry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aea-runtime",
        description="Inspect and route AI Engineering Arsenal skills (no skill code is executed).",
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
    return parser


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
