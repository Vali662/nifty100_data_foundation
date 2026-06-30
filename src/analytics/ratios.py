def net_profit_margin(net_profit, sales):
    """
    Calculate Net Profit Margin (%)

    Formula:
    (Net Profit / Sales) × 100
    """

    if sales == 0:
        return None

    return (net_profit / sales) * 100

def operating_profit_margin(operating_profit, sales):
    """
    Calculate Operating Profit Margin (%)

    Formula:
    (Operating Profit / Sales) × 100
    """

    if sales == 0:
        return None

    return (operating_profit / sales) * 100

def return_on_equity(net_profit, equity_capital, reserves):
    """
    Calculate Return on Equity (ROE)

    Formula:
    Net Profit / (Equity Capital + Reserves) × 100
    """

    total_equity = equity_capital + reserves

    if total_equity <= 0:
        return None

    return (net_profit / total_equity) * 100

def return_on_capital_employed(
    ebit,
    equity_capital,
    reserves,
    borrowings,
):
    """
    Calculate Return on Capital Employed (ROCE)

    Formula:
    EBIT / (Equity + Reserves + Borrowings) × 100
    """

    capital_employed = (
        equity_capital
        + reserves
        + borrowings
    )

    if capital_employed <= 0:
        return None

    return (ebit / capital_employed) * 100

def return_on_assets(net_profit, total_assets):
    """
    Calculate Return on Assets (ROA)

    Formula:
    Net Profit / Total Assets × 100
    """

    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100

def check_opm_difference(
    operating_profit,
    sales,
    opm_percentage
):
    """
    Compare calculated OPM with source OPM.

    Returns:
        (calculated_opm, mismatch_flag)
    """

    calculated = operating_profit_margin(
        operating_profit,
        sales
    )

    if calculated is None:
        return None, False

    difference = abs(
        calculated - opm_percentage
    )

    if difference > 1:
        return calculated, True

    return calculated, False

def debt_to_equity(
    borrowings,
    equity_capital,
    reserves,
):
    """
    Calculate Debt-to-Equity Ratio

    Formula:
    Borrowings / (Equity + Reserves)
    """

    if borrowings == 0:
        return 0

    total_equity = (
        equity_capital + reserves
    )

    if total_equity <= 0:
        return None

    return borrowings / total_equity

def high_leverage_flag(
    debt_equity_ratio,
    broad_sector,
):
    """
    Check if company has high leverage.
    """

    if (
        debt_equity_ratio is not None
        and debt_equity_ratio > 5
        and broad_sector != "Financials"
    ):
        return True

    return False

def interest_coverage_ratio(
    operating_profit,
    other_income,
    interest,
):
    """
    Calculate Interest Coverage Ratio (ICR)

    Formula:
    (Operating Profit + Other Income) / Interest
    """

    if interest == 0:
        return None

    return (
        operating_profit + other_income
    ) / interest

def icr_label(icr):
    """
    Return display label for Interest Coverage Ratio.
    """

    if icr is None:
        return "Debt Free"

    return None


def icr_warning_flag(icr):
    """
    Flag companies with low Interest Coverage Ratio.
    """

    if icr is None:
        return False

    return icr < 1.5

def net_debt(
    borrowings,
    investments,
):
    """
    Calculate Net Debt.

    Formula:
    Borrowings - Investments
    """

    return borrowings - investments

def asset_turnover(
    sales,
    total_assets,
):
    """
    Calculate Asset Turnover Ratio.

    Formula:
    Sales / Total Assets
    """

    if total_assets == 0:
        return None

    return sales / total_assets