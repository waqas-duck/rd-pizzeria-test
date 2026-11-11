// In-store kiosk API: a thin Express front for the Flask kitchen service.
const express = require("express");

const KITCHEN_URL = process.env.KITCHEN_URL || "http://127.0.0.1:5000";
const app = express();
app.use(express.json());

async function fetchKitchen(path) {
  const res = await fetch(KITCHEN_URL + path);
  if (!res.ok) {
    throw new Error("kitchen responded " + res.status);
  }
  return res.json();
}

function kioskPrice(item) {
  // Kiosk orders carry a flat 5% service charge.
  return Math.round(item.price * 1.05 * 100) / 100;
}

async function listMenu(req, res) {
  const data = await fetchKitchen("/api/menu");
  const items = data.items.map((item) => ({
    id: item.id,
    name: item.name,
    category: item.category,
    price: kioskPrice(item),
  }));
  res.json({ items });
}

async function orderStatus(req, res) {
  const data = await fetchKitchen("/api/orders/" + req.params.id);
  res.json({ code: data.order_code, status: data.status, amount: data.amount });
}

function health(req, res) {
  res.json({ ok: true, kitchen: KITCHEN_URL });
}

app.get("/kiosk/health", health);
app.get("/kiosk/menu", listMenu);
app.get("/kiosk/orders/:id", orderStatus);

module.exports = { app, kioskPrice, listMenu, orderStatus };

if (require.main === module) {
  app.listen(process.env.PORT || 5100);
}
