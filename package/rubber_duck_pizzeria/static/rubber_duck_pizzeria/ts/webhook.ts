import express from 'express';

export const hooks = express.Router();

hooks.post('/hooks/test', async (req, res) => {
  const { url } = req.body;
  const ping = await fetch(url, { method: 'POST', body: '{}' });
  res.json({ status: ping.status });
});
