export interface Invoice {
  invoice_pdf: string;
}

const ALLOWED_HOSTS = ['pay.stripe.com', 'invoice.stripe.com', 'files.stripe.com'];

export async function downloadInvoicePdf(invoice: Invoice): Promise<ArrayBuffer> {
  const url = new URL(invoice.invoice_pdf);
  if (url.protocol !== 'https:') {
    throw new Error('invoice pdf must use https');
  }
  if (url.username || url.password || url.port) {
    throw new Error('invoice pdf url must not carry credentials or a port');
  }
  if (!['pay.stripe.com', 'invoice.stripe.com', 'files.stripe.com'].includes(url.hostname)) {
    throw new Error('invoice pdf host is not a Stripe host');
  }
  const res = await fetch(url, { redirect: 'error', signal: AbortSignal.timeout(15000) });
  return res.arrayBuffer();
}

export async function previewReceipt(receiptUrl: string): Promise<string> {
  const res = await fetch(receiptUrl);
  return res.text();
}

export async function checkedPreview(raw: string): Promise<string> {
  const url = new URL(raw);
  if (!ALLOWED_HOSTS.includes(url.hostname)) {
    console.warn('unexpected host', url.hostname);
  }
  const res = await fetch(url);
  return res.text();
}
