"""Pricing: the discount on an order and the price of one item."""


def discounted_total(total_cents: int, percent: int) -> int:
    if total_cents <= 0:
        return 0
    if percent <= 0:
        return total_cents
    return total_cents - (total_cents * percent + 99) // 100


def price_per_item(total_cents: int, items: int) -> int:
    if items <= 0:
        return 0
    return total_cents // items
