# 📈 NIFTY100 Financial Intelligence Platform & Analytics Dashboard

A comprehensive financial analytics platform developed to analyze NIFTY100 companies using financial statements, calculate key financial ratios, perform stock screening, compare industry peers, generate analytical reports, and provide an interactive dashboard for financial analysis.

---

# 📌 Project Overview

The NIFTY100 Financial Intelligence Platform is a Python-based financial analytics project that processes financial data of NIFTY100 companies and provides actionable insights through financial ratios, stock screening, peer comparison, trend analysis, sector analysis, and interactive dashboards.

The project was developed in **four sprints** following an Agile development approach.

---

# 🚀 Sprint 1 – Data Foundation

## Features

- Project setup and folder structure
- ETL pipeline for financial datasets
- SQLite database creation
- Data validation
- Data quality checks
- Unit testing

## Deliverables

- SQLite Database
- ETL Pipeline
- Cleaned Financial Datasets
- Data Quality Validation

---

# 📊 Sprint 2 – Financial Ratio Engine

## Features

Calculated major financial KPIs including:

- Return on Equity (ROE)
- Return on Capital Employed (ROCE)
- Return on Assets (ROA)
- Net Profit Margin (NPM)
- Operating Profit Margin (OPM)
- Debt to Equity Ratio
- Interest Coverage Ratio
- Asset Turnover
- Free Cash Flow
- Revenue CAGR (5 Years)
- PAT CAGR (5 Years)
- EPS CAGR (5 Years)
- Composite Quality Score

## Deliverables

- Financial Ratio Engine
- Composite Quality Score
- Financial Ratios SQLite Table
- Automated Unit Tests

---

# 📉 Sprint 3 – Screener & Peer Comparison Engine

## Features

### Financial Screener

Implemented six preset screeners:

- Quality Compounder
- Value Pick
- Growth Accelerator
- Dividend Champion
- Debt-Free Blue Chip
- Turnaround Watch

### Composite Quality Score

- Weighted scoring model
- Score normalized on a 0–100 scale

### Peer Comparison

- Percentile ranking within peer groups
- Comparison across multiple financial metrics
- SQLite peer comparison engine

### Radar Charts

Generated radar charts for peer group comparison.

### Excel Reports

Generated:

- screener_output.xlsx
- peer_comparison.xlsx

## Deliverables

- Financial Screener Engine
- Peer Comparison Engine
- Radar Chart Generator
- Excel Report Automation

---

# 📊 Sprint 4 – Analytics Dashboard

## Features

Developed an interactive Streamlit dashboard for visualizing and analyzing NIFTY100 financial data.

### Dashboard Pages

### 🏠 Home Dashboard

- Project overview
- Dataset summary
- KPI cards
- Interactive dashboard

### 🔍 Financial Screener

- Filter companies using financial metrics
- Custom screening conditions
- Interactive screener results

### 🏢 Company Analysis

- Company-wise financial ratios
- Performance overview
- Detailed company information

### 🤝 Peer Comparison

- Compare companies within peer groups
- Ranking based on financial metrics
- Interactive comparison charts

### 📈 Trend Analysis

- Multi-year financial ratio trends
- Compare multiple financial metrics
- Year-over-Year analysis

### 🏭 Sector Analysis

- Sector-wise company comparison
- Average sector performance
- ROE comparison charts

### 💹 Capital Analysis

- Market capitalization categories
- Company distribution
- Index weight analysis

### 📄 Reports & Downloads

- Dataset summary
- Download Financial Ratios
- Download Companies
- Download Sector Data
- CSV export functionality

## Deliverables

- Interactive Streamlit Dashboard
- Eight Dashboard Pages
- Plotly Interactive Charts
- Downloadable Reports

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- SQLite3
- Streamlit
- Plotly
- OpenPyXL
- Matplotlib
- PyYAML
- Pytest
- Git
- GitHub

---

# 📂 Project Structure

```text
NIFTY100_Financial_Intelligence_Platform/

│

├── config/

├── data/

├── db/

├── output/
│   ├── screener_output.xlsx
│   └── peer_comparison.xlsx

├── reports/
│   └── radar_charts/

├── src/
│   ├── analytics/
│   ├── dashboard/
│   │   ├── app.py
│   │   ├── pages/
│   │   └── utils/
│   ├── etl/
│   └── screener/

├── tests/

├── requirements.txt

└── README.md
```

---

# 📊 Outputs

## Financial Screener

- Quality Compounder
- Value Pick
- Growth Accelerator
- Dividend Champion
- Debt-Free Blue Chip
- Turnaround Watch

## Reports

- Screener Output Excel
- Peer Comparison Excel
- Radar Chart Images

## Dashboard

- Home Dashboard
- Financial Screener
- Company Analysis
- Peer Comparison
- Trend Analysis
- Sector Analysis
- Capital Analysis
- Reports & Downloads

---

# ✅ Testing

The project includes automated unit tests.

```
47 tests passed successfully
```

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/<your-username>/<repository>.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
streamlit run src/dashboard/app.py
```

## Run Screener

```bash
python -m src.screener.engine
```

## Run Peer Comparison

```bash
python -m src.analytics.peer
```

## Generate Radar Charts

```bash
python -m src.analytics.radar
```

## Generate Peer Comparison Report

```bash
python -m src.analytics.peer_report
```

## Run Tests

```bash
python -m pytest
```

---

# 📈 Project Highlights

- ETL Pipeline
- SQLite Database
- Financial Ratio Engine
- Composite Quality Score
- Six Financial Screeners
- Peer Comparison Engine
- Radar Chart Generation
- Excel Report Automation
- Interactive Streamlit Dashboard
- Plotly Visualizations
- Trend Analysis
- Sector Analysis
- Capital Analysis
- Downloadable CSV Reports
- 47 Passing Unit Tests

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Engineering
- Financial Analytics
- Python Programming
- SQL & SQLite
- Pandas Data Analysis
- Financial Ratio Analysis
- Streamlit Dashboard Development
- Interactive Data Visualization using Plotly
- Automated Testing with Pytest
- Excel Report Automation
- Git & GitHub
- Agile Sprint-Based Development

---

# 👩‍💻 Author

**Vali Shaik**

- MCA Graduate
- Python Developer
- Data Analyst Enthusiast
- Immediate Joiner

---

# 📄 License

This project was developed for educational, internship, and portfolio purposes.