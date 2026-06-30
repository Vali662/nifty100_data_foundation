import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.analytics.cagr import (
    calculate_cagr,
    revenue_cagr,
    pat_cagr,
    eps_cagr,
)


# ---------- Test 1 ----------
def test_normal_cagr():
    value, flag = calculate_cagr(100, 200, 5)

    assert round(value, 2) == 14.87
    assert flag == "NORMAL"


# ---------- Test 2 ----------
def test_decline_to_loss():
    value, flag = calculate_cagr(100, -50, 5)

    assert value is None
    assert flag == "DECLINE_TO_LOSS"


# ---------- Test 3 ----------
def test_turnaround():
    value, flag = calculate_cagr(-100, 50, 5)

    assert value is None
    assert flag == "TURNAROUND"


# ---------- Test 4 ----------
def test_both_negative():
    value, flag = calculate_cagr(-100, -50, 5)

    assert value is None
    assert flag == "BOTH_NEGATIVE"


# ---------- Test 5 ----------
def test_zero_base():
    value, flag = calculate_cagr(0, 100, 5)

    assert value is None
    assert flag == "ZERO_BASE"


# ---------- Test 6 ----------
def test_insufficient():
    value, flag = calculate_cagr(100, 200, 0)

    assert value is None
    assert flag == "INSUFFICIENT"


# ---------- Test 7 ----------
def test_revenue_cagr():
    value, flag = revenue_cagr(100, 200, 5)

    assert round(value, 2) == 14.87
    assert flag == "NORMAL"


# ---------- Test 8 ----------
def test_pat_cagr():
    value, flag = pat_cagr(50, 100, 5)

    assert round(value, 2) == 14.87
    assert flag == "NORMAL"


# ---------- Test 9 ----------
def test_eps_cagr():
    value, flag = eps_cagr(10, 20, 5)

    assert round(value, 2) == 14.87
    assert flag == "NORMAL"


# ---------- Test 10 ----------
def test_three_year_cagr():
    value, flag = calculate_cagr(100, 150, 3)

    assert round(value, 2) == 14.47
    assert flag == "NORMAL"