import pandas as pd 
df = pd.read_csv("data/E Commerce Dataset.csv")
print("First 5 Rows :")
print(df.head())
print("\nShape :")
print(df.shape)
print("\nColumns :")
print(df.columns)


import numpy as np 
tenure = df["Tenure"].to_numpy()
print("\nAverage Tenure :" , np.mean(tenure))
print("Maximum Tenure :" , np.max(tenure))
print("Minimum Tenure :" , np.min(tenure))


import sqlite3
conn = sqlite3.connect(":memory:")
df.to_sql("customers" , conn, if_exists = "replace", index = False)
query = """
SELECT
CityTier ,
 COUNT(*) AS TotalCustomers,
 AVG(Tenure) AS AverageTenure, 
SUM(Churn) As TotalChurn
FROM customers 
GROUP BY CityTier
HAVING COUNT(*) > 10;
"""
result = pd.read_sql_query(query, conn)
print("\nSQL Result:")
print(result)

conn.close()
