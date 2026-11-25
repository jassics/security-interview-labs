# DS-04: Top K noisiest IPs

**Pattern:** counting with a hash map, sorting or a heap · **Difficulty:** easy to medium · **Suggested time:** 15 minutes · **Language:** Python

## Problem

Given a list of source IPs from a web log, return the `k` most frequent ones, most frequent first. If two IPs have the same count, the one that sorts first as a string comes first. `k = 0` returns an empty list; a `k` larger than the number of distinct IPs returns all of them; a negative `k` raises `ValueError`.

```python
top_k_ips(["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3"], 2)  # ["1.1.1.1", "2.2.2.2"]
```

## How to practise

Write it in `top_k_ips.py`, then run `IMPL=top_k_ips pytest coding_round/dsa_warmups/04_top_k_ips`.

## Hints

<details>
<summary>Hint 1</summary>

Count first, then rank. `collections.Counter` is allowed.
</details>

<details>
<summary>Hint 2</summary>

A sort key can be a tuple. How do you sort by count descending and name ascending at once?
</details>

<details>
<summary>Hint 3</summary>

Sorting everything is O(d log d) for d distinct IPs. A heap of size k gets O(d log k). When is that better?
</details>

## What the interviewer listens for

- You get a correct, simple solution first, then discuss the heap.
- You settle the tie-breaking rule up front, so the output is deterministic.
- Follow-ups: the log is 100 GB (a count-min sketch or sampling, or counting per shard and merging); you need the top IPs per hour (bucket by window); a few IPs behind one NAT are noisy but harmless (what would you add to the signal?).

## Complexity

Sorting: O(n + d log d). Heap: O(n + d log k). Classic pattern name: "top K frequent elements".
