"""Parse the small YAML frontmatter subset used by SKILL.md manifests.

The parser intentionally handles only top-level scalar fields and YAML block
scalars. It does not evaluate YAML tags, aliases, or arbitrary object graphs.
"""

from __future__ import annotations

import json
from pathlib import Path


class FrontmatterError(ValueError):
    """Raised when a SKILL.md header is malformed or incomplete."""


def _scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise FrontmatterError(f"invalid quoted scalar: {exc.msg}") from exc
        if not isinstance(parsed, str):
            raise FrontmatterError("manifest values must be strings")
        return parsed
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise FrontmatterError("unterminated single-quoted scalar")
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(path: Path) -> dict[str, str]:
    """Read name and description from a SKILL.md YAML frontmatter block."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        raise FrontmatterError(f"cannot read manifest: {exc}") from exc

    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("file must begin with a YAML frontmatter delimiter")

    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise FrontmatterError("missing closing frontmatter delimiter") from exc

    fields: dict[str, str] = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#") or line[0].isspace():
            i += 1
            continue
        if ":" not in line:
            raise FrontmatterError(f"invalid top-level field on line {i + 1}")
        key, raw = line.split(":", 1)
        key = key.strip()
        if not key or any(ch.isspace() for ch in key):
            raise FrontmatterError(f"invalid field name on line {i + 1}")
        if key in fields:
            raise FrontmatterError(f"duplicate field: {key}")
        raw = raw.strip()
        if raw in {"|", "|-", "|+", ">", ">-", ">+"}:
            block: list[str] = []
            i += 1
            while i < end:
                candidate = lines[i]
                if candidate and not candidate[0].isspace():
                    break
                block.append(candidate.strip())
                i += 1
            separator = "\n" if raw.startswith("|") else " "
            fields[key] = separator.join(part for part in block).strip()
            continue
        fields[key] = _scalar(raw)
        i += 1

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()
    if not name:
        raise FrontmatterError("required field 'name' is missing or empty")
    if not description:
        raise FrontmatterError("required field 'description' is missing or empty")
    return {"name": name, "description": description}
