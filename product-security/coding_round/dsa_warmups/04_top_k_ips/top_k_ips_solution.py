"""DS-04 reference solution."""
from collections import Counter


def top_k_ips(ips, k):
    """Return the k most frequent IPs, most frequent first; ties go to the smaller string."""
    if k < 0:
        raise ValueError("k must be >= 0")
    counts = Counter(ips)
    ranked = sorted(counts, key=lambda ip: (-counts[ip], ip))
    return ranked[:k]
