# DS-01: First replayed nonce

**Pattern:** hash set · **Difficulty:** easy · **Suggested time:** 10 minutes · **Language:** Python

## Problem

An API requires each request to carry a one-time value called a nonce. Replaying an old nonce is an attack. Given the nonces in the order requests arrived, return the **first nonce that is seen a second time** (the one whose repeat comes earliest). Return `None` if every nonce is unique.

```python
first_replayed_nonce(["a", "b", "c", "b", "a"])  # "b"
first_replayed_nonce(["a", "b", "b", "a"])       # "b"
first_replayed_nonce(["a", "b", "c"])            # None
```

## How to practise

Write it in `first_replayed_nonce.py`, then run `IMPL=first_replayed_nonce pytest coding_round/dsa_warmups/01_first_replayed_nonce`.

## Hints

<details>
<summary>Hint</summary>

What do you need to remember about the nonces you have already seen, and which structure answers "have I seen this?" fastest?
</details>

## What the interviewer listens for

- You state the brute force (compare every pair, O(n²)) and then improve it.
- You ask: is the input a list or a stream? Can it be huge? Is it case sensitive?
- Security angle: in a real service the set must expire old nonces, or memory grows without bound and old nonces become valid again.

## Complexity

O(n) time, O(n) space. Classic pattern name for practice on public judges: "contains duplicate".
