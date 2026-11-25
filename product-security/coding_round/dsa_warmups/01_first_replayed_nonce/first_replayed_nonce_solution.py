"""DS-01 reference solution."""


def first_replayed_nonce(events):
    """Return the first nonce whose second occurrence appears, or None."""
    seen = set()
    for nonce in events:
        if nonce in seen:
            return nonce
        seen.add(nonce)
    return None
