from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ai_engineering_runtime.frontmatter import FrontmatterError, parse_frontmatter
from ai_engineering_runtime.registry import load_registry


class FrontmatterTests(unittest.TestCase):
    def test_reads_required_fields_and_block_description(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / "SKILL.md"
            manifest.write_text(
                '---\nname: api-design\ndescription: |\n  Design safe APIs.\n  Include validation.\n---\n# Instructions\n',
                encoding="utf-8",
            )
            self.assertEqual(
                parse_frontmatter(manifest),
                {"name": "api-design", "description": "Design safe APIs.\nInclude validation."},
            )

    def test_rejects_duplicate_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            manifest = Path(temporary) / "SKILL.md"
            manifest.write_text("---\nname: first\nname: second\ndescription: useful\n---\n", encoding="utf-8")
            with self.assertRaisesRegex(FrontmatterError, "duplicate field"):
                parse_frontmatter(manifest)


class RegistryTests(unittest.TestCase):
    def _skill(self, root: Path, folder: str, name: str | None = None) -> None:
        package = root / folder
        package.mkdir()
        manifest_name = name or folder
        (package / "SKILL.md").write_text(
            f"---\nname: {manifest_name}\ndescription: A useful skill.\n---\n# Instructions\n",
            encoding="utf-8",
        )

    def test_discovers_valid_packages_in_stable_order(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._skill(root, "zeta")
            self._skill(root, "alpha")
            report = load_registry(root)
            self.assertTrue(report.is_valid)
            self.assertEqual([skill.name for skill in report.skills], ["alpha", "zeta"])

    def test_reports_directory_manifest_name_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._skill(root, "folder-name", "different-name")
            report = load_registry(root)
            self.assertFalse(report.is_valid)
            self.assertIn("does not match directory", report.issues[0].message)

    def test_rejects_skill_names_longer_than_64_characters(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self._skill(root, "a" * 65)
            report = load_registry(root)
            self.assertFalse(report.is_valid)
            self.assertIn("1-64 characters", report.issues[0].message)

    def test_rejects_descriptions_longer_than_1024_characters(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            package = root / "long-description"
            package.mkdir()
            (package / "SKILL.md").write_text(
                "---\nname: long-description\ndescription: " + ("x" * 1025) + "\n---\n",
                encoding="utf-8",
            )
            report = load_registry(root)
            self.assertFalse(report.is_valid)
            self.assertIn("1024 characters", report.issues[0].message)

    def test_missing_directory_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            report = load_registry(Path(temporary) / "missing")
            self.assertFalse(report.is_valid)
            self.assertEqual(report.skills, ())


if __name__ == "__main__":
    unittest.main()
