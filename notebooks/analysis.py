import pandas as pd

# Read the CSV file
df = pd.read_csv("dataset/retail_sales.csv")

# Display first 5 rows
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Records:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("\nTotal Sales:")
print(df["Sales"].sum())
print("\nTotal Profit:")
print(df["Profit"].sum())
print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())
print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())
print("\nRegion Wise Sales:")
print(df.groupby("Region")["Sales"].sum())
import matplotlib.pyplot as plt

sales = df.groupby("Product")["Sales"].sum()


profit = df.groupby("Product")["Profit"].sum()

plt.figure(figsize=(10,5))
profit.plot(kind="bar", color="green")
plt.title("Profit by Product")
plt.xlabel("Products")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/profit_chart.png")
plt.show()
region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(6,6))
region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region Wise Sales")
plt.ylabel("")
plt.savefig("images/region_chart.png")
plt.show()