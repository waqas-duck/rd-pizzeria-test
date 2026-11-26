from rubber_duck_pizzeria.receipt import receipt_text


def test_receipt_text():
    assert receipt_text([(250, 2)]) == "Total: 5.00"
