def menu_total(items):
    total = 0
    for item in items:
        total += item["price"] * item.get("qty", 1)
    return total
