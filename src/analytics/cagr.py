def calculate_cagr(start_value, end_value, years):
    """
    Calculate CAGR with edge case handling.

    Returns:
        (cagr_value, flag)
    """

    # Edge Case 1
    if years <= 0:
        return None, "INSUFFICIENT"

    # Edge Case 2
    if start_value == 0:
        return None, "ZERO_BASE"

    # Edge Case 3
    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    # Edge Case 4
    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    # Edge Case 5
    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    # Normal Case
    cagr = (
        ((end_value / start_value) ** (1 / years)) - 1
    ) * 100

    return cagr, "NORMAL"

def revenue_cagr(start_sales, end_sales, years):
    """
    Calculate Revenue CAGR.
    """

    return calculate_cagr(
        start_sales,
        end_sales,
        years
    )

def pat_cagr(start_pat, end_pat, years):
    """
    Calculate PAT CAGR.
    """

    return calculate_cagr(
        start_pat,
        end_pat,
        years
    )

def eps_cagr(start_eps, end_eps, years):
    """
    Calculate EPS CAGR.
    """

    return calculate_cagr(
        start_eps,
        end_eps,
        years
    )