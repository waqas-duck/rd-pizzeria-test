'use client';
import { useEffect } from 'react';
import { trackHeatmapClick } from '@/lib/gtm/trackHeatmapClick';

export function InteractionTracker() {
  useEffect(() => {
    const onClick = (e: MouseEvent) =>
      trackHeatmapClick(e.clientX, e.clientY, window.innerWidth, window.innerHeight);
    document.addEventListener('click', onClick);
    return () => document.removeEventListener('click', onClick);
  }, []);
  return null;
}
