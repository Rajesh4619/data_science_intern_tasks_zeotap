# Ecommerce Transactions Dataset Analysis

## Overview
This project analyzes customer, product, and transaction data to derive actionable insights, recommend similar customers, and segment customers into distinct clusters. The project is structured into three main tasks:

1. **Exploratory Data Analysis (EDA)**: Identifying trends in customer, product, and transaction data.
2. **Lookalike Customer Recommendation**: Leveraging cosine similarity to find customers with similar purchasing patterns.
3. **Customer Segmentation**: Using K-Means clustering to group customers into meaningful segments.

---

## Data Sources
The analysis is based on three datasets:
- **Customers.csv**: Contains customer details like `Region` and `SignupDate`.
- **Products.csv**: Includes product attributes such as `Category` and `Price`.
- **Transactions.csv**: Stores transaction data, including `TransactionDate`, `Quantity`, and `TotalValue`.

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

5.Future Enhancements
   - Incorporate additional datasets for deeper insights (e.g., customer feedback).
   - Explore advanced clustering algorithms like DBSCAN or hierarchical clustering.
   - Deploy the project as a web app for real-time analysis.


   
Author
- Tadipi Rajesh
- Passionate about backend development and machine learning.



