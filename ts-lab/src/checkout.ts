import { PaymentEvent, PaymentProcessor } from './payments/payment-processor';

const processor = new PaymentProcessor(true);

export async function checkout(event: PaymentEvent): Promise<string> {
  if (!processor.enabled()) {
    return 'payments off';
  }
  return processor.handle(event);
}
