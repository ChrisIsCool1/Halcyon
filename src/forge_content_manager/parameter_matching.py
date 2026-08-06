"""Helpers for matching Forge parameter names against configured patterns."""

from __future__ import annotations

import fnmatch
import re
from collections.abc import Iterable


# Parameter values that name local SVars. Keep this in the shared matching
# module so documentation discovery and editor validation use the same rules.
SVAR_REFERENCE_PARAMETERS = (
    "Execute", "Triggers", "ReplaceWith", "*SubAbility*",
)

# Any Forge parameter whose name contains Description can provide a natural
# language description that is useful for Script Editor autofill.
DESCRIPTION_PARAMETERS = ("*Description*",)


def matches_parameter(name: str, patterns: Iterable[str]) -> bool:
    """Return whether ``name`` matches one of the configured glob patterns."""
    return any(fnmatch.fnmatchcase(name, pattern) for pattern in patterns)


def wildcard_patterns_to_regex(patterns: Iterable[str]) -> str:
    """Convert glob-style parameter patterns into a regex alternation."""
    alternatives = []
    for pattern in patterns:
        escaped = re.escape(pattern).replace(r"\*", ".*").replace(r"\?", ".")
        alternatives.append(escaped)
    return "|".join(sorted(alternatives, key=len, reverse=True))
