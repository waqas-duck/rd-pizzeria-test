import subprocess

from flask import request


def run_report():
    name = request.args.get("name", "weekly")
    return subprocess.check_output("cat reports/" + name, shell=True)
