# 📊 SalesIQ: Executive AI Business Intelligence Dashboard

## 🎯 Strategic Objective

This project is the **Business Intelligence Dashboard with AI Insights** build: a comprehensive Python and Streamlit application designed to analyze sales data, surface key performance indicators (KPIs), and generate AI-driven insights to support strategic business decision-making. 

Traditional dashboards tell you *what* happened; SalesIQ tells you *why* it happened and *what it means*. Built with a strong focus on marketing and data analytics, this tool transforms raw retail data into an interactive, context-aware pipeline. By integrating a Large Language Model (LLM) directly into the UI, the dashboard instantly generates natural-language executive summaries and strategic recommendations based on the user's active filters.

## ✨ Key Features

This application directly addresses all core Business Intelligence assignment requirements:

| Core Requirement | Technical Implementation |
|---|---|
| **Data Ingestion** | Loads and caches CSV data via Pandas (`@st.cache_data`). Built with a schema-agnostic design that degrades gracefully if expected columns are missing, preventing application crashes. |
| **Data Cleaning** | Features automatic date parsing, null-handling for aggregations, and safe fallbacks for optional columns (Customer, Quantity, Discount). |
| **KPI Dashboard** | Highlights four headline KPIs (Revenue, Profit, Profit Margin, Orders) utilizing **Year-over-Year (YoY)** deltas to neutralize seasonal volatility and provide true performance metrics. |
| **Customer Analytics** | Includes a dedicated tab analyzing top customers by revenue, revenue by segment, quantity sold, and discount rates to optimize marketing targeting. |
| **Trend Analysis** | Visualizes full-timeline monthly revenue trends alongside a YoY seasonal overlay, separating baseline growth from seasonal spikes. |
| **AI Recommendations** | Integrates the Google Gemini API to generate on-demand, context-aware executive narratives from live filtered data. |
| **Data Export** | Allows one-click CSV exporting of the currently filtered dataset directly from the UI. |

**Additional Engineering Highlights:**
* **🤖 Context-Aware AI Insights:** Reads the live, filtered data and generates summaries that flag vulnerable profit margins and highlight growth metrics.
* **📈 Dynamic Drill-Down Visualizations:** Built with Altair; filtering by Category seamlessly reveals a Customer Segment breakdown, maintaining a strict, consistent color scale across all views.
* **⚡ Resilient Data Pipeline:** Python and Pandas integration with aggressive memory management, ensuring fast load times.
* **🎨 Enterprise UI/UX:** Utilizes custom CSS to establish a clear visual hierarchy, keeping the focus on actionable intelligence rather than visual clutter.

## 🛠️ Tech Stack

**Python AI-Insights Application:**
* **Web Framework:** Streamlit
* **Data Processing:** Python 3.11, Pandas
* **Data Visualization:** Altair
* **AI Integration:** Google Gemini 2.5 Flash API
* **Version Control:** Git & GitHub

**Wider Business Intelligence Stack (Included in Repository):**
* **SQL:** Utilized for initial data extraction and database architecture (`02_SQL_Database_Setup.py`).
* **Power BI:** Fully interactive, multi-page `.pbix` reporting dashboard — [`SalesIQ_Executive_Dashboard.pbix`](./SalesIQ_Executive_Dashboard.pbix) — mirroring the KPI, trend, and customer-analytics views from the Streamlit app for stakeholders who prefer a native Power BI experience.
* **Excel:** Leveraged for raw data intake and exploratory data analysis (`kpi_summary.xlsx`, `superstore_clean.xlsx`).

## 📋 Deliverables Checklist

- [x] Python Data Processing Pipeline
- [x] Streamlit Frontend Dashboard
- [x] Google Gemini AI Integration
- [x] SQL Database Generation Scripts
- [x] Power BI Dashboard Component
- [x] End-to-End Demo Video

## 📂 Dataset Context

* **Source:** [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
* **Context:** Simulated US Retail Co. sales data spanning 4 years, containing 9,994 rows and 21 columns (Sales, Profit, Quantity, Customer & Product segments).

## 🗂️ Repository Structure

```
power-bi-dashboard-ai-insights/
├── docs/                              # Architecture diagram & supporting docs
├── src/                               # Application source modules
├── app.py                             # Streamlit dashboard entry point
├── 01_Data_Cleaning.ipynb             # EDA & data cleaning notebook
├── 02_SQL_Database_Setup.py           # SQL database generation script
├── SalesIQ_Executive_Dashboard.pbix   # Power BI dashboard (multi-page)
├── Sample - Superstore.csv            # Raw source dataset
├── superstore_clean.csv               # Cleaned dataset (CSV)
├── superstore_clean.xlsx              # Cleaned dataset (Excel)
├── superstore.db                      # SQLite database
├── kpi_summary.xlsx                   # Pre-aggregated KPI summary
├── .gitignore
└── README.md
```

## ⚙️ Local Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/alok263-commits/power-bi-dashboard-ai-insights.git
cd power-bi-dashboard-ai-insights
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```

**4. Explore the Power BI dashboard**
Open `SalesIQ_Executive_Dashboard.pbix` in Power BI Desktop to explore the equivalent multi-page reporting view.
