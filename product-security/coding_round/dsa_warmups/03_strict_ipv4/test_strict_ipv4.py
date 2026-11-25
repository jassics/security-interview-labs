import importlib
import os

import pytest

impl = importlib.import_module(os.environ.get("IMPL", "strict_ipv4_solution"))
is_valid_ipv4 = impl.is_valid_ipv4


@pytest.mark.parametrize("text", ["0.0.0.0", "1.2.3.4", "192.168.1.1", "255.255.255.255", "10.0.0.10"])
def test_valid(text):
    assert is_valid_ipv4(text) is True


@pytest.mark.parametrize(
    "text",
    [
        "",
        "1.2.3",
        "1.2.3.4.5",
        "1..3.4",
        "1.2.3.",
        ".1.2.3",
        "256.1.1.1",
        "1.2.3.999",
        "01.2.3.4",
        "1.2.3.04",
        "00.0.0.0",
        "1.2.3.-4",
        "+1.2.3.4",
        " 1.2.3.4",
        "1.2.3.4 ",
        "1.2.3.4\n",
        "a.b.c.d",
        "1.2.3.4a",
        "0x7f.0.0.1",
        "1.2.3.1000",
        "١.2.3.4",   # Arabic-indic digit one: str.isdigit() is True for it
        "１.2.3.4",   # fullwidth digit one
    ],
)
def test_invalid(text):
    assert is_valid_ipv4(text) is False
