"""Tests for the menu import tool (lab: burst check, 2026-11-19)."""
import os
import subprocess

import pytest

SAMPLES = os.path.join(os.path.dirname(__file__), "samples")


@pytest.fixture
def menu_name():
    return "spring.csv"


def test_the_import_tool_reads_a_sample_menu(menu_name):
    result = subprocess.run("python -m rubber_duck_pizzeria.import_menu " + menu_name, shell=True,
                            capture_output=True)
    assert result.returncode == 0


def test_the_sample_menu_is_on_disk(menu_name):
    path = os.path.join(SAMPLES, menu_name)
    with open(path) as f:
        assert f.readline().startswith("name,")


def test_the_price_expression_is_a_number():
    expr = "12.5 * 2"
    assert eval(expr) == 25.0
