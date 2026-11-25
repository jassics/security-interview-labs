import importlib
import os

impl = importlib.import_module(os.environ.get("IMPL", "first_replayed_nonce_solution"))
find = impl.first_replayed_nonce


def test_returns_first_replay():
    assert find(["a", "b", "c", "b", "a"]) == "b"


def test_order_is_by_second_occurrence_not_first():
    assert find(["a", "b", "b", "a"]) == "b"


def test_no_replay_returns_none():
    assert find(["a", "b", "c"]) is None


def test_empty_input():
    assert find([]) is None


def test_single_event():
    assert find(["a"]) is None


def test_case_sensitive():
    assert find(["Abc", "abc"]) is None


def test_large_input_is_fast():
    events = [str(i) for i in range(200_000)] + ["199999"]
    assert find(events) == "199999"
