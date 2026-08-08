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