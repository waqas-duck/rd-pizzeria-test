import { cartTotal } from '../cart';

test('cart total', () => {
  expect(cartTotal([[250, 2]])).toBe(500);
});
