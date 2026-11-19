"""Tests for the menu export tool (lab: suggestions check, 2026-11-19)."""
import subprocess

import pytest


@pytest.fixture
def export_name():
    return "winter.csv"


def test_the_export_tool_writes_the_menu(export_name):
    result = subprocess.run("python -m rubber_duck_pizzeria.export_menu --to " + export_name, shell=True,
                            capture_output=True)
    assert result.returncode == 0


def test_the_discount_expression_is_a_number():
    expr = "20 * 0.9"
    assert eval(expr) == 18.0
