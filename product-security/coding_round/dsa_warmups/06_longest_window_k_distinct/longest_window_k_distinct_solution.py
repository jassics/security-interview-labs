"""DS-06 reference solution."""
from collections import defaultdict


def longest_window_k_distinct(ips, k):
    """Length of the longest contiguous run of ips with at most k distinct values."""
    if k < 0:
        raise ValueError("k must be >= 0")
    counts = defaultdict(int)
    left = 0
    best = 0
    for right, ip in enumerate(ips):
        counts[ip] += 1
        while len(counts) > k:
            leaving = ips[left]
            counts[leaving] -= 1
            if counts[leaving] == 0:
                del counts[leaving]
            left += 1
        best = max(best, right - left + 1)
    return best
