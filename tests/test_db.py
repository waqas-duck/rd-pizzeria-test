"""Review helpers in rubber_duck_pizzeria.db."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "package"))

from rubber_duck_pizzeria import db as dbmod  # noqa: E402


def setup_module(_module):
    dbmod.init_db(force=False)


def test_list_reviews_returns_published_newest_first():
    rows = dbmod.list_reviews()
    assert rows, "the seed data has published reviews"
    assert all(r["status"] == "published" for r in rows)
    ids = [r["id"] for r in rows]
    assert ids == sorted(ids, reverse=True)


def test_list_reviews_is_capped():
    assert len(dbmod.list_reviews(limit=2)) == 2


def test_add_review_is_listed():
    code = dbmod.add_review("Test Duck", "Great crust.", 4.0)
    assert code.startswith("#RD-")
    assert any(r["review_code"] == code for r in dbmod.list_reviews())
