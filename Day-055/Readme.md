# 🛡️ Fraud Detection & Transaction Risk System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)

A comprehensive Machine Learning pipeline designed to analyze financial transactions and detect fraudulent activity. This project automates data auditing, feature engineering, model comparison, threshold tuning, and model deployment for real-time inference.

## 📋 Features

- **Data Auditing & Cleaning**: Automatically handles duplicate rows, checks for missing values, and calculates baseline fraud rates.
- **Feature Engineering**: Generates new behavioral risk features like `transactions_per_account_age` and `daily_spend_rate`.
- **Robust Preprocessing**: Built-in `scikit-learn` pipelines for imputing missing values, scaling numerical data, and one-hot encoding categorical data.
- **Model Comparison**: Evaluates and compares multiple algorithms (Logistic Regression, Random Forest, Gradient Boosting) addressing class imbalance.
- **Advanced Evaluation**: Implements 5-fold Stratified Cross-Validation and decision threshold tuning (0.3 - 0.7) for optimal precision/recall tradeoffs.
- **Feature Selection**: Compares full-feature models against reduced feature sets using `SelectKBest` (ANOVA F-value).
- **Production Ready**: Retrains the best performing model on the entire dataset, exports it using `joblib`, and demonstrates real-time inference on custom data.

## 🛠️ Prerequisites

Ensure you have Python installed. You can install the required dependencies using `pip`:

```bash
pip install pandas scikit-learn joblib
```

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/fraud-detection-system.git
   cd fraud-detection-system
   ```

2. **Add your dataset:**
   Place your dataset file named `transaction.csv` in the root directory of the project. 
   
   *Note: The dataset should contain features like `transaction_amount`, `account_age_days`, `merchant_category`, `device_type`, `country`, and a target variable column named `fraud` (1 for fraud, 0 for legitimate).*

3. **Run the pipeline:**
   ```bash
   python main.py
   ```
   *(Replace `main.py` with whatever you named your Python script).*

## 🧠 Project Pipeline

1. **Section 1 & 2: Data Audit and Cleaning** 
   Loads the dataset, drops duplicates, and prints a health summary of the data including class distribution.
2. **Section 3: Feature Engineering**
   Creates composite features to capture spending velocity and account age dynamics.
3. **Section 4: Preprocessing**
   Utilizes `ColumnTransformer` to route categorical and numerical columns through their respective cleaning and scaling pipelines.
4. **Section 5 & 6: Model Comparison & Cross Validation**
   Trains multiple models and evaluates them using Accuracy, Precision, Recall, and F1-Score to handle the highly imbalanced nature of fraud data.
5. **Threshold Tuning & Feature Selection**
   Adjusts the prediction probability thresholds to find the sweet spot for catching fraud without excessively flagging legitimate users. Evaluates top 5 features.
6. **Final Model & Inference**
   The chosen model (Logistic Regression) is trained on 100% of the data and saved as `model.pkl`. The script then loads this file and predicts the risk score of a mock transaction.

## 📦 Model Export
Upon successful execution, the script generates a `model.pkl` file. This file contains the entire preprocessing and classification pipeline, meaning you can pass raw dictionary/JSON data directly into it in your production environment (e.g., a Flask/FastAPI backend) without manually scaling or encoding the inputs.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. 

## 📝 License
This project is licensed under the MIT License.