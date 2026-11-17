import { Message } from './email-handler';

export class SmsHandler {
  constructor(private readonly quota: number) {}

  enabled(): boolean {
    return this.quota > 0;
  }

  handle(message: Message): boolean {
    return message.body.length <= 160;
  }
}
