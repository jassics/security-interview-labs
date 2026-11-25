# DS-03: Strict IPv4 validator

**Pattern:** string parsing and edge cases · **Difficulty:** easy · **Suggested time:** 15 minutes · **Language:** Python

## Problem

Write `is_valid_ipv4(text)` that returns `True` only for strict dotted-decimal IPv4: exactly four parts, each a decimal number from 0 to 255 written with ASCII digits only, with **no leading zeros** (except the single digit `0`) and no spaces, signs or other characters.

```python
is_valid_ipv4("192.168.1.1")  # True
is_valid_ipv4("256.1.1.1")    # False
is_valid_ipv4("01.2.3.4")     # False
is_valid_ipv4("1.2.3")        # False
```

Do not use the `ipaddress` module.

## How to practise

Write it in `strict_ipv4.py`, then run `IMPL=strict_ipv4 pytest coding_round/dsa_warmups/03_strict_ipv4`.

## Hints

<details>
<summary>Hint 1</summary>

Split on `.` and check the count first. What does `"1..3.4".split(".")` give you?
</details>

<details>
<summary>Hint 2</summary>

`"١".isdigit()` returns `True` in Python, and `int("١")` works. Is that what you want from a validator?
</details>

<details>
<summary>Hint 3</summary>

Check the characters before you call `int`, and decide where the leading-zero rule belongs.
</details>

## What the interviewer listens for

- You ask what "valid" means before coding: leading zeros, whitespace, signs, hex forms.
- You think about the failure modes, not just the happy path.
- Security angle: parsers disagree about `01.2.3.4` (some read it as octal) and about forms like `0x7f.0.0.1`. That disagreement is how SSRF filters get bypassed: the validator accepts one meaning and the HTTP client uses another. A strict validator plus one canonical form is the defence.
- You notice that `isdigit()` and `isnumeric()` accept non-ASCII digits.

## Complexity

O(n) time, O(1) space.
