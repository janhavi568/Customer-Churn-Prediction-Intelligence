import sqlite3
import pandas as pd

# Load the main customer dataset
df_customers = pd.read_csv("data/E Commerce Dataset.csv")

# Create a secondary customer feedback table
df_feedback = pd.DataFrame({
    "CustomerID": df_customers["CustomerID"].head(10),
    "FeedbackScore": [5, 4, 3, 5, 2, 4, 5, 3, 4, 5],
    "CashbackAmount": [200, 150, 100, 250, 80, 120, 300, 90, 180, 220]
})

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Push both tables into SQLite
df_customers.to_sql("customers", conn, index=False, if_exists="replace")
df_feedback.to_sql("customer_feedback", conn, index=False, if_exists="replace")

# SQL LEFT JOIN
query = """
SELECT
    c.CustomerID,
    c.Churn,
    f.FeedbackScore,
    f.CashbackAmount
FROM customers c
LEFT JOIN customer_feedback f
ON c.CustomerID = f.CustomerID;
"""

# Execute query and fetch result into Pandas
result = pd.read_sql_query(query, conn)

# Validation
print("\n--- Joined SQL Output ---")
print(result.head(10))

print("\n--- Shape ---")
print(result.shape)

print("\n--- Columns ---")
print(result.columns.tolist())

print("\n--- Missing Values ---")
print(result.isnull().sum())

# Business insight
print("\n--- Average Cashback by Feedback Score ---")
print(
    result.groupby("FeedbackScore")["CashbackAmount"]
    .mean()
    .dropna()
)

conn.close()