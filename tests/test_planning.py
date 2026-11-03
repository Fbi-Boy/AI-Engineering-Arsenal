from ai_engineering_runtime.models import SkillManifest
from ai_engineering_runtime.planning import TaskDraft, plan_workflow


SKILLS = (
    SkillManifest("api-design", "design REST APIs and contracts", "skills/api-design", "SKILL.md"),
    SkillManifest("database-design", "design database schemas and ERD", "skills/database-design", "SKILL.md"),
)


def draft(task_id, description, depends_on=()):
    return TaskDraft(task_id, description, tuple(depends_on), ("Deliver reviewed output",))


def test_builds_stable_parallel_waves_and_dependency_order():
    plan = plan_workflow((
        draft("requirements", "write API requirements"),
        draft("schema", "design database schema"),
        draft("contract", "design REST API contract", ("requirements",)),
    ), SKILLS)
    assert plan.status == "ready"
    assert plan.parallel_groups == (("requirements", "schema"), ("contract",))
    assert plan.execution_order == ("requirements", "schema", "contract")
    assert all(task.route.selected is not None for task in plan.tasks)


def test_reports_unknown_dependency():
    plan = plan_workflow((draft("api", "design REST API", ("missing",)),), SKILLS)
    assert plan.status == "invalid"
    assert "unknown task" in plan.issues[0]


def test_detects_dependency_cycle():
    plan = plan_workflow((
        draft("a", "design REST API", ("b",)),
        draft("b", "design database schema", ("a",)),
    ), SKILLS)
    assert plan.status == "invalid"
    assert "cycle" in plan.issues[0]


def test_duplicate_ids_are_invalid():
    plan = plan_workflow((draft("same", "design REST API"), draft("same", "design database schema")), SKILLS)
    assert plan.status == "invalid"
    assert any("duplicate" in issue for issue in plan.issues)


def test_missing_acceptance_criteria_are_invalid():
    plan = plan_workflow((TaskDraft("api", "design REST API"),), SKILLS)
    assert plan.status == "invalid"
    assert any("acceptance criteria" in issue for issue in plan.issues)


def test_unmatched_task_requires_clarification_not_silent_assignment():
    plan = plan_workflow((draft("unknown", "prepare a catering menu"),), SKILLS)
    assert plan.status == "needs_clarification"
    assert plan.tasks[0].route.status == "no_match"
    assert plan.execution_order == ("unknown",)
