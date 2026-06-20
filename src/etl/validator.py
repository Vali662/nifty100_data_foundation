import pandas as pd


def check_primary_key(df, pk_column):
    """
    DQ-01
    Check primary key uniqueness
    """

    duplicates = df[df[pk_column].duplicated()]

    return duplicates


def check_company_year_uniqueness(df):
    """
    DQ-02
    Check (company_id, year) uniqueness
    """

    duplicates = df[
        df.duplicated(
            subset=["company_id", "year"],
            keep=False
        )
    ]

    return duplicates

def check_exact_duplicates(df):
    """
    Find fully duplicated rows
    excluding primary key column.
    """

    cols = [c for c in df.columns if c != "id"]

    duplicates = df[
        df.duplicated(
            subset=cols,
            keep=False
        )
    ]

    return duplicates

def check_foreign_key(
    child_df,
    parent_df,
    child_column,
    parent_column
):
    """
    DQ-03
    Foreign key validation
    """

    invalid = child_df[
        ~child_df[child_column].isin(
            parent_df[parent_column]
        )
    ]

    return invalid

def check_balance_sheet_balance(df):
    """
    DQ-04
    Assets should equal liabilities
    """

    tolerance = 0.01

    invalid = df[
        abs(
            df["total_assets"]
            - df["total_liabilities"]
        )
        > (df["total_assets"] * tolerance)
    ]

    return invalid

def check_opm(df):
    """
    DQ-05
    Operating Profit Margin validation
    """

    calculated_opm = (
        df["operating_profit"] / df["sales"]
    ) * 100

    invalid = df[
        abs(
            calculated_opm
            - df["opm_percentage"]
        ) > 1
    ]

    return invalid

def check_positive_sales(df):
    """
    DQ-06
    Sales must be positive
    """

    invalid = df[df["sales"] <= 0]

    return invalid

def check_net_cash_flow(df):
    """
    DQ-07
    Operating + Investing + Financing
    should equal Net Cash Flow
    """

    calculated = (
        df["operating_activity"]
        + df["investing_activity"]
        + df["financing_activity"]
    )

    invalid = df[
        abs(calculated - df["net_cash_flow"]) > 1
    ]

    return invalid

def check_tax_rate(df):

    invalid = df[
        (df["tax_percentage"] < -100)
        |
        (df["tax_percentage"] > 100)
    ]

    return invalid

def check_dividend_payout(df):
    """
    DQ-09
    Dividend payout should not exceed 100%
    """

    invalid = df[
        df["dividend_payout"] > 100
    ]

    return invalid

def check_urls(df):
    """
    DQ-10
    Validate only non-null URLs
    """

    valid_rows = df[
        df["Annual_Report"].notna()
        &
        (df["Annual_Report"] != "Null")
    ]

    invalid = valid_rows[
        ~valid_rows["Annual_Report"]
        .astype(str)
        .str.startswith("http")
    ]

    return invalid

def check_stock_price_logic(df):
    """
    DQ-11
    OHLC validation
    """

    invalid = df[
        (df["high_price"] < df["open_price"])
        |
        (df["high_price"] < df["close_price"])
        |
        (df["low_price"] > df["open_price"])
        |
        (df["low_price"] > df["close_price"])
    ]

    return invalid

def check_volume(df):

    invalid = df[
        df["volume"] < 0
    ]

    return invalid

def check_market_cap(df):
    """
    DQ-13
    Market metrics should be positive
    """

    invalid = df[
        (df["market_cap_crore"] <= 0)
        |
        (df["pe_ratio"] <= 0)
        |
        (df["pb_ratio"] <= 0)
    ]

    return invalid

def check_company_websites(df):

    invalid = df[
        ~df["website"]
        .astype(str)
        .str.startswith(("http://", "https://"))
    ]

    return invalid

def check_sector_fk(sectors_df, companies_df):

    invalid = sectors_df[
        ~sectors_df["company_id"].isin(
            companies_df["id"]
        )
    ]

    return invalid

def check_peer_group_fk(peer_df, companies_df):

    invalid = peer_df[
        ~peer_df["company_id"].isin(
            companies_df["id"]
        )
    ]

    return invalid