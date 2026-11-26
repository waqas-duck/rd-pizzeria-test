"""Prices for order lines and whole orders."""
from typing import List, Tuple


def line_total(price_cents: int, qty: int) -> int:
    if qty <= 0:
        return 0
    return price_cents * qty


def order_total(lines: List[Tuple[int, int]]) -> int:
    return sum(line_total(price, qty) for price, qty in lines)


class Basket:
    def __init__(self, price_cents: int, qty: int):
        self.total = line_total(price_cents, qty)
