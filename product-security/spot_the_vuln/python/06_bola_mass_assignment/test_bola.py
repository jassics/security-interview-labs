import pytest

import bola_fixed
import bola_vulnerable


def asha():
    return {"id": 1}


def test_vulnerable_get_order_leaks_other_users_order():
    db = bola_vulnerable.make_db()
    order = bola_vulnerable.get_order(db, asha(), 102)  # Ravi's order
    assert order["address"] == "7 Brigade Road"


def test_vulnerable_profile_update_allows_role_change():
    db = bola_vulnerable.make_db()
    bola_vulnerable.update_profile(db, asha(), {"role": "admin"})
    assert db["users"][1]["role"] == "admin"


def test_fixed_get_order_blocks_other_users_order():
    db = bola_fixed.make_db()
    with pytest.raises(KeyError):
        bola_fixed.get_order(db, asha(), 102)


def test_fixed_missing_and_not_yours_look_the_same():
    db = bola_fixed.make_db()
    with pytest.raises(KeyError) as missing:
        bola_fixed.get_order(db, asha(), 999)
    with pytest.raises(KeyError) as not_yours:
        bola_fixed.get_order(db, asha(), 102)
    assert str(missing.value) == str(not_yours.value)


def test_fixed_own_order_still_works():
    db = bola_fixed.make_db()
    assert bola_fixed.get_order(db, asha(), 101)["item"] == "keyboard"


def test_fixed_profile_update_rejects_privileged_fields():
    db = bola_fixed.make_db()
    with pytest.raises(ValueError):
        bola_fixed.update_profile(db, asha(), {"role": "admin"})
    assert db["users"][1]["role"] == "customer"


def test_fixed_profile_update_allows_name_and_email():
    db = bola_fixed.make_db()
    bola_fixed.update_profile(db, asha(), {"name": "Asha K"})
    assert db["users"][1]["name"] == "Asha K"
