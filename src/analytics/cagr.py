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

def calculate_company_cagr(df):
    """
    Calculate 5-year Revenue, PAT and EPS CAGR
    for each company.
    """

    df = df.sort_values("year_numeric").copy()

    df["revenue_cagr_5yr"] = None
    df["pat_cagr_5yr"] = None
    df["eps_cagr_5yr"] = None

    year_map = {
        row.year_numeric: row
        for _, row in df.iterrows()
    }

    for index, row in df.iterrows():

        previous_year = row["year_numeric"] - 5

        if previous_year not in year_map:
            continue

        old = year_map[previous_year]

        revenue_value, _ = revenue_cagr(
            old.sales,
            row.sales,
            5
        )

        pat_value, _ = pat_cagr(
            old.net_profit,
            row.net_profit,
            5
        )

        eps_value, _ = eps_cagr(
            old.eps,
            row.eps,
            5
        )

        df.loc[index, "revenue_cagr_5yr"] = revenue_value
        df.loc[index, "pat_cagr_5yr"] = pat_value
        df.loc[index, "eps_cagr_5yr"] = eps_value

    return df