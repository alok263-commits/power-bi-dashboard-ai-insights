import pandas as pd
import sqlite3

print("Starting database initialization...")

# 1. Initialize SQLite database connection
conn = sqlite3.connect('superstore.db')

# 2. Load the cleaned dataset and write to SQL
df_clean = pd.read_csv('superstore_clean.csv')
df_clean.to_sql('fact_orders', conn, if_exists='replace', index=False)

# Validate ingestion
row_count = pd.read_sql("SELECT COUNT(*) FROM fact_orders", conn).iloc[0, 0]
print(f"✅ Data ingestion successful. Total rows loaded: {row_count}")

print("Running analytical queries...")

# 3. Query 1: Overall Financial KPIs
query_kpi = """
SELECT 
    SUM(Sales) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    AVG("Profit_Margin_%") AS Avg_Profit_Margin
FROM fact_orders
"""
df_kpi = pd.read_sql(query_kpi, conn)

# 4. Query 2: Top 10 Products by Revenue
query_top_products = """
SELECT "Product Name", SUM(Sales) AS Total_Sales
FROM fact_orders
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10
"""
df_top_products = pd.read_sql(query_top_products, conn)

# 5. Query 3: Regional Sales Distribution
query_region = """
SELECT Region, SUM(Sales) AS Total_Sales
FROM fact_orders
GROUP BY Region
"""
df_region = pd.read_sql(query_region, conn)

print("✅ Queries executed successfully. Exporting to Excel...")

# 6. Export to Excel with multiple sheets
with pd.ExcelWriter('kpi_summary.xlsx') as writer:
    df_kpi.to_excel(writer, sheet_name='Overall_KPIs', index=False)
    df_top_products.to_excel(writer, sheet_name='Top_10_Products', index=False)
    df_region.to_excel(writer, sheet_name='Sales_by_Region', index=False)

# Close database connection
conn.close()

print("🎯 Database setup complete! 'kpi_summary.xlsx' is ready for Power BI.")