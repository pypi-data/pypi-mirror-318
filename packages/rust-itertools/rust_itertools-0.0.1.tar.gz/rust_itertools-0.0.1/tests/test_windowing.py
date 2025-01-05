import itertools

from rust_itertools import pairwise


def test_pairwise():
    assert pairwise([0, 1, 2, 3, 4, 8, 9]) == list(itertools.pairwise([0, 1, 2, 3, 4, 8, 9]))
