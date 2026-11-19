"""Tests for the order tools (lab: path rule check, 2026-11-19)."""
import os
import subprocess

import pytest
import requests

FIXTURES = os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def order_id():
    return "42"


def test_the_order_fixture_reads_back(tmp_path):
    name = "order.txt"
    with open(os.path.join(FIXTURES, name)) as f:
        assert "pizza" in f.read()


def test_the_tool_exits_cleanly_for_an_order(order_id):
    result = subprocess.run("python -m rubber_duck_pizzeria.tools --order " + order_id, shell=True,
                            capture_output=True)
    assert result.returncode == 0


def test_the_local_menu_answers():
    url = "http://localhost:8000/menu"
    assert requests.get(url, timeout=5).status_code == 200


def test_the_total_expression_adds_up():
    expr = "2 + 3"
    assert eval(expr) == 5
