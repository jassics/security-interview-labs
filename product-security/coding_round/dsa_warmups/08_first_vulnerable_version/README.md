# DS-08: First vulnerable version

**Pattern:** binary search on an answer · **Difficulty:** medium · **Suggested time:** 20 minutes · **Language:** Python

## Problem

Releases are numbered `1..n`. A vulnerability was introduced in some release, and every later release has it too. You can call `is_vulnerable(version)`, but each call runs a slow scan, so use as few calls as possible.

Return the **first vulnerable version**, or `None` if none of `1..n` is vulnerable.

```python
# versions 1..10, vulnerable from 6 onward
first_vulnerable_version(10, lambda v: v >= 6)  # 6
first_vulnerable_version(10, lambda v: False)   # None
```

## How to practise

Write it in `first_vulnerable_version.py`, then run `IMPL=first_vulnerable_version pytest coding_round/dsa_warmups/08_first_vulnerable_version`. The tests count your calls.

## Hints

<details>
<summary>Hint 1</summary>

The results look like `False False False True True True`. What does that shape let you skip?
</details>

<details>
<summary>Hint 2</summary>

Decide what your two pointers mean *before* writing the loop (for example, "the answer is somewhere in `[low, high]`"). Most bugs here are off-by-one errors from vague pointers.
</details>

<details>
<summary>Hint 3</summary>

`(low + high) // 2` is fine in Python. In Java or C++ with 32-bit integers, what could go wrong with `low + high`?
</details>

## What the interviewer listens for

- You see the monotonic shape and say binary search, and you explain the invariant that keeps the loop correct.
- You handle "none vulnerable" and `n = 0` without special-casing by accident.
- You mention integer overflow in fixed-width languages (`low + (high - low) / 2`).
- Security angle: this is `git bisect` for regressions and for finding when a vulnerable dependency or a bad config first shipped. It is also how you find the first release affected by a CVE with few scans.

## Complexity

O(log n) calls, O(1) space. Classic pattern name: "first bad version".
