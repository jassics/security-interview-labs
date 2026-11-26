"""SV-06 (fixed): object-level authorization and a field allowlist."""

ALLOWED_PROFILE_FIELDS = {"name", "email"}


def make_db():
    from bola_vulnerable import make_db as _make
    return _make()


def get_order(db, current_user, order_id):
    """Same answer for 'missing' and 'not yours', so IDs cannot be probed."""
    order = db["orders"].get(order_id)
    if order is None or order["owner_id"] != current_user["id"]:
        raise KeyError("not found")
    return order


def update_profile(db, current_user, payload):
    unknown = set(payload) - ALLOWED_PROFILE_FIELDS
    if unknown:
        raise ValueError(f"fields not allowed: {sorted(unknown)}")
    user = db["users"][current_user["id"]]
    user.update(payload)
    return user
