from rubber_duck_pizzeria.pricing import Basket, line_total, order_total


def test_line_total():
    assert line_total(250, 2) == 500


def test_order_total():
    assert order_total([(250, 2), (100, 1)]) == 600


def test_basket():
    assert Basket(250, 2).total == 500
