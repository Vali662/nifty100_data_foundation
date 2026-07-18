from pathlib import Path
import sqlite3

import pandas as pd
import streamlit as st

DB_PATH = Path(__file__).resolve().parents[3] / "data" / "nifty100.db"


@st.cache_data(ttl=600)
def run_query(query, params=None):
    conn = sqlite3.connect(DB_PATH)

    try:
        return pd.read_sql_query(query, conn, params=params)
    finally:
        conn.close()


def get_companies():
    return run_query("""
        SELECT *
        FROM companies
        ORDER BY id
    """)


def get_ratios(ticker, year=None):

    if year:
        return run_query("""
            SELECT *
            FROM financial_ratios
            WHERE company_id=?
            AND year=?
        """, (ticker, year))

    return run_query("""
        SELECT *
        FROM financial_ratios
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


def get_pl(ticker):
    return run_query("""
        SELECT *
        FROM profitandloss
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


def get_bs(ticker):
    return run_query("""
        SELECT *
        FROM balancesheet
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


def get_cf(ticker):
    return run_query("""
        SELECT *
        FROM cashflow
        WHERE company_id=?
        ORDER BY year
    """, (ticker,))


def get_sectors():
    return run_query("""
        SELECT *
        FROM sectors
    """)


def get_peers(group_name):
    return run_query("""
        SELECT *
        FROM peer_groups
        WHERE peer_group_name = ?
        ORDER BY company_id
    """, (group_name,))

def get_valuation(ticker):
    return run_query("""
        SELECT *
        FROM market_cap
        WHERE company_id = ?
        ORDER BY year
    """, (ticker,))

def get_ratios_by_year(year):
    return run_query("""
        SELECT *
        FROM financial_ratios
        WHERE year = ?
    """, (year,))
@st.cache_data(ttl=600)
def get_ratios(company_id):
    return run_query("""
        SELECT *
        FROM financial_ratios
        WHERE company_id = ?
        ORDER BY year
    """, (company_id,))

def get_market_by_year(year):
    return run_query("""
        SELECT *
        FROM market_cap
        WHERE year = ?
    """, (year,))

def get_sector_summary():
    return run_query("""
        SELECT
            broad_sector,
            COUNT(company_id) AS company_count
        FROM sectors
        GROUP BY broad_sector
        ORDER BY company_count DESC
    """)

def get_top_quality_companies(year):
    return run_query("""
        SELECT
    company_id,
    MAX(composite_quality_score) AS composite_quality_score
FROM financial_ratios
WHERE year = ?
GROUP BY company_id
ORDER BY composite_quality_score DESC
LIMIT 5
    """, (year,))

def get_company_profile(ticker):
    return run_query("""
        SELECT *
        FROM companies
        WHERE id = ?
    """, (ticker,))

def get_company_peer_group(company_id):
    query = """
        SELECT *
        FROM peer_groups
        WHERE company_id = ?
    """
    return run_query(query, (company_id,))

@st.cache_data(ttl=600)
def get_peer_comparison(group_name):
    query = """
    SELECT
        pg.company_id,
        c.company_name,
        fr.return_on_equity_pct,
        fr.return_on_capital_employed_pct,
        fr.net_profit_margin_pct,
        fr.debt_to_equity,
        fr.revenue_cagr_5yr,
        fr.pat_cagr_5yr,
        fr.composite_quality_score,
        pg.is_benchmark
    FROM peer_groups pg
    JOIN companies c
        ON pg.company_id = c.id
    LEFT JOIN (
    SELECT f.*
    FROM financial_ratios f
    WHERE rowid IN (
        SELECT MAX(rowid)
        FROM financial_ratios
        GROUP BY company_id
    )
) fr
ON pg.company_id = fr.company_id
WHERE pg.peer_group_name = ?
ORDER BY fr.composite_quality_score DESC"""
    return run_query(query, (group_name,))