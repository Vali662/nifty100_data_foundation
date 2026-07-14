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