from rubber_duck_pizzeria.pricing import apply_discount


def test_apply_discount_takes_ten_percent_off():
    assert apply_discount({"total": 20.0}, 0.1)["total"] == 18.0
