"""Lab: confirm per finding (#482 demo, dev only)."""

import sqlite3


def find_user(connection: sqlite3.Connection, username: str):
    query = "SELECT id FROM users WHERE username = ?"
    return connection.execute(query, (username,)).fetchall()
