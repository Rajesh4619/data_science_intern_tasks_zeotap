import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
customers = pd.read_csv('C:/Users/tadip/Downloads/D/Customers.csv')
products = pd.read_csv('C:/Users/tadip/Downloads/D/Products.csv')
transactions = pd.read_csv('C:/Users/tadip/Downloads/D/Transactions.csv')

# Convert dates to datetime format
customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

# Check for missing values
missing_customers = customers.isnull().sum()
missing_products = products.isnull().sum()
missing_transactions = transactions.isnull().sum()

# Summary statistics
customer_region_dist = customers['Region'].value_counts()
product_category_dist = products['Category'].value_counts()
total_sales = transactions['TotalValue'].sum()
avg_transaction_value = transactions['TotalValue'].mean()

# Top products by sales
transactions_merged = transactions.merge(products, on='ProductID')
top_products = (transactions_merged.groupby('ProductName')['TotalValue']
                .sum()
                .sort_values(ascending=False)
                .head(10))

# Monthly sales trend
transactions['Month'] = transactions['TransactionDate'].dt.to_period('M')
monthly_sales = transactions.groupby('Month')['TotalValue'].sum()

# Plotting
sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Region distribution
sns.countplot(data=customers, x='Region', ax=axes[0, 0], palette="viridis")
axes[0, 0].set_title("Customer Distribution by Region")

# Product category distribution
sns.countplot(data=products, y='Category', ax=axes[0, 1], palette="cubehelix")
axes[0, 1].set_title("Product Distribution by Category")

# Monthly sales trend
monthly_sales.plot(ax=axes[1, 0], color="b")
axes[1, 0].set_title("Monthly Sales Trend")
axes[1, 0].set_ylabel("Total Sales")

# Top products by sales
sns.barplot(x=top_products.values, y=top_products.index, ax=axes[1, 1], palette="magma")
axes[1, 1].set_title("Top 10 Products by Sales")

plt.tight_layout()
plt.show()


