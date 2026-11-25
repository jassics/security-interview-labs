"""DS-08 reference solution."""


def first_vulnerable_version(n, is_vulnerable):
    """Smallest version in 1..n for which is_vulnerable(version) is True, or None.

    Versions are numbered 1..n and once a version is vulnerable every later one is too.
    """
    low, high = 1, n + 1  # the answer is in [low, high]; high means "none"
    while low < high:
        mid = (low + high) // 2
        if is_vulnerable(mid):
            high = mid
        else:
            low = mid + 1
    return low if low <= n else None
