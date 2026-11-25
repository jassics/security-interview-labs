import subprocess
import sys
from pathlib import Path

TEMPLATE = Path(__file__).with_name("stdin_template.py")


def run(stdin_text):
    result = subprocess.run(
        [sys.executable, str(TEMPLATE)], input=stdin_text, capture_output=True, text=True, timeout=10
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_sample_input():
    assert run("3\n1 2 3\n") == "6\n"


def test_numbers_split_across_lines():
    assert run("4\n1 2\n3 4\n") == "10\n"


def test_no_trailing_newline():
    assert run("2\n5 5") == "10\n"
