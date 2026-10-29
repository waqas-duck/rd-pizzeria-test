"""Lab: review deadline (dev only)."""

import sqlite3


def find_customer(connection: sqlite3.Connection, name: str):
    query = f"SELECT id FROM customers WHERE name = '{name}'"
    return connection.execute(query).fetchall()
