"""Provider-neutral foundations for discovering and routing agent skills."""

from .models import RegistryIssue, RegistryReport, SkillManifest
from .registry import load_registry
from .routing import (
    RouteCandidate,
    RouteDecision,
    RoutingConfig,
    route_from_registry,
    route_task,
)

__all__ = [
    "RegistryIssue",
    "RegistryReport",
    "SkillManifest",
    "RouteCandidate",
    "RouteDecision",
    "RoutingConfig",
    "load_registry",
    "route_from_registry",
    "route_task",
]
__version__ = "0.1.0"
