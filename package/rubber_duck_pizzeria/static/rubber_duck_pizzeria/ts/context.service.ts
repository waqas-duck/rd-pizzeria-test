import { Injectable } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { internalUrl } from './internal-url';

@Injectable()
export class KitchenContextService {
  constructor(private readonly config: ConfigService) {}

  async get(kitchenId: string): Promise<unknown | null> {
    const base = this.config.get<string>('KITCHEN_SERVICE_URL')?.trim();
    if (!base || !/^[a-f\d]{24}$/i.test(kitchenId)) return null;
    const url = internalUrl(base, `/internal/kitchens/${kitchenId}/context`,
                            this.config.get<string>('KITCHEN_ALLOWED_ORIGINS'));
    const response = await fetch(url, { redirect: 'error', signal: AbortSignal.timeout(5000) });
    return response.ok ? response.json() : null;
  }
}
