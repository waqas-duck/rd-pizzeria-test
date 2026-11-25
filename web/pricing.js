// Prices shown in the web shop.
function deliveryFee(totalCents) {
  if (totalCents >= 6000) {
    return 0;
  }
  return 499;
}

function cartTotal(prices) {
  let sum = 0;
  for (const p of prices) {
    sum += p;
  }
  return sum + deliveryFee(sum);
}

module.exports = { deliveryFee, cartTotal };
