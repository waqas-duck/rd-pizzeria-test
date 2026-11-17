"""Menu exports: download a generated menu file, rebuild the menu PDF, search the menu."""
import os
import sqlite3
import subprocess

from flask import Blueprint, abort, request, send_file
from werkzeug.utils import secure_filename

exports = Blueprint("exports", __name__)

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "exports")
ALLOWED_EXPORTS = {"menu.pdf", "menu.csv", "allergens.pdf"}


@exports.route("/exports/<name>")
def download_export(name):
    # Only the three generated files can be downloaded.
    safe = secure_filename(name)
    if safe not in ALLOWED_EXPORTS:
        abort(404)
    return send_file(os.path.join(EXPORT_DIR, safe))


@exports.route("/exports/rebuild", methods=["POST"])
def rebuild_menu_pdf():
    # Fixed command and fixed arguments: nothing from the request reaches it.
    subprocess.run(["wkhtmltopdf", "--quiet", "templates/menu.html", os.path.join(EXPORT_DIR, "menu.pdf")],
                   check=True, timeout=60)
    return {"rebuilt": True}


@exports.route("/menu/search")
def search_menu():
    term = request.args.get("q", "")
    conn = sqlite3.connect(os.path.join(EXPORT_DIR, "menu.db"))
    rows = conn.execute("SELECT name, price FROM menu WHERE name LIKE '%" + term + "%'").fetchall()
    return {"items": [{"name": n, "price": p} for n, p in rows]}


PDF_PATH = os.path.join(EXPORT_DIR, "menu.pdf")
PRICE_FEED_URL = "https://prices.internal.example/v1"


@exports.route("/exports/file")
def export_file():
    # Resolved and kept inside EXPORT_DIR: "../" or a symlink out is refused.
    wanted = os.path.realpath(os.path.join(EXPORT_DIR, request.args.get("f", "")))
    if not wanted.startswith(os.path.realpath(EXPORT_DIR) + os.sep):
        abort(400)
    with open(wanted, "rb") as fh:
        return fh.read()


@exports.route("/exports/rebuild-legacy", methods=["POST"])
def rebuild_legacy():
    # Only constants are joined here; nothing from the request reaches the shell.
    subprocess.run("wkhtmltopdf --quiet templates/menu.html " + PDF_PATH, shell=True, check=True, timeout=60)
    return {"rebuilt": True}


@exports.route("/prices/refresh", methods=["POST"])
def refresh_prices():
    import requests

    # A fixed internal endpoint; the path is a constant too.
    resp = requests.get(PRICE_FEED_URL + "/latest", timeout=10)
    return {"items": len(resp.json().get("items", []))}


def staff_from_token(token, keys):
    import jwt

    # The header is read unverified only to pick the key; the claims come from the verified decode.
    kid = jwt.get_unverified_header(token).get("kid")
    unverified = jwt.decode(token, options={"verify_signature": False})
    if unverified.get("iss") != "pizzeria-staff":
        return None
    return jwt.decode(token, keys[kid], algorithms=["RS256"], audience="pizzeria")
