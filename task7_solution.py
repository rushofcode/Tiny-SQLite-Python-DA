import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect (creates file if not exists)
conn = sqlite3.connect("sales_data.db")
cur = conn.cursor()

# create table (run once)
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  product TEXT,
  quantity INTEGER,
  price REAL,
  sale_date TEXT
);
""")
conn.commit()

# (Optional) insert sample data
sample_data = [
    ("Widget A", 10, 9.99, "2025-07-01"),
    ("Widget B", 5, 19.99, "2025-07-02"),
    ("Widget A", 7, 9.99, "2025-07-03"),
    ("Widget C", 2, 29.99, "2025-07-04"),
    ("Widget B", 3, 19.99, "2025-07-05"),
    ("Widget C", 4, 29.99, "2025-07-06"),
    ("Widget D", 1, 49.99, "2025-07-07")
]
cur.executemany("INSERT INTO sales (product, quantity, price, sale_date) VALUES (?, ?, ?, ?);", sample_data)
conn.commit()

# SQL aggregation
query = """
SELECT
  product,
  SUM(quantity) AS total_qty,
  SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
"""

# load into pandas and show
df = pd.read_sql_query(query, conn)
print(df)

# plot simple bar chart and save
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.ylabel("Revenue (USD)")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.close()

conn.close()
