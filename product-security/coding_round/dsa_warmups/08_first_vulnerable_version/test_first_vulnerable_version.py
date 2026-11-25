import importlib
import math
import os

impl = importlib.import_module(os.environ.get("IMPL", "first_vulnerable_version_solution"))
first = impl.first_vulnerable_version


class Oracle:
    """Counts how many times the (pretend expensive) check is called."""

    def __init__(self, first_bad):
        self.first_bad = first_bad
        self.calls = 0

    def __call__(self, version):
        self.calls += 1
        return self.first_bad is not None and version >= self.first_bad


def test_finds_middle_version():
    assert first(10, Oracle(6)) == 6


def test_first_version_is_the_bad_one():
    assert first(10, Oracle(1)) == 1


def test_last_version_is_the_bad_one():
    assert first(10, Oracle(10)) == 10


def test_no_vulnerable_version_returns_none():
    assert first(10, Oracle(None)) is None


def test_single_version():
    assert first(1, Oracle(1)) == 1
    assert first(1, Oracle(None)) is None


def test_zero_versions_returns_none():
    assert first(0, Oracle(None)) is None


def test_uses_logarithmic_number_of_checks():
    n = 1_000_000
    oracle = Oracle(734_521)
    assert first(n, oracle) == 734_521
    assert oracle.calls <= math.ceil(math.log2(n + 1)) + 1


def test_no_version_found_is_also_logarithmic():
    n = 1_000_000
    oracle = Oracle(None)
    assert first(n, oracle) is None
    assert oracle.calls <= math.ceil(math.log2(n + 1)) + 1
