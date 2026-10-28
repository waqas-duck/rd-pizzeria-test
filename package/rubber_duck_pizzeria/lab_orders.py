"""Lab: confirm per finding (#482 demo, dev only)."""

import sqlite3


def find_order(connection: sqlite3.Connection, customer: str):
    query = "SELECT id FROM orders WHERE customer = ?"
    return connection.execute(query, (customer,)).fetchall()
