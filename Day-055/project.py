import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn import metrics
from sklearn.feature_selection import SelectKBest, f_classif
import joblib as jlb

print('========================================================')
print('         FRAUD DETECTION & TRANSACTION RISK SYSTEM')
print('========================================================\n')

#Section 1 - Data Audit
print('DATASET AUDIT')
print('--------------------------------------------------------\n')
df=pd.read_csv('transaction.csv')

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
logreg = LogisticRegression(class_weight='balanced',
    max_iter=1000)
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
print(f'Accuracy: {metrics.accuracy_score(y_test, rfc_pred)}')
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

print('Stratified Cross Validation')
print('--------------------------------------------------------\n')

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

f1_scores = cross_val_score(
    log_pipe,
    X_train,
    y_train,
    cv=cv,
    scoring='f1'
)

recall_scores = cross_val_score(
    log_pipe,
    X_train,
    y_train,
    cv=cv,
    scoring='recall'
)
precision_scores = cross_val_score(
    log_pipe,
    X_train,
    y_train,
    cv=cv,
    scoring='precision'
)
accuracy_scores = cross_val_score(
    log_pipe,
    X_train,
    y_train,
    cv=cv,
    scoring='accuracy'
)
print("Mean Accuracy:", accuracy_scores.mean())
print("Mean Precision:", precision_scores.mean())
print("Mean Recall:", recall_scores.mean())
print("Mean F1:", f1_scores.mean())

print('Threshold Tuning and Analysis')
print('--------------------------------------------------------\n')

log_pipe.fit(X_train, y_train)

y_prob = log_pipe.predict_proba(X_test)[: ,1]

thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]

for th in thresholds:
    y_pred_new = (y_prob > th).astype(int)

    print('Threshold:', th)
    print(f'Accuracy: {(metrics.accuracy_score(y_test, y_pred_new))*100:.2f}%')
    print(f'Precision: {metrics.precision_score(y_test, y_pred_new)}')
    print(f'Recall: {metrics.recall_score(y_test, y_pred_new)}')
    print(f'F1 Score: {metrics.f1_score(y_test, y_pred_new)}\n')

print('Feature Selecting ')
print('--------------------------------------------------------\n')

old_pipe = make_pipeline(create_preprocessor(), LogisticRegression(class_weight='balanced',
    max_iter=1000))

print('With All the Features')
old_pipe.fit(X_train, y_train)
old_pred = old_pipe.predict(X_test)
print(f'Accuracy: {metrics.accuracy_score(y_test, old_pred)}')
print(f'Precision: {metrics.precision_score(y_test, old_pred,zero_division=0)}')
print(f'Recall: {metrics.recall_score(y_test, old_pred,zero_division=0)}')
print(f'F1 Score: {metrics.f1_score(y_test, old_pred,zero_division=0)}\n')

selector = SelectKBest(score_func=f_classif, k=5) #lets get 5 features only

print('With best 5 Features')
new_pipe = make_pipeline(create_preprocessor(), selector, LogisticRegression(class_weight='balanced',
    max_iter=1000))
new_pipe.fit(X_train, y_train)
new_pred = new_pipe.predict(X_test)
print(f'Accuracy: {metrics.accuracy_score(y_test, new_pred)}')
print(f'Precision: {metrics.precision_score(y_test, new_pred,zero_division=0)}')
print(f'Recall: {metrics.recall_score(y_test, new_pred,zero_division=0)}')
print(f'F1 Score: {metrics.f1_score(y_test, new_pred,zero_division=0)}\n')

'''since log pipe gives us the top result, not the best, top among all the thiongs we have tried that is also the
old pipe object im gonna save that delete it and load it 

but instead of using the only the train data dor the final model i think imm gonna train the model using the entire
data we have because why waste the test data twin, might aswell use it for the final training'''

final_model_pipe = make_pipeline(create_preprocessor(), LogisticRegression(class_weight='balanced',
    max_iter=1000))
final_model_pipe.fit(X,y)
jlb.dump(final_model_pipe, 'model.pkl')

print('\n--------------------------------------------------------')
print('Model Saved SuccessFully ')
print('--------------------------------------------------------\n\n\n')


del final_model_pipe

print('Model Inference and Custom Prediction')
print('--------------------------------------------------------\n')

loaded_model = jlb.load('model.pkl')
transaction = {
    'customer_age': 34,
    'account_age_days': 420,
    'transaction_amount': 2850.75,
    'num_transactions_30d': 18,
    'avg_transaction_30d': 920.40,
    'failed_logins_7d': 4,
    'chargebacks_90d': 2,
    'distance_from_home_km': 680.5,
    'hour': 2,
    'device_trust_score': 28.5,
    'account_balance': 3200.75,
    'merchant_category': 'electronics',
    'device_type': 'mobile',
    'payment_method': 'credit_card',
    'country': 'USA',
    'channel': 'web',
    'card_present': 'No',
    'transactions_per_account_age': 2850.75 / 420,
    'daily_spend_rate': (18 / 30) * 920.40
}

prediction_data = pd.DataFrame([transaction])

prediction = loaded_model.predict(prediction_data)
probability = loaded_model.predict_proba(prediction_data)[:, 1]

print("Prediction:", prediction[0])
print("Fraud Probability:", probability[0])
print('----------------------------------------------------------')