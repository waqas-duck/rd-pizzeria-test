"""The text printed on a receipt."""
from typing import List, Tuple

from rubber_duck_pizzeria.pricing import order_total


def receipt_text(lines: List[Tuple[int, int]]) -> str:
    return f"Total: {order_total(lines) / 100:.2f}"
