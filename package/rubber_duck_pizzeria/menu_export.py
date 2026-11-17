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
