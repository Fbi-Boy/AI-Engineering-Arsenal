"""Small immutable domain objects shared by runtime components."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SkillManifest:
    """Validated metadata for one on-disk skill package."""

    name: str
    description: str
    directory: str
    manifest_path: str


@dataclass(frozen=True, slots=True)
class RegistryIssue:
    """A non-fatal package discovery or validation problem."""

    path: str
    message: str


@dataclass(frozen=True, slots=True)
class RegistryReport:
    """Deterministic registry result, including packages and diagnostics."""

    skills: tuple[SkillManifest, ...]
    issues: tuple[RegistryIssue, ...]

    @property
    def is_valid(self) -> bool:
        return not self.issues
