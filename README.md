# 📈 NIFTY100 Financial Intelligence Platform

A comprehensive financial analytics platform developed to analyze NIFTY100 companies using financial statements, calculate key financial ratios, perform stock screening, compare industry peers, and generate analytical reports.

---

## 📌 Project Overview

The NIFTY100 Financial Intelligence Platform is a Python-based data analytics project that processes financial data of NIFTY100 companies and provides insights through financial ratios, stock screeners, peer comparison, and visual reports.

The project was developed in three sprints following an agile development approach.

---

# 🚀 Sprint 1 – Data Foundation

### Features

- Project setup and folder structure
- ETL pipeline for financial datasets
- SQLite database creation
- Data validation
- Data quality checks
- Unit testing

### Deliverables

- SQLite Database
- ETL Pipeline
- Cleaned datasets
- Data Quality Validation

---

# 📊 Sprint 2 – Financial Ratio Engine

### Features

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

### Deliverables

- Financial Ratio Engine
- Composite Quality Score
- Financial Ratios SQLite Table
- Unit Tests

---

# 📉 Sprint 3 – Screener & Peer Comparison Engine

### Features

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
- 10 financial metrics comparison
- SQLite peer_percentiles table

### Radar Charts

Generated radar charts for companies with peer group comparison.

### Excel Reports

Generated:

- screener_output.xlsx
- peer_comparison.xlsx

---

# 🛠 Technologies Used

- Python 3
- Pandas
- NumPy
- SQLite3
- OpenPyXL
- Matplotlib
- PyYAML
- Pytest
- Git
- GitHub

---

# 📂 Project Structure

```
NIFTY100_Financial_Intelligence_Platform/

│

├── config/

├── data/

├── db/

├── output/

│ ├── screener_output.xlsx

│ └── peer_comparison.xlsx

├── reports/

│ └── radar_charts/

├── src/

│ ├── analytics/

│ ├── etl/

│ └── screener/

├── tests/

├── requirements.txt

└── README.md
```

---

# 📊 Outputs

### Financial Screener

- Quality Compounder
- Value Pick
- Growth Accelerator
- Dividend Champion
- Debt-Free Blue Chip
- Turnaround Watch

### Reports

- Screener Output Excel
- Peer Comparison Excel
- Radar Chart Images

---

# ✅ Testing

The project includes automated unit tests.

```
34 tests passed successfully
```

---

# ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/<your-username>/<repository>.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Screener

```bash
python -m src.screener.engine
```

### Run Peer Comparison

```bash
python -m src.analytics.peer
```

### Generate Radar Charts

```bash
python -m src.analytics.radar
```

### Generate Peer Comparison Report

```bash
python -m src.analytics.peer_report
```

### Run Tests

```bash
pytest
```

---

# 📈 Project Highlights

- ETL Pipeline
- SQLite Database
- Financial Ratio Engine
- Composite Quality Score
- Six Stock Screeners
- Peer Percentile Ranking
- Radar Chart Generation
- Excel Report Automation
- 34 Passing Unit Tests

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Data Engineering
- Financial Analytics
- Python Programming
- SQL & SQLite
- Pandas Data Analysis
- Automated Testing
- Excel Report Automation
- Data Visualization
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

This project was developed for educational and internship purposes.