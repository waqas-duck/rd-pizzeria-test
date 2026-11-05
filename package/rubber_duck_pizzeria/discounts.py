def apply_discount(total, percent):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    cut = total * percent / 100
    return round(total - cut, 2)
