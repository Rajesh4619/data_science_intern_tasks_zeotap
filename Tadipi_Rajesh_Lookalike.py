import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

customers = pd.read_csv('C:/Users/tadip/Downloads/D/Customers.csv')
products = pd.read_csv('C:/Users/tadip/Downloads/D/Products.csv')
transactions = pd.read_csv('C:/Users/tadip/Downloads/D/Transactions.csv')


# Merge datasets
transactions_merged = transactions.merge(customers, on="CustomerID", how="left")
transactions_merged = transactions_merged.merge(products, on="ProductID", how="left")

# Aggregate transaction data to compute customer-specific features
customer_features = transactions_merged.groupby("CustomerID").agg(
    total_spent=("TotalValue", "sum"),
    avg_price=("Price_y", "mean"),
    total_quantity=("Quantity", "sum"),
    unique_products=("ProductID", "nunique"),
    region=("Region", "first"),
    categories=("Category", lambda x: ', '.join(set(x)))
).reset_index()

# Preprocess the data before feeding it into the cosine_similarity method
numeric_features = customer_features[["total_spent", "avg_price", "total_quantity", "unique_products"]]
scaler = StandardScaler()
numeric_features_scaled = scaler.fit_transform(numeric_features)

# co-sines similarity computation
similarity = cosine_similarity(numeric_features_scaled)
customer_ids = customer_features["CustomerID"].tolist()

# Pick the 3 best doppelgängers for the first 20 customers (C0001 - C0020)
lookalike_results = []
for i in range(20):
    customer_id = customer_ids[i]
    similarities = list(enumerate(similarity[i]))
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[1:4]  # Top 3 excluding self
    top_similar = [(customer_ids[j], round(score, 4)) for j, score in similarities]
    lookalike_results.append((customer_id, top_similar))

# Create and save the Lookalike 

# Create and save the Lookalike CSV
lookalike_df = pd.DataFrame({
    "CustomerID": [result[0] for result in lookalike_results],
    "Lookalikes": [result[1] for result in lookalike_results]
})

lookalike_csv_path = "Tadipi_Rajesh_Lookalike.csv"
lookalike_df.to_csv(lookalike_csv_path, index=False)

print(f"Lookalike recommendations saved to {lookalike_csv_path}")