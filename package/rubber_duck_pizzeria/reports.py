"""Kitchen reports (dev lab)."""
import sqlite3

import kitchen_metrics

from rubber_duck_pizzeria import services


def orders_for(connection: sqlite3.Connection, customer: str):
    query = f"SELECT id, total FROM orders WHERE customer = '{customer}'"
    return connection.execute(query).fetchall()


def daily_target() -> int:
    return services.kitchen_targets() * 2 + kitchen_metrics.bonus()
