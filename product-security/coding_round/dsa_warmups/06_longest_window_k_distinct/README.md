# DS-06: Longest window with at most K distinct IPs

**Pattern:** sliding window with a hash map · **Difficulty:** medium · **Suggested time:** 20 to 25 minutes · **Language:** Python

## Problem

Given a list of source IPs in request order and an integer `k`, return the length of the longest **contiguous** run that contains at most `k` distinct IPs. A negative `k` raises `ValueError`. `k = 0` gives 0.

```python
longest_window_k_distinct(["a", "b", "a", "c", "c"], 2)  # 3  (a, b, a)
longest_window_k_distinct(["a", "b", "b", "b", "c"], 1)  # 3
```

## How to practise

Write it in `longest_window_k_distinct.py`, then run `IMPL=longest_window_k_distinct pytest coding_round/dsa_warmups/06_longest_window_k_distinct`.

## Hints

<details>
<summary>Hint 1</summary>

Keep a window with two pointers. When you add a new IP on the right and the window has too many distinct IPs, what do you do on the left?
</details>

<details>
<summary>Hint 2</summary>

A count per IP is enough to know when an IP has fully left the window. Remember to delete it from the map when its count reaches zero.
</details>

## What the interviewer listens for

- You start from the O(n²) idea (try every start) and explain why the two-pointer version is O(n): each index enters and leaves the window once.
- You handle `k = 0`, empty input and `k` larger than the number of distinct values.
- Security angle: a long run from only a few IPs is a signal (a bot, a scanner, or a shared NAT). Be ready to discuss what you would do with the answer, and how a time-based window differs from a count-based one.

## Complexity

O(n) time, O(k) space. Classic pattern name: "longest substring with at most K distinct characters".
