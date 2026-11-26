import { pushToDataLayer } from '@/lib/gtm/pushToDataLayer';

export function clamp01(n: number): number {
  return Math.min(1, Math.max(0, n));
}

export function trackHeatmapClick(x: number, y: number, width: number, height: number): void {
  pushToDataLayer({ event: 'heatmap_click', x: clamp01(x / width), y: clamp01(y / height) });
}
