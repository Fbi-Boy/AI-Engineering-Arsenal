"""Explainable, provider-neutral baseline routing over discovered skills."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .models import SkillManifest
from .registry import load_registry
from .tokenization import normalized_skill_name, tokenize


@dataclass(frozen=True, slots=True)
class RoutingConfig:
    """Thresholds that make the router conservative and predictable."""

    min_score: float = 0.30
    ambiguity_margin: float = 0.08
    max_candidates: int = 5

    def __post_init__(self) -> None:
        if not 0.0 <= self.min_score <= 1.0:
            raise ValueError("min_score must be between 0 and 1")
        if not 0.0 <= self.ambiguity_margin <= 1.0:
            raise ValueError("ambiguity_margin must be between 0 and 1")
        if self.max_candidates < 1:
            raise ValueError("max_candidates must be at least 1")


@dataclass(frozen=True, slots=True)
class RouteCandidate:
    """A ranked skill candidate with a human-readable explanation."""

    skill: SkillManifest
    score: float
    matched_terms: tuple[str, ...]
    reasons: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class RouteDecision:
    """Routing outcome; selection is separate from skill execution."""

    status: Literal["selected", "ambiguous", "no_match"]
    selected: SkillManifest | None
    candidates: tuple[RouteCandidate, ...]
    query_terms: tuple[str, ...]
    explanation: str


def _score(query_terms: tuple[str, ...], skill: SkillManifest) -> RouteCandidate:
    name_terms = set(normalized_skill_name(skill.name).split())
    description_terms = set(tokenize(skill.description))
    searchable_terms = name_terms | description_terms
    matched = tuple(term for term in query_terms if term in searchable_terms)
    name_matches = tuple(term for term in query_terms if term in name_terms)

    coverage = len(matched) / len(query_terms)
    name_coverage = len(name_matches) / len(query_terms)
    score = min(1.0, (0.70 * coverage) + (0.30 * name_coverage))

    normalized_query = " ".join(query_terms)
    normalized_name = normalized_skill_name(skill.name)
    if normalized_name and normalized_name in normalized_query:
        score = min(1.0, score + 0.15)

    reasons: list[str] = []
    if matched:
        reasons.append("query terms found in skill name or description")
    if name_matches:
        reasons.append("skill name directly matches part of the request")
    if normalized_name and normalized_name in normalized_query:
        reasons.append("full skill name phrase matched")
    if not reasons:
        reasons.append("no meaningful term overlap")

    return RouteCandidate(
        skill=skill,
        score=round(score, 4),
        matched_terms=matched,
        reasons=tuple(reasons),
    )


def route_task(
    request: str,
    skills: tuple[SkillManifest, ...] | list[SkillManifest],
    config: RoutingConfig | None = None,
) -> RouteDecision:
    """Rank skill metadata against a request without invoking a model or skill."""
    settings = config or RoutingConfig()
    query_terms = tokenize(request)
    if not query_terms:
        return RouteDecision(
            "no_match", None, (), (), "Request contains no searchable terms."
        )

    ranked = sorted(
        (_score(query_terms, skill) for skill in skills),
        key=lambda candidate: (-candidate.score, candidate.skill.name),
    )
    candidates = tuple(ranked[: settings.max_candidates])
    if not candidates or candidates[0].score < settings.min_score:
        return RouteDecision(
            "no_match", None, candidates, query_terms,
            "No skill met the minimum relevance threshold.",
        )

    if len(candidates) > 1 and (
        candidates[0].score - candidates[1].score < settings.ambiguity_margin
    ):
        return RouteDecision(
            "ambiguous", None, candidates, query_terms,
            "Several skills have similar relevance; request clarification or use a higher-level planner.",
        )

    return RouteDecision(
        "selected", candidates[0].skill, candidates, query_terms,
        "Selected the highest-scoring skill using name and description overlap.",
    )


def route_from_registry(
    request: str,
    skills_dir: str = "skills",
    config: RoutingConfig | None = None,
) -> tuple[RouteDecision, tuple[str, ...]]:
    """Route against the local registry and return any registry diagnostics."""
    report = load_registry(skills_dir)
    decision = route_task(request, report.skills, config)
    diagnostics = tuple(f"{issue.path}: {issue.message}" for issue in report.issues)
    return decision, diagnostics
