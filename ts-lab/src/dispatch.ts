import { EmailHandler, Message } from './notifications/email-handler';
import { SmsHandler } from './notifications/sms-handler';
import { buildIdempotencyKey } from './orders/order-keys';

const email = new EmailHandler();
const sms = new SmsHandler(10);

export async function notify(message: Message): Promise<string[]> {
  const sent: string[] = [];
  if (email.enabled()) {
    await email.handle(message);
    sent.push('email');
  }
  if (sms.enabled()) {
    sms.handle(message);
    sent.push('sms');
  }
  return sent;
}

export function orderKeys(orderId: string): string[] {
  return [buildIdempotencyKey(orderId, 1), buildIdempotencyKey(orderId, 2)];
}

export async function retry(message: Message): Promise<boolean> {
  return email.enabled() ? email.handle(message) : sms.handle(message);
}
