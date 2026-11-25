import importlib
import os

import pytest

impl = importlib.import_module(os.environ.get("IMPL", "merge_access_windows_solution"))
merge = impl.merge_access_windows


def test_merges_overlapping():
    assert merge([(1, 5), (4, 8)]) == [(1, 8)]


def test_touching_windows_are_merged():
    assert merge([(1, 3), (3, 6)]) == [(1, 6)]


def test_disjoint_windows_stay_separate():
    assert merge([(1, 2), (4, 5)]) == [(1, 2), (4, 5)]


def test_unsorted_input():
    assert merge([(8, 10), (1, 3), (2, 6), (15, 18)]) == [(1, 6), (8, 10), (15, 18)]


def test_contained_window_is_absorbed():
    assert merge([(1, 10), (2, 3), (4, 5)]) == [(1, 10)]


def test_single_point_window():
    assert merge([(5, 5), (5, 5)]) == [(5, 5)]


def test_empty_input():
    assert merge([]) == []


def test_does_not_modify_input():
    windows = [(5, 6), (1, 2)]
    merge(windows)
    assert windows == [(5, 6), (1, 2)]


def test_invalid_window_raises():
    with pytest.raises(ValueError):
        merge([(5, 1)])
