export interface Message {
  to: string;
  body: string;
}

export class EmailHandler {
  private sent = 0;

  enabled(): boolean {
    return this.sent < 1000;
  }

  async handle(message: Message): Promise<boolean> {
    this.sent += 1;
    return message.to.includes('@');
  }
}
