import itertools

from rust_itertools import repeat


def test_repeat():
    assert repeat(3, 10) == list(itertools.repeat(3, 10))
