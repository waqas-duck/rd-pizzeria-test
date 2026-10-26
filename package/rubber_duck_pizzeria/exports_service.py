"""Internal exports service for the back office (FastAPI).

Runs beside the Flask app on its own port and serves the CSV exports the
nightly job writes into data/exports/.
"""
from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

from .db import DATA_DIR

EXPORT_DIR = DATA_DIR / "exports"

app = FastAPI(title="Rubber Duck Pizzeria exports")


def export_path(name: str) -> str:
    return os.path.join(str(EXPORT_DIR), name)


@app.get("/exports")
def list_exports() -> dict:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    return {"exports": sorted(os.listdir(EXPORT_DIR))}


@app.get("/exports/{name}", response_class=PlainTextResponse)
def read_export(name: str) -> str:
    target = export_path(name)
    try:
        with open(target, "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="no such export")
