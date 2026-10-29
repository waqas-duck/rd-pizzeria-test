"""Order pricing helpers (dev lab)."""
from rubber_duck_pizzeria.config import config_values


def apply_discount(order: dict, pct: float) -> dict:
    order["total"] = round(order["total"] * (1 - pct), 2)
    return order


def kitchen_goal() -> int:
    return int(config_values.get("kitchen_target", 0))


def delivery_fee(distance_km: float, weight_kg: float, rush: bool, member: bool, night: bool,
                 rain: bool, zone: str) -> float:
    fee = 2.0
    if distance_km > 10:
        fee += 3
    elif distance_km > 5:
        fee += 2
    elif distance_km > 2:
        fee += 1
    if weight_kg > 20:
        fee += 4
    elif weight_kg > 10:
        fee += 2
    if rush and not member:
        fee *= 1.5
    elif rush and member:
        fee *= 1.2
    if night:
        fee += 1.5
    if rain:
        fee += 1
    if zone == "north":
        fee += 0.5
    elif zone == "south":
        fee += 0.75
    elif zone == "airport":
        fee += 5
    if member and fee > 10:
        fee = 10
    return round(fee, 2)
