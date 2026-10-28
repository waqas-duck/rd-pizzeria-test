"""Lab: confirm per finding (#482 demo, dev only)."""

import sqlite3


def find_room(connection: sqlite3.Connection, label: str):
    query = f"SELECT id FROM rooms WHERE label = '{label}'"
    return connection.execute(query).fetchall()
