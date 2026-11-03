from __future__ import annotations

import unittest

from ai_engineering_runtime.models import SkillManifest
from ai_engineering_runtime.routing import RoutingConfig, route_task
from ai_engineering_runtime.tokenization import tokenize


def skill(name: str, description: str) -> SkillManifest:
    return SkillManifest(name, description, f"skills/{name}", f"skills/{name}/SKILL.md")


class TokenizationTests(unittest.TestCase):
    def test_normalizes_case_and_removes_common_stop_words(self) -> None:
        self.assertEqual(tokenize("Build an API for the Backend"), ("build", "api", "backend"))


class RoutingTests(unittest.TestCase):
    def test_selects_best_skill_and_explains_match(self) -> None:
        skills = (
            skill("database-erd-design", "Model entities relationships and database schema"),
            skill("frontend-feature-implementation", "Build user interfaces and components"),
        )
        decision = route_task("Please design a database ERD schema", skills)
        self.assertEqual(decision.status, "selected")
        self.assertEqual(decision.selected.name, "database-erd-design")
        self.assertTrue(decision.candidates[0].matched_terms)

    def test_returns_no_match_for_unrelated_request(self) -> None:
        skills = (skill("api-design", "Design REST APIs and request validation"),)
        decision = route_task("write a poem about sunrise", skills)
        self.assertEqual(decision.status, "no_match")
        self.assertIsNone(decision.selected)

    def test_returns_no_match_for_empty_or_stopword_only_request(self) -> None:
        skills = (skill("api-design", "Design REST APIs"),)
        self.assertEqual(route_task("untuk yang di", skills).status, "no_match")
        self.assertEqual(route_task("", skills).status, "no_match")

    def test_marks_close_candidates_as_ambiguous(self) -> None:
        skills = (
            skill("backend-feature-implementation", "Implement backend service logic"),
            skill("backend-testing", "Test backend service behavior"),
        )
        decision = route_task("backend service", skills)
        self.assertEqual(decision.status, "ambiguous")
        self.assertIsNone(decision.selected)

    def test_config_rejects_invalid_thresholds(self) -> None:
        with self.assertRaises(ValueError):
            RoutingConfig(min_score=1.5)
        with self.assertRaises(ValueError):
            RoutingConfig(max_candidates=0)

    def test_candidate_limit_is_respected(self) -> None:
        skills = tuple(skill(f"skill-{index}", "Build software") for index in range(8))
        decision = route_task("build software", skills, RoutingConfig(max_candidates=3))
        self.assertEqual(len(decision.candidates), 3)


if __name__ == "__main__":
    unittest.main()
