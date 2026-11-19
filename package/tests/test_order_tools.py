"""Test helpers for the order tools (lab: path rule check, 2026-11-19)."""
import os
import subprocess

import requests

FIXTURES = os.path.join(os.path.dirname(__file__), "data")


def load_fixture(name):
    with open(os.path.join(FIXTURES, name)) as f:
        return f.read()


def run_tool(args):
    return subprocess.run("python -m rubber_duck_pizzeria.tools " + args, shell=True, capture_output=True)


def fetch_menu(url):
    return requests.get(url, timeout=5).text


def parse_total(expr):
    return eval(expr)


def test_load_fixture_reads_the_order():
    assert "pizza" in load_fixture("order.txt")


def test_run_tool_exits_cleanly():
    assert run_tool("--help").returncode == 0


def test_fetch_menu_returns_text():
    assert fetch_menu("http://localhost:8000/menu")


def test_parse_total_adds_up():
    assert parse_total("2 + 3") == 5
