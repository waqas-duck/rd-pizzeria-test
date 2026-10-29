"""Consumers of kitchen config (impact / rename labs)."""
from rubber_duck_pizzeria.config import config_values, get_setting


def kitchen_target() -> int:
    return int(config_values.get("kitchen_target", 0))


def promo_enabled(store: str) -> bool:
    return bool(get_setting(f"promo_enabled_{store}", False))


def timezone_label() -> str:
    return str(config_values.get("timezone", "UTC"))
