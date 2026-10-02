import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn import metrics

print('========================================================')
print('         FRAUD DETECTION & TRANSACTION RISK SYSTEM')
print('========================================================\n')

#Section 1 - Data Audit
print('DATASET AUDIT')
print('--------------------------------------------------------\n')
df=pd.read_csv('transactions.csv')

print(f'Original Dataset Shape: {df.shape}')
print(f'Duplicate Rows: {df.duplicated().sum().sum()}')
print(f'Missing Cells: {df.isna().sum().sum()}')
print(f'Fraud Transactions {(df['fraud']==1).sum()}')
print(f'Legitimate Transactions {(df['fraud']==0).sum()}')
print(f'Fraud Rate: {((df['fraud']==1).sum())/(((df['fraud']==0).sum())+((df['fraud']==1).sum()))*100:.2f}%\n')

#Section 2 - Data Cleaning
print('DATASET CLEANING')
print('--------------------------------------------------------\n')

print(f'Duplicates Removed: {df.duplicated().sum().sum()}')
df.drop_duplicates(inplace=True)
print(f'Missing Cells Before Imputation: {df.isna().sum().sum()}')
print('Engineered Features: 2')

#SECTION 3 — FEATURE ENGINEERING
df['transactions_per_account_age'] = df['transaction_amount']/df['account_age_days']
df['daily_spend_rate'] = (df['num_transactions_30d']/30)*df['avg_transaction_30d']

#Section 4- Preprocessing
def create_preprocessor():
    categ = ['merchant_category', 'device_type', 'payment_method','country',
       'channel', 'card_present' ]

    numeric = ['customer_age', 'account_age_days', 'transaction_amount', 
           'num_transactions_30d', 'avg_transaction_30d', 'failed_logins_7d', 'chargebacks_90d', 
           'distance_from_home_km', 'hour', 'device_trust_score', 'account_balance',
           'transactions_per_account_age', 'daily_spend_rate']

    cat_pipe = make_pipeline(SimpleImputer(strategy='most_frequent'),OneHotEncoder(handle_unknown='ignore'))
    num_pipe = make_pipeline(SimpleImputer(strategy='median'), StandardScaler())

    return ColumnTransformer([
    ('cat', cat_pipe, categ),
    ('num', num_pipe, numeric)])

X= df.drop(columns=['transaction_id','fraud'])
y= df['fraud']
X_train, X_test, y_train, y_test= train_test_split(
    X, y, test_size=0.2, random_state=41, stratify=y)

#Section 5 and 6- Class Imbalance and Model Comparision
print('MODEL COMPARISON')
print('--------------------------------------------------------\n')

print('Logistic Regression:')
logreg = LogisticRegression(class_weight='balanced')
log_pipe = make_pipeline(create_preprocessor(), logreg)

log_pipe.fit(X_train, y_train)
log_pred = log_pipe.predict(X_test)
print(f'Accuracy: {metrics.accuracy_score(y_test, log_pred)}')
print(f'Precision: {metrics.precision_score(y_test, log_pred,zero_division=0)}')
print(f'Recall: {metrics.recall_score(y_test, log_pred,zero_division=0)}')
print(f'F1 Score: {metrics.f1_score(y_test, log_pred,zero_division=0)}\n')

print('Random Forest:')
rfc = RandomForestClassifier(class_weight='balanced')
rfc_pipe= make_pipeline(create_preprocessor(), rfc)

rfc_pipe.fit(X_train, y_train)
rfc_pred = rfc_pipe.predict(X_test)
print(f'Accuracy: {metrics.accuracy_score(y_test, rfc_pred,)}')
print(f'Precision: {metrics.precision_score(y_test, rfc_pred,zero_division=0)}')
print(f'Recall: {metrics.recall_score(y_test, rfc_pred,zero_division=0)}')
print(f'F1 Score: {metrics.f1_score(y_test, rfc_pred,zero_division=0)}\n')

print('Gradient Boosting:')
gbc = GradientBoostingClassifier()
gbc_pipe = make_pipeline(create_preprocessor(), gbc)

gbc_pipe.fit(X_train, y_train)
gbc_pred = gbc_pipe.predict(X_test)
print(f'Accuracy: {metrics.accuracy_score(y_test, gbc_pred)}')
print(f'Precision: {metrics.precision_score(y_test, gbc_pred,zero_division=0)}')
print(f'Recall: {metrics.recall_score(y_test, gbc_pred,zero_division=0)}')
print(f'F1 Score: {metrics.f1_score(y_test, gbc_pred,zero_division=0)}\n')


