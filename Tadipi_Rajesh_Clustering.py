import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import davies_bouldin_score, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Read in the files
customers = pd.read_csv('C:/Users/tadip/Downloads/D/Customers.csv')
transactions = pd.read_csv('C:/Users/tadip/Downloads/D/Transactions.csv')
products = pd.read_csv('C:/Users/tadip/Downloads/D/Products.csv')


# Merging the data
transactions_merged = transactions.merge(customers, on="CustomerID", how="left")
transactions_merged = transactions_merged.merge(products, on="ProductID", how="left")

# Group transaction data by customer and calculate features
customer_features = transactions_merged.groupby("CustomerID").agg(
    total_spent=("TotalValue", "sum"),
    avg_price=("Price_y", "mean"),
    total_quantity=("Quantity", "sum"),
unique_products=("ProductID", "nunique"),
    region=("Region", "first"),
    categories=("Category", lambda x: ', '.join(set(x)))
).reset_index()

# Encode categorical variables (Region)
customer_features = pd.get_dummies(customer_features, columns=["region"], drop_first=True)

# Prepare features for clustering
numeric_features = customer_features.drop(columns=["CustomerID", "categories"])
scaler = StandardScaler()
numeric_features_scaled = scaler.fit_transform(numeric_features)

# Use K-Means clustering for different number of clusters
cluster_results = {}
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(numeric_features_scaled)
db_index = davies_bouldin_score(numeric_features_scaled, cluster_labels)
silhouette_avg = silhouette_score(numeric_features_scaled, cluster_labels)
cluster_results[k] = {
        "model": kmeans,
        "db_index": db_index,
        "silhouette": silhouette_avg,
        "labels": cluster_labels
    }

# Choose the best number of clusters with the lowest DB Index
best_k = min(cluster_results, key=lambda k: cluster_results[k]["db_index"])
best_model = cluster_results[best_k]["model"]
best_labels = cluster_results[best_k]["labels"]

# Append the best cluster labels to total_dataset
total_customer_data = customer_features.copy()
total_customer_data["Cluster"] = best_labels

# Plot the clusters with PCA reducing dimensionality
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(numeric_features_scaled)

plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=reduced_features[:, 0],
    y=reduced_features[:, 1],
    hue=best_labels,
    palette="viridis",
    legend="full",
)
plt.title(f"Customer Clusters (k={best_k})", fontsize=14)
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(title="Cluster", loc="best")
plt.show()

# Save clustering results
clustering_results_path = "Tadipi_Rajesh_Clustering.csv"
total_customer_data.to_csv(clustering_results_path, index=False)

# Print summary
print(f"Best number of clusters: {best_k}")
print(f"Davies-Bouldin Index for best model: {cluster_results[best_k]['db_index']:.4f}")
print(f"Silhouette Score for best model: {cluster_results[best_k]['silhouette']:.4f}")
print(f"Clustering results saved to {clustering_results_path}")
