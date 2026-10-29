"""Lab: f-string query with a params tuple (row 8, dev only)."""

import sqlite3


def list_rooms(connection: sqlite3.Connection, building: str, sort: str):
    query = f"SELECT id FROM rooms WHERE building = ? ORDER BY {sort}"
    return connection.execute(query, (building,)).fetchall()
