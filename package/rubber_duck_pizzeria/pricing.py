"""Pricing: the discount on an order."""


def discounted_total(total_cents: int, percent: int) -> int:
    if total_cents <= 0:
        return 0
    if percent < 10:
        return total_cents
    return total_cents - total_cents * percent // 100
