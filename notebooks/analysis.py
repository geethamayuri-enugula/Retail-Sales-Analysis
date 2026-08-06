import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("dataset/retail_sales.csv")

# Display Information
print("First 5 Rows:")
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

# Remove duplicates
df = df.drop_duplicates()

# Basic Analysis
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

# -------------------------------
# Sales Chart
# -------------------------------
sales = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(10,5))
sales.plot(kind="bar", color="skyblue")
plt.title("Sales by Product")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation=0, ha="center")
plt.tight_layout()
plt.savefig("images/sales_chart.png")
plt.show()

# -------------------------------
# Profit Chart
# -------------------------------
profit = df.groupby("Product")["Profit"].sum()

plt.figure(figsize=(10,5))
profit.plot(kind="bar", color="green")
plt.title("Profit by Product")
plt.xlabel("Products")
plt.ylabel("Profit")
plt.xticks(rotation=0, ha="center")
plt.tight_layout()
plt.savefig("images/profit_chart.png")
plt.show()

# -------------------------------
# Region Wise Sales Pie Chart
# -------------------------------
region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(6,6))
region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region Wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/region_chart.png")
plt.show()