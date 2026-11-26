"""SV-06 (vulnerable): a tiny in-memory 'API' with two classic API bugs.

Intentionally insecure. Read it, find the bugs, then run the tests.
"""


def make_db():
    return {
        "users": {
            1: {"id": 1, "name": "Asha", "email": "asha@example.com", "role": "customer"},
            2: {"id": 2, "name": "Ravi", "email": "ravi@example.com", "role": "customer"},
        },
        "orders": {
            101: {"id": 101, "owner_id": 1, "item": "keyboard", "address": "12 MG Road"},
            102: {"id": 102, "owner_id": 2, "item": "monitor", "address": "7 Brigade Road"},
        },
    }


def get_order(db, current_user, order_id):
    """GET /orders/{id}"""
    order = db["orders"].get(order_id)
    if order is None:
        raise KeyError("not found")
    return order


def update_profile(db, current_user, payload):
    """PATCH /me with a JSON body"""
    user = db["users"][current_user["id"]]
    user.update(payload)
    return user
