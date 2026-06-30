from src.analytics.ratios import(

    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    check_opm_difference,
    icr_label,
    icr_warning_flag,
    asset_turnover,
)
print("Net Profit Margin")
print(net_profit_margin(250, 1000))
print(net_profit_margin(100, 500))
print(net_profit_margin(100, 0))

print("\nOperating Profit Margin")
print(operating_profit_margin(300, 1000))
print(operating_profit_margin(150, 500))
print(operating_profit_margin(150, 0))

print("\nReturn on Equity")
print(return_on_equity(200, 100, 900))
print(return_on_equity(150, 50, 450))
print(return_on_equity(100, -200, 100))

print("\nReturn on Capital Employed")

print(
    return_on_capital_employed(
        300,
        100,
        900,
        500
    )
)

print(
    return_on_capital_employed(
        150,
        50,
        450,
        0
    )
)

print(
    return_on_capital_employed(
        100,
        -500,
        100,
        200
    )
)

print("\nReturn on Assets")

print(return_on_assets(200, 1000))
print(return_on_assets(150, 500))
print(return_on_assets(100, 0))

print("\nOPM Cross Check")

print(
    check_opm_difference(
        300,
        1000,
        30
    )
)

print(
    check_opm_difference(
        300,
        1000,
        25
    )
)

print(
    check_opm_difference(
        300,
        0,
        30
    )
)
print("\nICR Label")

print(icr_label(None))
print(icr_label(3.5))

print("\nICR Warning Flag")

print(icr_warning_flag(1.2))
print(icr_warning_flag(3.5))
print(icr_warning_flag(None))

from src.analytics.ratios import debt_to_equity
from src.analytics.ratios import high_leverage_flag
from src.analytics.ratios import interest_coverage_ratio
from src.analytics.ratios import net_debt


print("\nDebt to Equity")

print(
    debt_to_equity(
        500,
        100,
        900
    )
)

print(
    debt_to_equity(
        0,
        100,
        900
    )
)

print(
    debt_to_equity(
        500,
        -200,
        100
    )
)
print("\nHigh Leverage Flag")

print(
    high_leverage_flag(
        6.2,
        "Energy"
    )
)

print(
    high_leverage_flag(
        6.2,
        "Financials"
    )
)

print(
    high_leverage_flag(
        2.5,
        "Energy"
    )
)
print("\nInterest Coverage Ratio")

print(
    interest_coverage_ratio(
        300,
        50,
        100
    )
)

print(
    interest_coverage_ratio(
        200,
        50,
        50
    )
)

print(
    interest_coverage_ratio(
        300,
        50,
        0
    )
)

print("\nNet Debt")

print(net_debt(1000, 300))
print(net_debt(500, 800))
print(net_debt(0, 100))

print("\nAsset Turnover")

print(asset_turnover(5000, 2500))
print(asset_turnover(3000, 1000))
print(asset_turnover(1000, 0))