"""Display labels for the kitchen (moved out of services)."""
from rubber_duck_pizzeria.config import config_values


def timezone_label() -> str:
    return str(config_values.get("timezone", "UTC"))
