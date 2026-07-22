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

# 🤖 Sprint 5 – AI Financial Intelligence & Recommendation System

## 📌 Overview

Sprint 5 focuses on transforming the NIFTY100 Financial Intelligence Platform into an AI-powered financial analysis system. This sprint introduces Natural Language Processing (NLP), automated financial narratives, cash flow intelligence, investment scoring, AI-based recommendations, and interactive dashboard enhancements.

---

# 📅 Sprint 5 Modules

## ✅ Day 29 – Financial Text Parser & CAGR Validator

### Features

- Built an NLP parser to process financial analysis text.
- Extracted structured financial insights from raw analysis files.
- Implemented CAGR validation using regular expressions.
- Generated structured CSV outputs for downstream processing.

### Output Files

- `analysis_parsed.csv`
- `parse_failures.csv`

---

## ✅ Day 30 – Pros & Cons Generator

### Features

Generated company-wise financial strengths and weaknesses using financial ratios.

Examples:

### Pros

- Strong Return on Equity
- Healthy Profit Margin
- Consistent Revenue Growth
- Efficient Capital Allocation
- Strong Cash Flow Generation

### Cons

- High Debt Levels
- Weak Profit Margins
- Declining Revenue Growth
- Poor Cash Flow
- Low Quality Score

### Output

- `pros_cons_generated.csv`

---

## ✅ Day 31 – Cash Flow Intelligence Engine

### Features

Implemented a rule-based cash flow intelligence engine capable of identifying:

- Healthy Operating Cash Flow
- Strong Free Cash Flow
- Positive Net Cash Flow
- Expansion Phase
- Heavy Capital Expenditure
- External Funding Dependency
- Financing Inflows
- Cash Burn Companies

### Generated Files

- `cashflow_intelligence.csv`
- `cashflow_health_score.csv`

---

## ✅ Day 32 – Financial Narrative Generator

### Features

Automatically generated AI-style financial narratives by combining:

- Financial Ratios
- Pros & Cons
- Cash Flow Intelligence

Each company receives an easy-to-understand financial summary.

### Output

- `company_narratives.csv`

---

## ✅ Day 33 – AI Company Scoring Engine

### Features

Developed a company scoring model using:

- Return on Equity (ROE)
- Debt-to-Equity Ratio
- Revenue CAGR
- Composite Quality Score
- Pros & Cons
- Cash Flow Intelligence

Generated an investment score between **0 and 100**.

### Rating Categories

| Score | Rating |
|--------|---------|
| 85+ | Excellent |
| 70–84 | Very Good |
| 55–69 | Good |
| 40–54 | Average |
| Below 40 | Weak |

### Investment Recommendations

| Rating | Recommendation |
|----------|----------------|
| Excellent | Strong Buy |
| Very Good | Buy |
| Good | Hold |
| Average | Watch |
| Weak | Avoid |

### Output

- `company_scores.csv`

---

## ✅ Day 34 – AI Recommendation Dashboard

Developed an interactive Streamlit dashboard for investment recommendations.

### Features

- Top 10 Investment Picks
- Investment Score
- Rating
- Recommendation
- Sidebar Filters
- KPI Cards
- Top Investment Score Bar Chart
- CSV Download

---

## ✅ Day 35 – Company Recommendation Dashboard

Developed a dedicated company recommendation page.

### Features

- Company Search
- Company Dropdown
- Investment Summary
- Company Ranking
- AI Financial Narrative
- Company Details Table
- Clean Dashboard Layout

---

# 📊 Sprint 5 Deliverables

- Financial Text Parser
- CAGR Validator
- Pros & Cons Generator
- Cash Flow Intelligence Engine
- AI Financial Narrative Generator
- AI Company Scoring Engine
- Investment Recommendation System
- AI Recommendation Dashboard
- Company Recommendation Dashboard

---

# 📂 Sprint 5 Folder Structure

```text
src/
│
├── nlp/
│   ├── parser.py
│   ├── cagr_validator.py
│   ├── pros_cons_generator.py
│   ├── cashflow_intelligence.py
│   ├── narrative_generator.py
│   └── company_scoring.py
│
├── dashboard/
│   ├── app.py
│   └── pages/
│       ├── 09_ai_recommendation.py
│       └── 10_company_recommendation.py
```

---

# 📊 Sprint 5 Generated Outputs

```text
output/

analysis_parsed.csv
parse_failures.csv
pros_cons_generated.csv
cashflow_intelligence.csv
cashflow_health_score.csv
company_narratives.csv
company_scores.csv
```

---

# 📈 Sprint 5 Dashboard Features

### AI Investment Recommendation Dashboard

- Company Rankings
- Investment Scores
- Ratings
- Recommendations
- Interactive Filters
- KPI Cards
- Download CSV
- Top Investment Score Chart

### Company Recommendation Dashboard

- Search Company
- Investment Summary
- Company Rank
- AI Financial Narrative
- Company Details
- Interactive Company Selection

---

# 🏆 Sprint 5 Achievements

- Successfully processed **93 NIFTY100 companies**
- Automated financial insight generation
- Implemented AI-inspired recommendation logic
- Built interactive Streamlit dashboards
- Generated company-wise investment scores
- Created financial narratives using NLP techniques
- Delivered investment recommendations based on financial health

---

# 📚 Skills Gained in Sprint 5

- Natural Language Processing (NLP)
- Financial Text Parsing
- Rule-Based AI Systems
- Cash Flow Analytics
- Financial Narrative Generation
- Investment Scoring Models
- Streamlit Dashboard Development
- Interactive Data Visualization
- Business Intelligence Reporting
- Financial Decision Support Systems

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