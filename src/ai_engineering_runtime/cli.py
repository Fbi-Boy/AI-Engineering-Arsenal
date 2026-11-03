"""Command-line entry point for inspecting the local skill registry."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from .registry import load_registry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="aea-runtime",
        description="Inspect AI Engineering Arsenal skill packages (no skill code is executed).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command, help_text in (
        ("list", "list discovered skill packages"),
        ("validate", "validate discovered skill manifests"),
    ):
        child = subparsers.add_parser(command, help=help_text)
        child.add_argument("--skills-dir", default="skills", help="path to the skills directory")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
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
