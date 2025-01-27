# Ecommerce Transactions Dataset

## Overview
This project involves analyzing customer, product, and transaction data to derive actionable insights, recommend lookalike customers, and segment customers into distinct clusters. The project is divided into three key tasks:

1. **Exploratory Data Analysis (EDA)**: Visualizing customer, product, and transaction trends.
2. **Lookalike Customer Recommendation**: Using cosine similarity to find customers with similar purchasing behavior.
3. **Customer Segmentation**: Applying K-Means clustering to group customers into distinct segments.

---

## Data Sources
The analysis utilizes the following datasets:
- **Customers.csv**: Contains information about customers, including their `Region` and `SignupDate`.
- **Products.csv**: Contains product details like `Category` and `Price`.
- **Transactions.csv**: Contains transaction details, including `TransactionDate`, `Quantity`, and `TotalValue`.

---

## Tasks and Approach

### **Task 1: Exploratory Data Analysis (EDA)**
**Objective**: Understand customer demographics, product preferences, and transaction trends.

#### **Steps**:
1. Loaded and preprocessed data:
   - Converted date columns to `datetime`.
   - Checked for missing values and summarized the data.
2. Analyzed key metrics:
   - Customer distribution by region.
   - Product category preferences.
   - Monthly sales trends.
   - Top 10 products by sales.
3. Visualized insights using:
   - Bar plots for categorical distributions.
   - Line plot for monthly sales trends.

---

### **Task 2: Lookalike Customer Recommendation**
**Objective**: Recommend the top 3 most similar customers (lookalikes) for each customer.

#### **Steps**:
1. Merged `Customers.csv`, `Products.csv`, and `Transactions.csv` to create a comprehensive dataset.
2. Computed customer-specific features:
   - Total amount spent.
   - Average price of purchased products.
   - Total quantity of products bought.
   - Number of unique products purchased.
3. Preprocessed numeric features using `StandardScaler`.
4. Calculated cosine similarity between customers and identified the top 3 lookalikes for the first 20 customers.
5. Saved the recommendations to a CSV file (`Tadipi_Rajesh_Lookalike.csv`).

---

### **Task 3: Customer Segmentation**
**Objective**: Cluster customers into distinct groups based on their purchasing behavior.

#### **Steps**:
1. Merged datasets and computed customer features (similar to Task 2).
2. Encoded categorical variables (e.g., `Region`) and scaled numeric features using `StandardScaler`.
3. Applied K-Means clustering for `k` ranging from 2 to 10.
4. Evaluated clustering performance using:
   - **Davies-Bouldin Index**: Lower is better.
   - **Silhouette Score**: Higher is better.
5. Selected the best number of clusters (`k`) based on the lowest Davies-Bouldin Index.
6. Visualized clusters using PCA for dimensionality reduction.
7. Saved clustering results to a CSV file (`Tadipi_Rajesh_Clustering.csv`).

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rajesh4619/data_science_intern_tasks_zeotap.git
2. Install dependencies:
   Ensure you have Python installed, then run:
   pip install -r requirements.txt
3. Prepare datasets:
   Place the following files in the data/ directory:
   
   Customers.csv
   Products.csv
   Transactions.csv

4. Run the scripts:
   Task 1: Exploratory Data Analysis (EDA)
   Run the following command to generate visualizations and insights:
   python Tadipi_Rajesh_EDA.py

   Task 2: Lookalike Customer Recommendation
   Run the following command to generate the lookalike recommendations CSV:
   python Tadipi_Rajesh_lookalike.py
   
   Task 3: Customer Segmentation
   Run the following command to perform clustering and save the results:

5.Future Enhancements
   Incorporate additional datasets for deeper insights (e.g., customer feedback).
   Explore advanced clustering algorithms like DBSCAN or hierarchical clustering.
   Deploy the project as a web app for real-time analysis.


   
Author
Tadipi Rajesh
Passionate about backend development and machine learning.

Connect with me on LinkedIn.


