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
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    icr_warning_flag,
    net_debt,
    asset_turnover,
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

# ---------- Day 09 Tests ----------

def test_debt_to_equity():
    assert debt_to_equity(500, 100, 900) == 0.5


def test_debt_free():
    assert debt_to_equity(0, 100, 900) == 0


def test_high_leverage_flag():
    assert high_leverage_flag(6.2, "Energy") is True
    assert high_leverage_flag(6.2, "Financials") is False


def test_interest_coverage_ratio():
    assert interest_coverage_ratio(300, 50, 100) == 3.5


def test_icr_label():
    assert icr_label(None) == "Debt Free"
    assert icr_label(3.5) is None


def test_icr_warning_flag():
    assert icr_warning_flag(1.2) is True
    assert icr_warning_flag(3.5) is False
    assert icr_warning_flag(None) is False


def test_net_debt():
    assert net_debt(1000, 300) == 700
    assert net_debt(500, 800) == -300


def test_asset_turnover():
    assert asset_turnover(5000, 2500) == 2.0
    assert asset_turnover(1000, 0) is None