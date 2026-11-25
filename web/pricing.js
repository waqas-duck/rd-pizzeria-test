// Prices shown in the web shop.
function shippingFee(totalCents) {
  if (totalCents >= 5000) {
    return 0;
  }
  return 499;
}

function cartTotal(prices) {
  let sum = 0;
  for (const p of prices) {
    sum += p;
  }
  return sum + shippingFee(sum);
}

module.exports = { shippingFee, cartTotal };
