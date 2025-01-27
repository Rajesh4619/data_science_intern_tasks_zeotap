# Data Science Intern Tasks - Zeotap

This repository contains the tasks and solutions for a Data Science assignment focused on analyzing an **eCommerce Transactions dataset**. The work encompasses **Exploratory Data Analysis (EDA)**, **Lookalike Modeling**, and **Customer Segmentation** to derive actionable insights and build data-driven strategies.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Tasks Overview](#tasks-overview)
    - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Lookalike Modeling](#lookalike-modeling)
    - [Customer Segmentation](#customer-segmentation)
4. [Approach](#approach)
5. [File Structure](#file-structure)
6. [How to Run](#how-to-run)
7. [Conclusions](#conclusions)
8. [License](#license)

---

## Introduction
The main objective of this repository is to analyze customer behavior, identify patterns, and develop models to support data-driven marketing strategies. Each task was carefully approached to ensure robust analysis and meaningful results.

---

## Dataset
The dataset consists of **eCommerce transaction data**, including information such as customer IDs, transaction values, timestamps, and product details. The data is anonymized to ensure privacy.

---

## Tasks Overview

### 1. Exploratory Data Analysis (EDA)
- **Objective**: To explore the dataset, understand its structure, and identify patterns or anomalies.
- **Key Steps**:
  - Data cleaning and preprocessing.
  - Generating descriptive statistics.
  - Visualizing key insights (e.g., sales trends, customer behavior, etc.).
  
### 2. Lookalike Modeling
- **Objective**: To build a model that identifies customers similar to a target group for effective marketing campaigns.
- **Key Steps**:
  - Feature engineering (e.g., RFM analysis: Recency, Frequency, and Monetary value).
  - Applying machine learning models to classify or rank customers.

### 3. Customer Segmentation
- **Objective**: To segment customers into distinct groups for personalized marketing.
- **Key Steps**:
  - Using clustering algorithms (e.g., K-Means or hierarchical clustering).
  - Visualizing clusters and analyzing segment profiles.

---

## Approach

### General Workflow:
1. **Data Preparation**: 
   - Handled missing values, outliers, and inconsistencies.
   - Standardized and normalized features for modeling.

2. **EDA**:
   - Created visualizations to uncover trends and outliers using tools like `matplotlib` and `seaborn`.
   - Analyzed distributions, correlations, and time-series trends.

3. **Lookalike Modeling**:
   - Defined the target group based on specific criteria (e.g., high-value customers).
   - Engineered features for predictive modeling and evaluated model performance.

4. **Customer Segmentation**:
   - Performed dimensionality reduction using PCA for high-dimensional data.
   - Applied clustering techniques and validated results using metrics like Silhouette Score.

5. **Visualization**:
   - Used Python libraries to create meaningful plots and dashboards to represent results.

---

## File Structure
data_science_intern_tasks_zeotap/ ├── data/ │ ├── raw_dataset.csv # Original dataset │ ├── processed_dataset.csv # Cleaned and prepared data ├── notebooks/ │ ├── Tadipi_Rajesh_EDA.py # Exploratory Data Analysis │ ├── 2Tadipi_Rajesh_Lookalike.py # Lookalike Modeling │ ├── 3Tadipi_Rajesh_Culstering.py # Customer Segmentation ├── visualizations/ │ ├── eda_plots.png # EDA visualizations │ ├── segmentation_clusters.png # Cluster analysis plots ├── README.md # Project documentation └── requirements.txt # Dependencies
