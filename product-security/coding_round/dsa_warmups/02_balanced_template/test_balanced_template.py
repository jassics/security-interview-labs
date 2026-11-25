import importlib
import os

import pytest

impl = importlib.import_module(os.environ.get("IMPL", "balanced_template_solution"))
is_balanced = impl.is_balanced


@pytest.mark.parametrize("text", ["", "()", "([]{})", "a(b[c]{d})e", "{{[()]}}", "no brackets at all"])
def test_balanced(text):
    assert is_balanced(text) is True


@pytest.mark.parametrize("text", ["(", ")", "(]", "([)]", "((", "))", "{[}]", "a(b", "]["])
def test_not_balanced(text):
    assert is_balanced(text) is False


def test_deeply_nested_input_does_not_crash():
    depth = 200_000
    assert is_balanced("(" * depth + ")" * depth) is True
