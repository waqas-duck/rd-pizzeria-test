import { unitPrice } from './pricing';

export function cartTotal(lines: Array<[number, number]>): number {
  return lines.reduce((sum, [cents, qty]) => sum + unitPrice(cents, qty), 0);
}
