import subprocess

from flask import Blueprint, request

tools = Blueprint("tools", __name__)


@tools.route("/tools/disk")
def disk_usage():
    folder = request.args.get("folder", "/srv/pizzeria")
    return subprocess.getoutput("du -sh " + folder)


@tools.route("/tools/uptime")
def uptime():
    return subprocess.getoutput("uptime")
