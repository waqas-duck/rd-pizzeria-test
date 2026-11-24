"""Consumers of kitchen config (impact / rename labs)."""
from rubber_duck_pizzeria.config import config_values, get_setting


def kitchen_target() -> int:
    return int(config_values.get("kitchen_target", 0))


def promo_enabled() -> bool:
    return bool(get_setting("promo_enabled", False))


def timezone_label() -> str:
    return str(config_values.get("timezone", "UTC"))


def delivery_minutes(distance_km: float) -> int:
    return int(15 + distance_km * 4)
