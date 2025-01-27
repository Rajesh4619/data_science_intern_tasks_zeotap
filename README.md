# data_science_intern_tasks_zeotap


# Data Science Assignment: eCommerce Transactions Dataset

This repository contains the solution for the Data Science assignment focused on analyzing an eCommerce Transactions dataset. The tasks include exploratory data analysis, building a lookalike model, and performing customer segmentation.

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

Dataset Links:
- [Customers.csv](https://drive.google.com/file/d/1bu_--mo79VdUG9oin4ybfFGRUSXAe-WE/view?usp=sharing)
- [Products.csv](https://drive.google.com/file/d/1IKuDizVapw-hyktwfpoAoaGtHtTNHfd0/view?usp=sharing)
- [Transactions.csv](https://drive.google.com/file/d/1saEqdbBB-vuk2hxoAf4TzDEsykdKlzbF/view?usp=sharing)

---

## Assignment Tasks

### Task 1: Exploratory Data Analysis (EDA) and Business Insights
- **Objective**: Perform EDA on the dataset and derive at least 5 actionable business insights.
- **Deliverables**:
  - A Jupyter Notebook or Python script with the EDA code.
  - A PDF report summarizing the insights.

### Task 2: Lookalike Model
- **Objective**: Build a model to recommend 3 similar customers based on user profile and transaction history.
- **Deliverables**:
  - A Jupyter Notebook or Python script with the model implementation.
  - A CSV file (`Lookalike.csv`) containing recommendations for the first 20 customers (`C0001` - `C0020`).

### Task 3: Customer Segmentation / Clustering
- **Objective**: Perform customer segmentation using clustering techniques with data from both Customers.csv and Transactions.csv.
- **Deliverables**:
  - A report detailing the number of clusters, DB Index value, and other metrics.
  - A Jupyter Notebook or Python script with clustering code.

---

## Submission Guidelines
1. Upload all files to a public GitHub repository.
2. File naming conventions:
   - `FirstName_LastName_EDA.pdf`
   - `FirstName_LastName_EDA.ipynb`
   - `FirstName_LastName_Lookalike.csv`
   - `FirstName_LastName_Lookalike.ipynb`
   - `FirstName_LastName_Clustering.pdf`
   - `FirstName_LastName_Clustering.ipynb`

---

## Evaluation Criteria
- **Exploratory Data Analysis (EDA)**: 25%
- **Business Insights**: 15%
- **Lookalike Model**: 30%
- **Customer Segmentation**: 30%

---

## Final Note
This assignment emphasizes practical application of data science skills. Ensure your code is clean, efficient, and insightful. Good luck!
