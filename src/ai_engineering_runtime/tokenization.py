"""Small, deterministic text normalization helpers for the baseline router."""

from __future__ import annotations

import re

_TOKEN = re.compile(r"[a-z0-9]+")
_STOP_WORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "buat", "by", "dari",
    "di", "do", "for", "in", "into", "is", "ke", "membuat", "of",
    "on", "or", "please", "saya", "the", "to", "untuk", "with", "yang",
})


def tokenize(text: str) -> tuple[str, ...]:
    """Return unique, lowercase alphanumeric terms in first-seen order."""
    seen: set[str] = set()
    terms: list[str] = []
    for token in _TOKEN.findall(text.casefold()):
        if token in _STOP_WORDS or len(token) < 2 or token in seen:
            continue
        seen.add(token)
        terms.append(token)
    return tuple(terms)


def normalized_skill_name(name: str) -> str:
    """Convert kebab-case skill names into searchable words."""
    return " ".join(tokenize(name.replace("-", " ")))
