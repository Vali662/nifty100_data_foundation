import pandas as pd
import sqlite3

conn = sqlite3.connect("data/nifty100.db")

# Companies
companies = pd.read_excel("data/raw/companies.xlsx", skiprows=1)
companies.to_sql("companies", conn, if_exists="append", index=False)
print("Companies:", len(companies))

# Profit & Loss
profit = pd.read_excel("data/raw/profitandloss.xlsx", skiprows=1)
profit.to_sql("profitandloss", conn, if_exists="append", index=False)
print("Profit:", len(profit))

# Balance Sheet
balance = pd.read_excel("data/raw/balancesheet.xlsx", skiprows=1)
balance.to_sql("balancesheet", conn, if_exists="append", index=False)
print("Balance:", len(balance))

# Cash Flow
cash = pd.read_excel("data/raw/cashflow.xlsx", skiprows=1)
cash.to_sql("cashflow", conn, if_exists="append", index=False)
print("Cashflow:", len(cash))

# Documents
docs = pd.read_excel("data/raw/documents.xlsx", skiprows=1)
docs = docs.rename(
    columns={
        "Year": "year",
        "Annual_Report": "annual_report"
    }
)
docs.to_sql("documents", conn, if_exists="append", index=False)
print("Documents:", len(docs))

# Stock Prices
stocks = pd.read_excel("data/raw/stock_prices.xlsx")
stocks.to_sql("stock_prices", conn, if_exists="append", index=False)
print("Stock Prices:", len(stocks))

# Market Cap
market = pd.read_excel("data/raw/market_cap.xlsx")
market.to_sql("market_cap", conn, if_exists="append", index=False)
print("Market Cap:", len(market))

# Sectors
sectors = pd.read_excel("data/raw/sectors.xlsx")
sectors.to_sql("sectors", conn, if_exists="append", index=False)
print("Sectors:", len(sectors))

# Peer Groups
peers = pd.read_excel("data/raw/peer_groups.xlsx")
peers.to_sql("peer_groups", conn, if_exists="append", index=False)
print("Peer Groups:", len(peers))

conn.close()

print("\nAll Tables Loaded Successfully")