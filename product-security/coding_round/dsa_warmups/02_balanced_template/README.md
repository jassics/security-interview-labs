# DS-02: Balanced template braces

**Pattern:** stack · **Difficulty:** easy · **Suggested time:** 10 to 15 minutes · **Language:** Python

## Problem

A template engine accepts text containing `()`, `[]` and `{}`. Return `True` if every bracket is closed by the right kind in the right order. All other characters are ignored.

```python
is_balanced("a(b[c]{d})e")  # True
is_balanced("([)]")         # False
is_balanced("((")           # False
```

## How to practise

Write it in `balanced_template.py`, then run `IMPL=balanced_template pytest coding_round/dsa_warmups/02_balanced_template`.

## Hints

<details>
<summary>Hint 1</summary>

The most recently opened bracket must be the first one closed. Which structure behaves that way?
</details>

<details>
<summary>Hint 2</summary>

Two failure cases are easy to forget: a closer with nothing open, and openers left over at the end.
</details>

## What the interviewer listens for

- You name the stack and explain why a counter alone fails on `([)]`.
- You cover the empty string and both leftover cases without prompting.
- Security angle: the last test uses 200,000 levels of nesting. A recursive solution would hit Python's recursion limit and crash. Untrusted input shape is a denial-of-service risk, so say so.

## Complexity

O(n) time, O(n) space. Classic pattern name: "valid parentheses".
