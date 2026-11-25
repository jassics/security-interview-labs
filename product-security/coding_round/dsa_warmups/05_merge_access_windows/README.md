# DS-05: Merge access windows

**Pattern:** sort then sweep (intervals) · **Difficulty:** medium · **Suggested time:** 20 minutes · **Language:** Python

## Problem

A just-in-time access system grants engineers time windows `(start, end)`, both as integer minutes and inclusive. Merge every window that overlaps or touches another, and return the result sorted by start as a list of tuples. A window with `start > end` is invalid and raises `ValueError`. Do not modify the input list.

```python
merge_access_windows([(8, 10), (1, 3), (2, 6), (15, 18)])  # [(1, 6), (8, 10), (15, 18)]
merge_access_windows([(1, 3), (3, 6)])                      # [(1, 6)]
```

## How to practise

Write it in `merge_access_windows.py`, then run `IMPL=merge_access_windows pytest coding_round/dsa_warmups/05_merge_access_windows`.

## Hints

<details>
<summary>Hint 1</summary>

If the windows were sorted by start, how many windows would you need to compare a new one against?
</details>

<details>
<summary>Hint 2</summary>

A window can be fully inside the previous one. Merging means taking the larger end, not just the new end.
</details>

## What the interviewer listens for

- You sort first and say why, and you state the cost (O(n log n)).
- You decide and say whether touching windows merge. Here they do.
- You use `max` for the end, which catches the "contained window" case.
- Security angle: this is how you compute continuous privileged access. Ask what happens at the boundary: if two grants touch, was the engineer privileged the whole time? Audit questions turn on that edge.

## Complexity

O(n log n) time, O(n) space. Classic pattern name: "merge intervals".
