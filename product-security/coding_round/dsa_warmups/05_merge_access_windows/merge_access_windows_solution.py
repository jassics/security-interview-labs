"""DS-05 reference solution."""


def merge_access_windows(windows):
    """Merge overlapping or touching (start, end) windows; return a sorted list of tuples."""
    for start, end in windows:
        if start > end:
            raise ValueError("window starts after it ends")
    merged = []
    for start, end in sorted(windows):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged
