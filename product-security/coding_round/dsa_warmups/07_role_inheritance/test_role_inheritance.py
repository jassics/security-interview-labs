import importlib
import os

impl = importlib.import_module(os.environ.get("IMPL", "role_inheritance_solution"))
effective = impl.effective_permissions
has_cycle = impl.has_inheritance_cycle

PARENTS = {"admin": ["editor"], "editor": ["viewer"], "viewer": []}
GRANTS = {"admin": {"delete"}, "editor": {"write"}, "viewer": {"read"}}


def test_inherits_through_the_chain():
    assert effective(PARENTS, GRANTS, "admin") == {"delete", "write", "read"}


def test_leaf_role_has_only_its_own_permissions():
    assert effective(PARENTS, GRANTS, "viewer") == {"read"}


def test_multiple_parents_and_diamond_shape():
    parents = {"d": ["b", "c"], "b": ["a"], "c": ["a"]}
    grants = {"a": {"p"}, "b": {"q"}, "c": {"r"}, "d": {"s"}}
    assert effective(parents, grants, "d") == {"p", "q", "r", "s"}


def test_unknown_role_has_no_permissions():
    assert effective(PARENTS, GRANTS, "ghost") == set()


def test_parent_missing_from_dicts_is_ignored():
    assert effective({"a": ["b"]}, {"a": {"x"}}, "a") == {"x"}


def test_effective_permissions_terminates_on_a_cycle():
    parents = {"a": ["b"], "b": ["a"]}
    grants = {"a": {"x"}, "b": {"y"}}
    assert effective(parents, grants, "a") == {"x", "y"}


def test_does_not_modify_inputs():
    parents = {"a": ["b"], "b": []}
    grants = {"a": {"x"}, "b": {"y"}}
    effective(parents, grants, "a")
    assert parents == {"a": ["b"], "b": []} and grants == {"a": {"x"}, "b": {"y"}}


def test_no_cycle_in_a_tree_and_a_diamond():
    assert has_cycle(PARENTS) is False
    assert has_cycle({"d": ["b", "c"], "b": ["a"], "c": ["a"], "a": []}) is False


def test_detects_two_node_cycle():
    assert has_cycle({"a": ["b"], "b": ["a"]}) is True


def test_detects_self_inheritance():
    assert has_cycle({"a": ["a"]}) is True


def test_detects_long_cycle():
    assert has_cycle({"a": ["b"], "b": ["c"], "c": ["d"], "d": ["a"]}) is True


def test_empty_graph():
    assert has_cycle({}) is False


def test_long_chain_does_not_hit_recursion_limit():
    n = 50_000
    parents = {i: [i + 1] for i in range(n)}
    parents[n] = []
    assert has_cycle(parents) is False
    parents[n] = [0]
    assert has_cycle(parents) is True
