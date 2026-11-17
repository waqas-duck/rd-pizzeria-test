export interface PaymentEvent {
  id: string;
  amount: number;
}

export class PaymentProcessor {
  private readonly prefix = 'pay';

  constructor(private readonly on: boolean) {}

  async process(event: PaymentEvent): Promise<string> {
    if (!this.on) {
      return 'skipped';
    }
    return `${this.prefix}:${event.id}`;
  }

  refund(event: PaymentEvent): string {
    return `refund:${event.id}`;
  }
}
