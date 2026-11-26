export function pushToDataLayer(event: Record<string, unknown>): void {
  const w = window as unknown as { dataLayer?: unknown[] };
  w.dataLayer = w.dataLayer || [];
  w.dataLayer.push(event);
}
