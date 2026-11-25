"""DS-02 reference solution."""

_CLOSERS = {")": "(", "]": "[", "}": "{"}
_OPENERS = set(_CLOSERS.values())


def is_balanced(text):
    """True if every (), [] and {} in text is properly matched and nested."""
    stack = []
    for char in text:
        if char in _OPENERS:
            stack.append(char)
        elif char in _CLOSERS:
            if not stack or stack.pop() != _CLOSERS[char]:
                return False
    return not stack
