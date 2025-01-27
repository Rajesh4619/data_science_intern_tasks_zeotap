# Data Science Intern Tasks - Zeotap

This repository contains Data Science Intern Tasks - Zeotap. The focus is on analyzing e-commerce transaction data to derive actionable insights and build customer-focused solutions.

---

## Project Context

In the competitive e-commerce landscape, understanding customer behavior is critical for improving customer retention, boosting sales, and personalizing marketing strategies. This project uses data science techniques to analyze customer transactions, identify patterns, and group customers into meaningful segments.

Key goals:
1. Explore customer, product, and transaction data for trends and insights.
2. Recommend similar customers using purchasing behavior.
3. Segment customers into distinct groups to enable targeted marketing strategies.

---
Dataset Links:
- [Customers.csv](https://drive.google.com/file/d/1bu_--mo79VdUG9oin4ybfFGRUSXAe-WE/view?usp=sharing)
- [Products.csv](https://drive.google.com/file/d/1IKuDizVapw-hyktwfpoAoaGtHtTNHfd0/view?usp=sharing)
- [Transactions.csv](https://drive.google.com/file/d/1saEqdbBB-vuk2hxoAf4TzDEsykdKlzbF/view?usp=sharing)

---
## Dataset Overview

The dataset consists of three files:
1. **Customers.csv**
   - `CustomerID`: Unique identifier for each customer.
   - `CustomerName`: Name of the customer.
   - `Region`: Continent where the customer resides.
   - `SignupDate`: Date when the customer signed up.

2. **Products.csv**
   - `ProductID`: Unique identifier for each product.
   - `ProductName`: Name of the product.
   - `Category`: Product category.
   - `Price`: Product price in USD.

3. **Transactions.csv**
   - `TransactionID`: Unique identifier for each transaction.
   - `CustomerID`: ID of the customer who made the transaction.
   - `ProductID`: ID of the product sold.
   - `TransactionDate`: Date of the transaction.
   - `Quantity`: Quantity of the product purchased.
   - `TotalValue`: Total value of the transaction.
   - `Price`: Price of the product sold.
---

## Key Tasks and Methodology

### Task 1: Exploratory Data Analysis (EDA)
**Goal**: Understand customer demographics, product preferences, and transaction patterns.

#### Methodology:
1. Data Preprocessing:
   - Converted date columns to `datetime` format.
   - Handled missing values and summarized data.
2. Metrics Analyzed:
   - Customer distribution by region.
   - Most popular product categories.
   - Monthly sales trends.
   - Top 10 products by sales volume.
3. Visualizations:
   - Bar charts for category distributions.
   - Line charts for sales trends over time.

---

### Task 2: Lookalike Customer Recommendation
**Goal**: Identify the top 3 customers with the most similar purchasing behavior for each customer.

#### Methodology:
1. Data Preparation:
   - Merged datasets to create a unified customer profile.
2. Feature Engineering:
   - Total spending, average product price, total quantity purchased, and unique products bought.
3. Preprocessing:
   - Normalized numeric features using `StandardScaler`.
4. Similarity Computation:
   - Calculated pairwise cosine similarity and identified the top 3 similar customers for the first 20 customers.
5. Output:
   - Recommendations saved in `Tadipi_Rajesh_Lookalike.csv`.

---

### Task 3: Customer Segmentation
**Goal**: Cluster customers based on their purchasing patterns.

#### Methodology:
1. Data Preparation:
   - Merged datasets and engineered customer-level features.
2. Preprocessing:
   - Encoded categorical variables and scaled numeric features.
3. Clustering:
   - Applied K-Means clustering for `k` values ranging from 2 to 10.
   - Evaluated using:
     - **Davies-Bouldin Index** (lower is better).
     - **Silhouette Score** (higher is better).
4. Results:
   - Selected the optimal `k` based on evaluation metrics.
   - Visualized clusters using PCA for dimensionality reduction.
5. Output:
   - Results saved in `Tadipi_Rajesh_Clustering.csv`.

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rajesh4619/data_science_intern_tasks_zeotap.git
   
2. Install dependencies:
   - Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
4. Prepare datasets:
   - Place the following files in the data/ directory:
   
   Customers.csv
   Products.csv
   Transactions.csv

5. Run the scripts:
   - Task 1: Exploratory Data Analysis (EDA)
   - Run the following command to generate visualizations and insights:
      ```bash
      python Tadipi_Rajesh_EDA.py

   - Task 2: Lookalike Customer Recommendation
   - Run the following command to generate the lookalike recommendations CSV:
      ```bash
      python Tadipi_Rajesh_lookalike.py
   
   -Task 3: Customer Segmentation
   -Run the following command to perform clustering and save the results:
      ```bash
       python Tadipi_Rajesh_clustering.py

#### Key Insights
1. Customer Behavior:
   - High-value customers with frequent transactions were identified.
   - Seasonal trends and popular products were observed.
2. Lookalike Customers:
   - Customers with similar purchasing patterns were successfully identified, enabling personalized marketing campaigns.
3. Customer Segments:
   - Customers were grouped into distinct clusters such as "High Spenders," "Frequent Buyers," and "Low Engagement."
   - These insights enable tailored promotions and retention strategies.

#### Future Work
**Goal**: Potential extensions and improvements for this project include:

1.Predictive Analytics:
   - Use machine learning models to predict future customer behavior, such as likelihood to churn or next product to purchase.

2. Real-Time Recommendations:
   - Build a pipeline to recommend products or customers in real-time using streaming data.

3. Enhanced Segmentation:
   - Incorporate advanced clustering methods like DBSCAN or hierarchical clustering to capture more nuanced customer segments.

4. Dashboard Development:
   - Create an interactive dashboard with tools like Streamlit or Dash for real-time visualization and reporting.


   
  Author
- Tadipi Rajesh
- Passionate about backend development and machine learning.



