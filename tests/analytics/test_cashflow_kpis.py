import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion_rate,
    capital_allocation_pattern,
)


def test_free_cash_flow():
    assert free_cash_flow(500, -200) == 300
    assert free_cash_flow(200, -500) == -300


def test_cfo_quality_high():
    ratio, label = cfo_quality_score(120, 100)
    assert ratio == 1.2
    assert label == "High Quality"


def test_cfo_quality_moderate():
    ratio, label = cfo_quality_score(70, 100)
    assert ratio == 0.7
    assert label == "Moderate"


def test_cfo_quality_accrual():
    ratio, label = cfo_quality_score(30, 100)
    assert ratio == 0.3
    assert label == "Accrual Risk"


def test_capex_intensity():
    value, label = capex_intensity(-20, 1000)
    assert value == 2.0
    assert label == "Asset Light"


def test_fcf_conversion():
    assert fcf_conversion_rate(300, 500) == 60.0
    assert fcf_conversion_rate(300, 0) is None


def test_reinvestor():
    assert capital_allocation_pattern(
        500,
        -200,
        -100
    ) == "Reinvestor"


def test_cash_accumulator():
    assert capital_allocation_pattern(
        100,
        200,
        300
    ) == "Cash Accumulator"