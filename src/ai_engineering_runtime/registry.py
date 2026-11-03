"""Filesystem-backed skill discovery with deterministic, safe defaults."""

from __future__ import annotations

import re
from pathlib import Path

from .frontmatter import FrontmatterError, parse_frontmatter
from .models import RegistryIssue, RegistryReport, SkillManifest

_SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_registry(skills_dir: str | Path = "skills") -> RegistryReport:
    """Discover immediate child skill packages without executing their content.

    A package is recognized only when it is a real directory containing a
    regular SKILL.md file. Symlinked package directories/manifests are rejected
    so discovery cannot escape the configured skills root.
    """
    root = Path(skills_dir)
    if not root.exists():
        return RegistryReport((), (RegistryIssue(str(root), "skills directory does not exist"),))
    if not root.is_dir():
        return RegistryReport((), (RegistryIssue(str(root), "skills path is not a directory"),))

    root_resolved = root.resolve()
    skills: list[SkillManifest] = []
    issues: list[RegistryIssue] = []
    seen_names: set[str] = set()

    try:
        children = sorted(root.iterdir(), key=lambda item: item.name.casefold())
    except OSError as exc:
        return RegistryReport((), (RegistryIssue(str(root), f"cannot list skills directory: {exc}"),))

    for package_dir in children:
        if package_dir.is_symlink():
            if package_dir.is_dir():
                issues.append(RegistryIssue(str(package_dir), "symlinked skill directories are not allowed"))
            continue
        if not package_dir.is_dir():
            continue

        manifest = package_dir / "SKILL.md"
        if not manifest.exists():
            continue
        if manifest.is_symlink() or not manifest.is_file():
            issues.append(RegistryIssue(str(manifest), "manifest must be a regular, non-symlink file"))
            continue
        try:
            manifest.resolve(strict=True).relative_to(root_resolved)
        except (OSError, ValueError):
            issues.append(RegistryIssue(str(manifest), "manifest resolves outside the skills directory"))
            continue

        try:
            metadata = parse_frontmatter(manifest)
        except FrontmatterError as exc:
            issues.append(RegistryIssue(str(manifest), str(exc)))
            continue

        name = metadata["name"]
        if not _SKILL_NAME.fullmatch(name):
            issues.append(RegistryIssue(str(manifest), "skill name must be lowercase kebab-case"))
            continue
        if name != package_dir.name:
            issues.append(RegistryIssue(str(manifest), f"manifest name '{name}' does not match directory '{package_dir.name}'"))
            continue
        if name in seen_names:
            issues.append(RegistryIssue(str(manifest), f"duplicate skill name: {name}"))
            continue

        seen_names.add(name)
        skills.append(
            SkillManifest(
                name=name,
                description=metadata["description"],
                directory=str(package_dir),
                manifest_path=str(manifest),
            )
        )

    return RegistryReport(tuple(skills), tuple(issues))
