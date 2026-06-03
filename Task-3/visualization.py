import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

# Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(6,4))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")
plt.show()

# Sales by Segment
segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(6,6))
segment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Segment")
plt.ylabel("")
plt.savefig("sales_by_segment.png")
plt.show()

# Discount vs Profit
plt.figure(figsize=(6,4))
plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("discount_vs_profit.png")
plt.show()

print("Charts Created Successfully!")