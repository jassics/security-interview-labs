import importlib
import os

import pytest

impl = importlib.import_module(os.environ.get("IMPL", "longest_window_k_distinct_solution"))
longest = impl.longest_window_k_distinct


def test_basic():
    assert longest(["a", "b", "a", "c", "c"], 2) == 3


def test_k_one_finds_longest_run():
    assert longest(["a", "b", "b", "b", "c"], 1) == 3


def test_k_at_least_distinct_count_returns_everything():
    assert longest(["a", "b", "c"], 3) == 3
    assert longest(["a", "b", "c"], 10) == 3


def test_k_zero_returns_zero():
    assert longest(["a", "b"], 0) == 0


def test_empty_input():
    assert longest([], 2) == 0


def test_all_same():
    assert longest(["a"] * 6, 1) == 6


def test_negative_k_raises():
    with pytest.raises(ValueError):
        longest(["a"], -1)


def test_large_input_is_linear():
    ips = [str(i % 50) for i in range(400_000)]
    assert longest(ips, 5) == 5
