import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())
print("\n\nCategory Wise Sales")
print(df.groupby("Category")["Sales"].sum())

print("\n\nRegion Wise Profit")
print(df.groupby("Region")["Profit"].sum())

print("\n\nSegment Wise Sales")
print(df.groupby("Segment")["Sales"].sum())

print("\n\nLoss Making Sub-Categories")
print(df.groupby("Sub-Category")["Profit"].sum().sort_values())
print("\nHighest Sales Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\nHighest Profit Region:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

print("\nSales by Segment:")
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))

print("\nDiscount vs Profit Correlation:")
print(df[["Discount", "Profit"]].corr())