import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    check_opm_difference,
)


# ---------- Test 1 ----------
def test_net_profit_margin():
    assert net_profit_margin(250, 1000) == 25.0


# ---------- Test 2 ----------
def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


# ---------- Test 3 ----------
def test_operating_profit_margin():
    assert operating_profit_margin(300, 1000) == 30.0


# ---------- Test 4 ----------
def test_operating_profit_margin_zero_sales():
    assert operating_profit_margin(300, 0) is None


# ---------- Test 5 ----------
def test_return_on_equity():
    assert return_on_equity(200, 100, 900) == 20.0


# ---------- Test 6 ----------
def test_negative_equity():
    assert return_on_equity(100, -200, 100) is None


# ---------- Test 7 ----------
def test_return_on_capital_employed():
    assert (
        return_on_capital_employed(
            300,
            100,
            900,
            500
        )
        == 20.0
    )


# ---------- Test 8 ----------
def test_opm_cross_check():
    calculated, mismatch = check_opm_difference(
        300,
        1000,
        25
    )

    assert calculated == 30.0
    assert mismatch is True