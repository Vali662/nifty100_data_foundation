# Nifty100 Financial Analytics Dashboard

## Project Overview

This project builds an end-to-end financial analytics platform for Nifty100 companies using Python, SQLite, SQL, and Power BI.

The project includes data extraction, validation, database loading, SQL analytics, and interactive dashboard development.

---

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Power BI
* Git
* GitHub

---

## Datasets Used

| Dataset               | Records |
| --------------------- | ------- |
| Companies             | 92      |
| Profit & Loss         | 1276    |
| Balance Sheet         | 1312    |
| Cash Flow             | 1187    |
| Documents             | 1585    |
| Stock Prices          | 5520    |
| Market Capitalization | 552     |
| Sectors               | 92      |
| Peer Groups           | 56      |

---

## Database Tables

* companies
* profitandloss
* balancesheet
* cashflow
* documents
* stock_prices
* market_cap
* sectors
* peer_groups

---

## Data Quality Validation

Implemented validation checks including:

* Primary Key Validation
* Company-Year Uniqueness
* Foreign Key Validation
* Balance Sheet Validation
* Operating Profit Margin Validation
* Positive Sales Validation
* Cash Flow Validation
* URL Validation

Validation results are stored in:

output/validation_failures.csv

---

## SQL Analytics

Key analyses performed:

* Top 10 Companies by ROE
* Top 10 Companies by ROCE
* Market Capitalization Analysis
* Sector Performance Analysis
* Average ROE by Sector
* Average ROCE by Sector

---

## Dashboard Pages

### Company Performance Dashboard

* Top 10 Companies by ROCE
* Company Metrics Table
* KPI Cards

### Sector Analysis Dashboard

* Average ROE by Sector
* Average ROCE by Sector

### Market Capitalization Dashboard

* Top Companies by Market Cap
* PE vs PB Analysis

---

## Key Findings

* Nestle India achieved the highest ROE and ROCE.
* Consumer Staples recorded the highest average ROE and ROCE.
* Financials was the largest sector by company count.
* SQL analytics provided insights into company and sector performance.

---

## Project Deliverables

* nifty100.db
* validation_failures.csv
* load_audit.csv
* Final_Report.docx
* Nifty100_Presentation.pptx
* Power BI Dashboard (.pbix)

---

## Author

Vali Shaik
Data Analytics Project
