"""Lab: raw ORDER BY and a shell argv (dev only). Both functions are injectable."""

import sqlite3
import subprocess


def list_orders_raw(connection: sqlite3.Connection, customer: str, sort: str):
    query = f"SELECT o.id FROM orders o WHERE o.customer = ? ORDER BY {sort}"
    return connection.execute(query, (customer,)).fetchall()


def shell_lookup(host: str):
    return subprocess.run(["sh", "-c", "nslookup " + host], capture_output=True, text=True).stdout
