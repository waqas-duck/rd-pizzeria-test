"""Checkout: prices an order, applies a discount code and takes the payment."""
from typing import Dict, List

import requests
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from .pricing import discounted_total

db = SQLAlchemy()
DISCOUNT_CODES = {"DUCK10": 10, "DUCK5": 5}


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="open")
    total_cents = db.Column(db.Integer, default=0)
    payment_id = db.Column(db.String(64))


def order_status(paid: bool, items: int) -> str:
    if items <= 0:
        return "empty"
    return "paid" if paid else "pending"


def checkout(order_id: int, card_token: str, code: str) -> Dict:
    order = db.session.get(Order, order_id)
    if order is None or order.status != "open":
        return {"ok": False, "error": "this order cannot be paid"}
    if not card_token:
        return {"ok": False, "error": "no card"}
    amount = discounted_total(order.total_cents, DISCOUNT_CODES.get(code.strip().upper(), 0))
    charge = requests.post(current_app.config["PAYMENT_URL"],
                           json={"card": card_token, "amount": amount}, timeout=10).json()
    order.payment_id = charge["id"]
    order.status = "paid"
    db.session.commit()
    return {"ok": True, "amount": amount}


def order_totals(order_ids: List[int]) -> Dict[int, int]:
    orders = db.session.query(Order).filter(Order.id.in_(order_ids)).all()
    return {o.id: o.total_cents for o in orders}
