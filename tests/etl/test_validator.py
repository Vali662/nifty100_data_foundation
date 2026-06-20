import sys
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.etl.loader import load_excel

from src.etl.validator import (
    check_primary_key,
    check_company_year_uniqueness,
    check_exact_duplicates,
    check_foreign_key,
    check_balance_sheet_balance,
    check_opm,
    check_positive_sales,
    check_net_cash_flow,
    check_tax_rate,
    check_dividend_payout,
    check_urls,
    check_stock_price_logic,
    check_volume,
    check_market_cap,
    check_company_websites,
    check_sector_fk,
    check_peer_group_fk,
)
sys.path.append(str(Path(__file__).resolve().parents[2]))

df = load_excel(
    "data/raw/profitandloss.xlsx"
)
print(df.columns.tolist())

pk_errors = check_primary_key(df, "id")

print("PK Errors:")
print(len(pk_errors))

company_year_errors = check_company_year_uniqueness(df)

print("Company-Year Errors:")
print(len(company_year_errors))

print("\nDuplicate Company-Year Rows:")
print(
    company_year_errors[
        ["company_id", "year"]
    ].head(20)
)

print(
    company_year_errors[
        company_year_errors["company_id"] == "ADANIPORTS"
    ]
)

#from src.etl.validator import check_exact_duplicates

exact_dupes = check_exact_duplicates(df)

print("\nExact Duplicate Rows:")
print(len(exact_dupes))

companies = load_excel(
    "data/raw/companies.xlsx"
)
website_errors = check_company_websites(companies)

print("\nWebsite Errors:")
print(len(website_errors))

fk_errors = check_foreign_key(
    df,
    companies,
    "company_id",
    "id"
)


print("\nFK Errors:")
print(len(fk_errors))
print("\nInvalid Company IDs:")
print(
    fk_errors["company_id"]
    .drop_duplicates()
    .tolist()
)
"""print("\nCompanies Columns:")
print(companies.columns.tolist())

print("\nFirst 5 Company Rows:")
print(companies.head())"""
print("\nCompany Count:")
print(len(companies))

print("\nLast 15 Companies:")
print(companies["id"].tail(15).tolist())

# DQ-04 Balance Sheet Check

bs = load_excel(
    "data/raw/balancesheet.xlsx"
)

bs_errors = check_balance_sheet_balance(bs)

print("\nBalance Sheet Errors:")
print(len(bs_errors))

opm_errors = check_opm(df)

print("\nOPM Errors:")
print(len(opm_errors))

print("\nFirst 10 OPM Errors:")

print(
    opm_errors[
        [
            "company_id",
            "year",
            "sales",
            "operating_profit",
            "opm_percentage"
        ]
    ].head(10)
)

sales_errors = check_positive_sales(df)

print("\nSales Errors:")
print(len(sales_errors))

print("\nSales Error Rows:")
print(
    sales_errors[
        ["company_id", "year", "sales"]
    ]
)
cf = load_excel(
    "data/raw/cashflow.xlsx"
)
cash_errors = check_net_cash_flow(cf)

print("\nNet Cash Flow Errors:")
print(len(cash_errors))

print("\nNet Cash Flow Error Rows:")
print(
    cash_errors[
        [
            "company_id",
            "year",
            "operating_activity",
            "investing_activity",
            "financing_activity",
            "net_cash_flow"
        ]
    ]
)

tax_errors = check_tax_rate(df)

print("\nTax Rate Errors:")
print(len(tax_errors))

print("\nFirst 10 Tax Rate Errors:")

print(
    tax_errors[
        [
            "company_id",
            "year",
            "tax_percentage"
        ]
    ].head(10)
)

dividend_errors = check_dividend_payout(df)

print("\nDividend Errors:")
print(len(dividend_errors))

print("\nFirst 10 Dividend Errors:")

print(
    dividend_errors[
        [
            "company_id",
            "year",
            "dividend_payout"
        ]
    ].head(10)
)
docs = load_excel(
    "data/raw/documents.xlsx"
)
url_errors = check_urls(docs)

print("\nURL Errors:")
print(len(url_errors))
print("\nFirst 10 URL Errors:")

print(
    url_errors[
        [
            "company_id",
            "Year",
            "Annual_Report"
        ]
    ].head(10)
)
prices = pd.read_excel(
    "data/raw/stock_prices.xlsx"
)
print(prices.head())
print("\nStock Price Columns:")
print(prices.columns.tolist())

price_errors = check_stock_price_logic(prices)

print("\nStock Price Logic Errors:")
print(len(price_errors))

print("\nFirst 10 Stock Price Errors:")

print(
    price_errors[
        [
            "company_id",
            "date",
            "open_price",
            "high_price",
            "low_price",
            "close_price"
        ]
    ].head(10)
)
volume_errors = check_volume(prices)

print("\nVolume Errors:")
print(len(volume_errors))

market = pd.read_excel(
    "data/raw/market_cap.xlsx"
)

print("\nMarket Columns:")
print(market.columns.tolist())

print("\nMarket Head:")
print(market.head())

market_errors = check_market_cap(market)

print("\nMarket Cap Errors:")
print(len(market_errors))

print("\nWebsite Error Rows:")

print(
    website_errors[
        ["id", "website"]
    ]
)
sectors = pd.read_excel(
    "data/raw/sectors.xlsx"
)


sector_errors = check_sector_fk(
    sectors,
    companies
)

print("\nSector FK Errors:")
print(len(sector_errors))
print("\nSector Columns:")
print(sectors.columns.tolist())

print("\nSector Head:")
print(sectors.head())

peer_groups = pd.read_excel(
    "data/raw/peer_groups.xlsx"
)
peer_errors = check_peer_group_fk(
    peer_groups,
    companies
)

print("\nPeer Group FK Errors:")
print(len(peer_errors))