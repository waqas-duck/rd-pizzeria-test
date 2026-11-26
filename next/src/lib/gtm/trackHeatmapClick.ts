import { pushToDataLayer } from '@/lib/gtm/pushToDataLayer';

export function clamp01(n: number): number {
  if (Number.isNaN(n)) return 0;
  return Math.round(Math.min(1, Math.max(0, n)) * 100) / 100;
}

export function trackHeatmapClick(x: number, y: number, width: number, height: number): void {
  if (width <= 0 || height <= 0) return;
  pushToDataLayer({ event: 'heatmap_click', x: clamp01(x / width), y: clamp01(y / height) });
}
