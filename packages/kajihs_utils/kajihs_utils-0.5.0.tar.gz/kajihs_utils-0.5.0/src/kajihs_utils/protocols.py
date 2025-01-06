"""Useful protocols for structural subtyping."""

from typing import (
    Protocol,
    runtime_checkable,
)


@runtime_checkable
class SupportsLessThan[T](Protocol):
    """A protocol for objects supporting less-than comparisons."""

    def __lt__(self, other: T) -> bool: ...
