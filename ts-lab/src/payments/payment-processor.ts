export interface PaymentEvent {
  id: string;
  amount: number;
}

export class PaymentProcessor {
  private readonly prefix = 'pay';

  constructor(private readonly on: boolean) {}

  enabled(): boolean {
    return this.on;
  }

  buildIdempotencyKey(event: PaymentEvent): string {
    return `${this.prefix}:${event.id}`;
  }

  async handle(event: PaymentEvent): Promise<string> {
    if (!this.enabled()) {
      return 'skipped';
    }
    return this.buildIdempotencyKey(event);
  }

  refund(event: PaymentEvent): string {
    return `refund:${event.id}`;
  }
}
