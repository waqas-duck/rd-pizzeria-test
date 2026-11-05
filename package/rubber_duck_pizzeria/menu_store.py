import json


def load_menu(path):
    f = open(path)
    data = f.read()
    return json.loads(data)


def save_order(db, order):
    try:
        db.insert(order)
    except Exception:
        pass
