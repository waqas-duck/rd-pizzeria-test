export function unitPrice(cents: number, qty: number): number {
  if (qty <= 0) {
    return 0;
  }
  return Math.round(cents * qty * 0.95);
}
