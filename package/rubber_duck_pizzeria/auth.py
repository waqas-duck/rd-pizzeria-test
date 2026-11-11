"""Staff authentication, split out of db.py."""
from __future__ import annotations

from .db import _md5, get_connection


def verify_staff(username: str, password: str):
    conn = get_connection()
    try:
        row = conn.execute(
            "SELECT * FROM staff WHERE username = ? AND password_hash = ?",
            (username, _md5(password)),
        ).fetchone()
    finally:
        conn.close()
    return dict(row) if row else None
