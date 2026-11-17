export function buildIdempotencyKey(orderId: string, attempt: number): string {
  return `order:${orderId}:${attempt}`;
}
