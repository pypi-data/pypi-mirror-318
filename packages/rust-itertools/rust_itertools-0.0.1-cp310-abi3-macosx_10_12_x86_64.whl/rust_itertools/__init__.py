from collections.abc import Iterable, Sized
from typing import Any

from . import _rust_itertools

__all__ = (
    'VERSION',
    'derangements_range',
    'derangements',
    'permutations',
    'distinct_permutations',
    'combinations',
    'combinations_with_replacement',
    'pairwise',
    'repeat',
    'powerset',
)

# VERSION is set in Cargo.toml
VERSION = _rust_itertools.VERSION
derangements_range = _rust_itertools.derangements_range


def derangements(iterable: Sized, k: int | None = None) -> list[list[Any]]:
    return _rust_itertools.derangements(iterable, len(iterable) if k is None else k)


def permutations(iterable: Iterable[Any], k: int | None = None) -> list[list[Any]]:
    iterable = list(iterable)
    return _rust_itertools.permutations(iterable, len(iterable) if k is None else k)


def distinct_permutations(iterable: Sized, k: int | None = None) -> list[list[Any]]:
    return _rust_itertools.distinct_permutations(iterable, len(iterable) if k is None else k)


def combinations(iterable: Iterable[Any], k: int) -> list[list[Any]]:
    return _rust_itertools.combinations(list(iterable), k)


def combinations_with_replacement(iterable: Iterable[Any], k: int) -> list[list[Any]]:
    return _rust_itertools.combinations_with_replacement(list(iterable), k)


def powerset(iterable: Iterable[Any]) -> list[list[Any]]:
    return _rust_itertools.powerset(list(iterable))


# combinations = _rust_itertools.combinations
# combinations_with_replacement = _rust_itertools.combinations_with_replacement
pairwise = _rust_itertools.pairwise
repeat = _rust_itertools.repeat
# powerset = _rust_itertools.powerset
