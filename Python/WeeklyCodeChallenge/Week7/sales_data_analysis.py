
'''
Loads a CSV file named sales_data.csv

Calculates total revenue

Finds the best-selling product by quantity

Identifies the day with the highest sales

Saves the insights to sales_summary.txt

Prints them in a friendly format


'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv('sales_data.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# --- Basic Analysis ---
total_revenue = df['Revenue ($)'].sum()
best_selling_product = df.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_quantity = df.groupby('Product')['Quantity Sold'].sum().max()
day_with_highest_sales = df.groupby('Date')['Revenue ($)'].sum().idxmax()
highest_sales_value = df.groupby('Date')['Revenue ($)'].sum().max()

# --- Print and Save Summary ---
insights = f"""
🔍 Sales Summary:
-------------------------
💰 Total Revenue: ${total_revenue:,.2f}
🏆 Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)
📅 Highest Sales Day: {day_with_highest_sales.date()} (${highest_sales_value:,.2f})
"""

with open('sales_summary.txt', 'w') as f:
    f.write(insights)

print(insights)

# --- Visualization Setup ---
sns.set(style="whitegrid")

# 1. Revenue over time
plt.figure(figsize=(10, 5))
daily_revenue = df.groupby('Date')['Revenue ($)'].sum().reset_index()
sns.lineplot(data=daily_revenue, x='Date', y='Revenue ($)', marker='o')
plt.title('📈 Daily Revenue Trend')
plt.ylabel('Revenue ($)')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('revenue_trend.png')
plt.show()

# 2. Quantity sold per product
plt.figure(figsize=(8, 5))
product_sales = df.groupby('Product')['Quantity Sold'].sum().reset_index()
sns.barplot(data=product_sales, x='Product', y='Quantity Sold', palette='viridis')
plt.title('📊 Quantity Sold per Product')
plt.ylabel('Quantity Sold')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('product_sales.png')
plt.show()
