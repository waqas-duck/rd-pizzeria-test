"""Staff login against the seeded staff table."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "package"))

from rubber_duck_pizzeria import db as dbmod  # noqa: E402


def setup_module(_module):
    dbmod.init_db(force=False)


def test_authenticate_staff_accepts_the_seeded_manager():
    user = dbmod.authenticate_staff("admin", "admin123")
    assert user and user["role"] == "manager"


def test_wrong_password_is_rejected():
    assert dbmod.verify_staff("admin", "nope") is None
