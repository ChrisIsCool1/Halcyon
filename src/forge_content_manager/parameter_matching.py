"""Helpers for matching Forge parameter names against configured patterns."""

from __future__ import annotations

import fnmatch
import re
from collections.abc import Iterable


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
