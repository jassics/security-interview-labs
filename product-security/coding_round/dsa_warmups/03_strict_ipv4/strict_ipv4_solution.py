"""DS-03 reference solution."""

_DIGITS = "0123456789"


def is_valid_ipv4(text):
    """Strict dotted-decimal IPv4: four ASCII-digit octets, 0 to 255, no leading zeros."""
    parts = text.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part or len(part) > 3:
            return False
        if any(char not in _DIGITS for char in part):  # str.isdigit() would accept other scripts
            return False
        if len(part) > 1 and part[0] == "0":
            return False
        if int(part) > 255:
            return False
    return True
