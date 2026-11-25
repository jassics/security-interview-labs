import importlib
import os

import pytest

impl = importlib.import_module(os.environ.get("IMPL", "top_k_ips_solution"))
top_k = impl.top_k_ips


def test_basic_ranking():
    ips = ["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3", "1.1.1.1", "2.2.2.2"]
    assert top_k(ips, 2) == ["1.1.1.1", "2.2.2.2"]


def test_ties_broken_by_smaller_string():
    ips = ["b", "a", "c", "a", "b", "c"]
    assert top_k(ips, 2) == ["a", "b"]


def test_k_larger_than_distinct_returns_all():
    assert top_k(["x", "y", "x"], 10) == ["x", "y"]


def test_k_zero_returns_empty():
    assert top_k(["x", "y"], 0) == []


def test_empty_input():
    assert top_k([], 3) == []


def test_negative_k_raises():
    with pytest.raises(ValueError):
        top_k(["x"], -1)


def test_large_input():
    ips = ["10.0.0.%d" % (i % 1000) for i in range(300_000)] + ["10.0.0.7"] * 5
    assert top_k(ips, 1) == ["10.0.0.7"]
