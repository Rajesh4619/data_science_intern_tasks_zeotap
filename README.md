# Customer Insights and Analysis Project

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

#### **Code Highlights**:
- Used `pandas`, `matplotlib`, and `seaborn` for data manipulation and visualization.

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

#### **Code Highlights**:
- Used `scikit-learn` for similarity computation.
- Resulting CSV structure:
    | CustomerID | Lookalikes                       |
    |------------|----------------------------------|
    | C0001      | [(C0010, 0.98), (C0005, 0.94)] |
    | C0002      | [(C0011, 0.96), (C0008, 0.92)] |

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

#### **Code Highlights**:
- Used `scikit-learn` for clustering and evaluation metrics.
- Resulting clusters visualized in 2D space:
   
---

## Results
### **Key Insights**:
1. **From Task 1**:
   - Identified regional distribution and top-performing products.
   - Observed monthly sales trends, providing insights into seasonality.

2. **From Task 2**:
   - Successfully identified lookalike customers for personalized recommendations.

3. **From Task 3**:
   - Segmented customers into distinct clusters, enabling targeted marketing strategies.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `pandas`, `numpy`: Data manipulation
  - `matplotlib`, `seaborn`: Visualization
  - `scikit-learn`: Similarity computation, clustering, and metrics
  - `PCA`: Dimensionality reduction for cluster visualization

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-insights-analysis.git

2. pip install -r requirements.txt
3. Place the datasets (Customers.csv, Products.csv, Transactions.csv) in the data/ directory.
4. Run the scripts:
    Task 1: Tadipi_Rajesh_EDA.py
    Task 2: Tadipi_Rajesh_lookalike.py
    Task 3: Tadipi_Rajesh_clustering.py
   
Files in Repository
 Tadipi_Rajesh_EDA.py: Script for exploratory data analysis.
Tadipi_Rajesh_lookalike.py: Script for lookalike customer recommendation.
Tadipi_Rajesh_clustering.py: Script for customer segmentation.
Tadipi_Rajesh_Lookalike.csv: Output of Task 2.
Tadipi_Rajesh_Clustering.csv: Output of Task 3.

Future Enhancements
Incorporate additional datasets for deeper insights (e.g., customer feedback).
Explore advanced clustering algorithms like DBSCAN or hierarchical clustering.
Deploy the project as a web app for real-time analysis.
Author
Tadipi Rajesh
Passionate about backend development and machine learning. Connect with me on LinkedIn.

License
This project is licensed under the MIT License. See the LICENSE file for details.


### Notes:
- Replace `https://github.com/yourusername/customer-insights-analysis.git` with your actual GitHub repository URL.
- Add real visualizations to replace the placeholder links in the **Task 1** and **Task 3** sections.
- Ensure the file structure mentioned in the **How to Run** section matches your actual project structure. 

Let me know if you'd like help fine-tuning this further!


