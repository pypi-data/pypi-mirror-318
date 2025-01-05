import itertools

import more_itertools
import pytest

from rust_itertools import (
    combinations,
    combinations_with_replacement,
    derangements,
    derangements_range,
    distinct_permutations,
    permutations,
    powerset,
)


def derangements_range_py(n):
    """Yield successive distinct derangements of the range up to *n*.

    >>> sorted(derangements_range_py(3))
    [(1, 2, 0), (2, 0, 1)]
    """
    if n == 2:
        yield 1, 0
    elif n == 1:
        yield from []
    elif n == 0:
        yield ()
    else:
        lag1 = derangements_range_py(n - 1)
        for lag in lag1:
            for split in range(len(lag)):
                yield lag[0:split] + (n - 1,) + lag[split + 1 :] + (lag[split],)

        lag2 = derangements_range_py(n - 2)
        for lag in lag2:
            yield lag + (n - 1, n - 2)
            for k in range(n - 3, -1, -1):
                i = lag.index(k)
                lag = lag[:i] + (k + 1,) + lag[i + 1 :]
                yield lag[:k] + (n - 1,) + lag[k:] + (k,)


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8, 9])
def test_derangement_range(k):
    assert len(derangements_range(k)) == len(list(derangements_range_py(k)))


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8, 9])
def test_derangements(k):
    assert len(derangements(range(k))) == len(list(derangements_range(k)))


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8])
def test_permutations(k):
    assert len(permutations(range(k))) == len(list(itertools.permutations(range(k))))
    assert len(permutations(range(9), k)) == len(list(itertools.permutations(range(9), k)))


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8])
def test_distinct_permutations(k):
    assert len(distinct_permutations(range(k))) == len(list(more_itertools.distinct_permutations(range(k))))
    assert len(distinct_permutations(range(9), k)) == len(list(distinct_permutations(range(9), k)))
    assert len(distinct_permutations(range(k))) == len(permutations(range(k)))


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8])
def test_combinations(k):
    assert len(combinations(range(9), k)) == len(list(itertools.combinations(range(9), k)))


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8])
def test_combinations_with_replacement(k):
    assert len(combinations_with_replacement(range(9), k)) == len(
        list(itertools.combinations_with_replacement(range(9), k))
    )


@pytest.mark.parametrize('k', [0, 1, 2, 3, 4, 8])
def test_powerset(k):
    assert len(powerset(range(k))) == len(list(more_itertools.powerset(range(k))))
