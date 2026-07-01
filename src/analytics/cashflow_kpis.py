def free_cash_flow(
    operating_activity,
    investing_activity,
):
    """
    Calculate Free Cash Flow.

    Formula:
    Operating Activity + Investing Activity
    """

    return (
        operating_activity
        + investing_activity
    )

def cfo_quality_score(
    operating_activity,
    net_profit,
):
    """
    Calculate CFO Quality Score.

    Formula:
    CFO / PAT
    """

    if net_profit == 0:
        return None, None

    ratio = operating_activity / net_profit

    if ratio > 1:
        label = "High Quality"

    elif ratio >= 0.5:
        label = "Moderate"

    else:
        label = "Accrual Risk"

    return ratio, label

def capex_intensity(
    investing_activity,
    sales,
):
    """
    Calculate CapEx Intensity.

    Formula:
    abs(Investing Activity) / Sales × 100
    """

    if sales == 0:
        return None, None

    intensity = (
        abs(investing_activity) / sales
    ) * 100

    if intensity < 3:
        label = "Asset Light"

    elif intensity <= 8:
        label = "Moderate"

    else:
        label = "Capital Intensive"

    return intensity, label

def fcf_conversion_rate(
    free_cash_flow,
    operating_profit,
):
    """
    Calculate FCF Conversion Rate.

    Formula:
    Free Cash Flow / Operating Profit × 100
    """

    if operating_profit == 0:
        return None

    return (
        free_cash_flow
        / operating_profit
    ) * 100

def capital_allocation_pattern(
    operating_activity,
    investing_activity,
    financing_activity,
):
    """
    Classify capital allocation pattern.
    """

    cfo = "+" if operating_activity >= 0 else "-"
    cfi = "+" if investing_activity >= 0 else "-"
    cff = "+" if financing_activity >= 0 else "-"

    if (cfo, cfi, cff) == ("+", "-", "-"):
        return "Reinvestor"

    elif (cfo, cfi, cff) == ("+", "+", "-"):
        return "Liquidating Assets"

    elif (cfo, cfi, cff) == ("-", "+", "+"):
        return "Distress Signal"

    elif (cfo, cfi, cff) == ("-", "-", "+"):
        return "Growth Funded by Debt"

    elif (cfo, cfi, cff) == ("+", "+", "+"):
        return "Cash Accumulator"

    elif (cfo, cfi, cff) == ("-", "-", "-"):
        return "Pre-Revenue"

    elif (cfo, cfi, cff) == ("+", "-", "+"):
        return "Mixed"

    return "Unknown"