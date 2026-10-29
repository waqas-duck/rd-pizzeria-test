"""Lab: allow-listed ORDER BY and argv lists (dev only). Both functions are safe."""

import sqlite3
import subprocess

SORT_COLUMNS = {"id": "o.id", "date": "o.created_at", "total": "o.total"}


def list_orders(connection: sqlite3.Connection, customer: str, sort: str, direction: str):
    sort = SORT_COLUMNS.get(sort, "o.id")
    direction = "ASC" if direction.lower() == "asc" else "DESC"
    query = f"SELECT o.id FROM orders o WHERE o.customer = ? ORDER BY {sort} {direction}"
    return connection.execute(query, (customer,)).fetchall()


def safe_shell_lookup(host: str):
    return subprocess.run(["nslookup", host], shell=False, capture_output=True, text=True).stdout
