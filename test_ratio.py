from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_capital_employed,
    return_on_assets,
    check_opm_difference,
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