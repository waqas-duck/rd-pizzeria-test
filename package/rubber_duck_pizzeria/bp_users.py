"""Lab: bound parameters (dev only)."""

import sqlite3


def find_user(connection: sqlite3.Connection, username: str):
    query = f"SELECT id FROM users WHERE username = '{username}'"
    return connection.execute(query).fetchall()
