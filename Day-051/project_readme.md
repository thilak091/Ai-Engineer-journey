# 📊 Customer Intelligence & Churn Prediction System

*An end-to-end Machine Learning pipeline built as part of the **AI Engineering Journey — Day 51**.*

This project analyzes a large customer dataset to perform two primary tasks: **Customer Churn Prediction** (Supervised Learning) and **Customer Segmentation** (Unsupervised Learning). The main goal is to demonstrate a complete, robust Machine Learning workflow—from raw data ingestion and quality checks to feature engineering, model training, evaluation, and clustering.

---

## 🚀 Project Overview

The system follows a comprehensive, production-style ML workflow:

**Raw Customer Data** ➔ **Data Quality Checks & Duplicate Removal** ➔ **Missing Value Imputation** ➔ **Feature Engineering & Selection** ➔ **Pipeline Preprocessing** ➔ **Model Training** ➔ **Threshold Analysis** ➔ **Customer Segmentation**

---

## 📂 Dataset Information

The project utilizes a synthetic customer dataset containing over **100,000 records**, specifically designed to include real-world data quality issues like missing values and duplicate rows for demonstration purposes.

*   **Features Included:** Customer ID, Age, Gender, Region, Plan Type, Contract Type, Tenure, Monthly Spend, Total Spend, Monthly Usage, Support Tickets, Complaints, Satisfaction Score, Discount Percentage, Payment Method, and Auto Pay.
*   **Target Variable:** `Churn` (0 = Retained, 1 = Churned)

> **Note:** Because this dataset is synthetic and created for educational purposes, the resulting model metrics should not be treated as real-world business benchmarks.

---

## 🧠 Machine Learning Tasks

### 1. Churn Prediction (Supervised Learning)
Predicts whether a customer is likely to cancel their subscription.
*   **Models Evaluated:** Logistic Regression, Random Forest, Gradient Boosting.
*   **Class Imbalance Handling:** The churn class is the minority. `LogisticRegression(class_weight="balanced")` was utilized to penalize minority-class errors during training.

### 2. Customer Segmentation (Unsupervised Learning)
Groups customers based on numerical behavioral metrics to identify distinct user profiles.
*   **Algorithm:** K-Means Clustering ($K=4$, selected via Inertia analysis).
*   **Features Used:** Tenure, Monthly Spend, Monthly Usage, Support Tickets, Complaints, Satisfaction.

---

## 🛠️ Data Preparation & Preprocessing

The data preparation steps are fully integrated using Scikit-Learn's `Pipeline` and `ColumnTransformer` to prevent data leakage between training and testing sets.

*   **Duplicate Removal:** Identified and dropped using `df.duplicated().sum()`.
*   **Missing Values:** 
    *   Numerical: `SimpleImputer(strategy="median")`
    *   Categorical: `SimpleImputer(strategy="most_frequent")`
*   **Feature Engineering:** Created new behavioral ratios to enrich the model:
    *   `Support Tickets Per Month` = Support Tickets / Tenure Months
    *   `Complaints Per Month` = Complaints / Tenure Months
    *   `Spend Per Tenure` = Monthly Spend / Tenure Months
*   **Feature Selection:** Evaluated using `SelectKBest(f_classif)` to isolate the most statistically significant predictors.
*   **Scaling & Encoding:** `StandardScaler` for continuous variables and `OneHotEncoder` for categorical variables.

---

## 📈 Model Evaluation & Optimization

Relying on accuracy alone is misleading for imbalanced datasets. This project comprehensively evaluates model performance using:
*   **Metrics:** Precision, Recall, F1-Score, and Confusion Matrices.
*   **Cross-Validation:** To ensure models generalize well to unseen data.
*   **Threshold Analysis:** Instead of relying on the default classification threshold, `model.predict_proba()` was used to test varying thresholds. This highlights the business trade-off between maximizing the capture of churning customers (Recall) and minimizing false alarms (Precision).

---

## ⚠️ Challenges Overcome

1.  **Data Leakage:** Prevented by strictly splitting training and testing data *before* learning preprocessing parameters via `Pipeline`.
2.  **Class Imbalance:** Accuracy paradox addressed by prioritizing F1-Score/Recall and applying balanced class weights.
3.  **Cluster Interpretation:** K-Means only outputs integer labels. Clusters were translated into actionable business profiles by analyzing the numerical averages and categorical distributions of each group.
4.  **Large Inertia Values:** With 100k+ records, absolute inertia values are naturally massive. Evaluation was shifted to relative comparison across different $K$ values rather than absolute thresholds.

---

## 💻 Technologies & Stack

*   **Language:** Python
*   **Data Manipulation:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn
*   **Key Scikit-Learn Components:** `LogisticRegression`, `RandomForestClassifier`, `GradientBoostingClassifier`, `KMeans`, `SimpleImputer`, `StandardScaler`, `OneHotEncoder`, `ColumnTransformer`, `Pipeline`, `SelectKBest`.

---

## 📁 Project Structure

```text
Project-5-Customer-Intelligence-&-Churn-Prediction-System/
│
├── data/
│   └── customer_data.csv
│
├── src/
│   └── main.py
│
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Project-5-Customer-Intelligence-Churn-Prediction-System
```

**2. Install dependencies**
```bash
pip install pandas numpy scikit-learn
# Or if using a requirements file:
# pip install -r requirements.txt
```

**3. Execute the pipeline**
```bash
python src/main.py
```
*(Ensure `customer_data.csv` is correctly placed inside the `data/` directory before running).*

---

## 🎓 What This Project Demonstrates

This project acts as a capstone, combining multiple concepts learned throughout the **AI ENGINEERING JOURNEY**:

Data Cleaning ➔ Missing Value Handling ➔ Feature Engineering ➔ Feature Selection ➔ Scaling ➔ Encoding ➔ Pipelines ➔ Cross-Validation ➔ Class Imbalance ➔ Threshold Tuning ➔ Supervised Learning ➔ Unsupervised Learning

## 🔮 Limitations & Future Improvements

**Current Limitations:**
*   Relies on synthetic data without real-world customer records.
*   No deployed prediction API or interactive custom prediction interface.
*   Exploratory Data Analysis (EDA) visualizations are kept outside the final execution script for pipeline simplicity.

**Future Roadmap:**
*   [ ] Build an interactive EDA and Customer Segmentation dashboard.
*   [ ] Save trained models using `Joblib`.
*   [ ] Wrap the prediction engine in a `FastAPI` service for deployment.
*   [ ] Test the architecture against a real-world telecommunications or SaaS churn dataset.

---
**Author:** Thilak