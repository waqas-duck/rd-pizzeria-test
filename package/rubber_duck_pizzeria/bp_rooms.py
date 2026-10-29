"""Lab: bound parameters (dev only)."""

import sqlite3

ROOM_TABLE = "rooms"
DEFAULT_LIMIT = 50


def find_room(connection: sqlite3.Connection, label: str):
    query = f"SELECT id FROM rooms WHERE label = '{label}'"
    return connection.execute(query).fetchall()
