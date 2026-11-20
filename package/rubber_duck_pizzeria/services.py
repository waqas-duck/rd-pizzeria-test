"""Consumers of kitchen config (impact / rename labs)."""
from typing import Optional

from rubber_duck_pizzeria.config import config_values, get_setting


def kitchen_target() -> int:
    return int(config_values.get("kitchen_target", 0))


def promo_enabled() -> bool:
    return bool(get_setting("promo_enabled", False))


def timezone_label() -> str:
    return str(config_values.get("timezone", "UTC"))


def split_bill(total_cents: int, people: int) -> int:
    return total_cents // people


def customer_initial(name: Optional[str]) -> str:
    return name.strip()[0].upper()
