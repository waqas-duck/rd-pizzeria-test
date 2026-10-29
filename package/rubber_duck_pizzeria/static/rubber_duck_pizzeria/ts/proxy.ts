import express from 'express';

export const proxy = express.Router();

proxy.get('/proxy', async (req, res) => {
  const upstream = await fetch(req.query.url as string);
  res.send(await upstream.text());
});
