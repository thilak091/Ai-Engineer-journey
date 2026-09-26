import pandas as pd
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import metrics
from sklearn.cluster import KMeans

print('========================================================')
print('         CUSTOMER INTELLIGENCE AND CHURN SYSTEM')
print('========================================================')

print('\nDataset')
print('--------------------------------------------------------')

CURRENT_DIR = Path(__file__).resolve().parent
CSV_PATH = CURRENT_DIR.parent / "data" / "customer_data.csv"

df=pd.read_csv(CSV_PATH)
print(f'Shape: {df.shape}\n')
print(f'Number of Duplicate rows: {df.duplicated().sum()}\n')  #only 500 duplicate rows
print(f'Number of Missing Values: {df.isna().sum().sum()}\n')    # more that 8000 missing values

'''since only 500 duplicate rows that is 0.5 percent of the data, i decide to remove it


in the case of missing values since it is around 
26 percent of the actual data i decide to impute it'''
#Data Cleaning
df.drop_duplicates(inplace=True)

print('TARGET DISTRIBUTION')
print('--------------------------------------------------------')
print('Churn Distribution:\n')
print(f'Retained: {(df['churn']==0).sum()}\n')
print(f'Churned: {(df['churn']==1).sum()}\n')
print(f'Churn Rate: {(((df['churn']==1).sum())/(((df['churn']==1).sum())+((df['churn']==0).sum())))*100:.2f}%\n')

''' Im skipping the graphs, its not for me'''

#SECTION 4-Feature Engineering

df['support_tickets_per_month'] = df['support_tickets']/df['tenure_months']
df['complaints_per_month'] = df['complaints']/df['tenure_months']
df['spend_per_tenure'] = df['monthly_spend']/df['tenure_months']
# 3 Important Feature Engineered out of existing features


#SECTION 5-Feature Selection
X = df[['region','plan_type','contract_type','tenure_months','monthly_spend','total_spend',
        'monthly_usage_hours','support_tickets','complaints','satisfaction_score','discount_percent',
        'payment_method','auto_pay','support_tickets_per_month','complaints_per_month','spend_per_tenure']]
y = df['churn']
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2,  stratify=y, random_state=4)

categ= ['region', 'plan_type', 'contract_type',
        'payment_method', 'auto_pay']

numeric= ['tenure_months', 'monthly_spend',
          'total_spend', 'monthly_usage_hours', 'support_tickets',
          'complaints', 'satisfaction_score', 'discount_percent'
          ,'support_tickets_per_month','complaints_per_month','spend_per_tenure']

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categ),
        ('num', SimpleImputer(strategy='median'),numeric)
    ],
    remainder='passthrough'
)
X_ohe = preprocessor.fit_transform(X_train)
skb = SelectKBest(score_func=f_classif, k=7)
X_skb=skb.fit_transform(X_ohe,y_train)
pipe1= make_pipeline(preprocessor,skb)

#Section 7 and 8 with 9
print('MODEL COMPARISON AND EVALUATION')
print('--------------------------------------------------------\n')

logreg= LogisticRegression(class_weight='balanced',max_iter=1000)
rfc=RandomForestClassifier(n_estimators=50,min_samples_leaf=10)
xgb= GradientBoostingClassifier(n_estimators=50,min_samples_leaf=10, learning_rate=0.25)

logreg.fit(X_skb, y_train)
rfc.fit(X_skb, y_train)
xgb.fit(X_skb, y_train)

l_pred = logreg.predict(pipe1.transform(X_test))
r_pred = rfc.predict(pipe1.transform(X_test))
g_pred = xgb.predict(pipe1.transform(X_test))

print('Logistic Regression:')
print(metrics.classification_report(y_test,l_pred, zero_division=0))

print('Random Forest:')
print(metrics.classification_report(y_test,r_pred, zero_division=0))

print('Gradient Boosting:')
print(metrics.classification_report(y_test,g_pred, zero_division=0))

'''since RFC and XGB are not even considering the class 1,
precision and Recall remains zero , but using Lograg with weights balanced improves the recall of 1 
eventhough it reduces accuracy'''

#Section 6 with 9
print('PREPROCESSING PIPELINE')
print('--------------------------------------------------------\n')

numeric= ['tenure_months', 'monthly_spend',
          'total_spend', 'monthly_usage_hours', 'support_tickets',
          'complaints', 'satisfaction_score', 'discount_percent'
          ,'support_tickets_per_month','complaints_per_month','spend_per_tenure']

categ= ['region', 'plan_type', 'contract_type',
        'payment_method', 'auto_pay']

num_pipe= make_pipeline(SimpleImputer(strategy='median'), StandardScaler())
cat_pipe= make_pipeline(SimpleImputer(strategy='most_frequent'),OneHotEncoder(handle_unknown='ignore'))

col_trans=ColumnTransformer([
    ('num', num_pipe, numeric),
    ('cat', cat_pipe, categ)])

pipe= make_pipeline(col_trans, LogisticRegression(class_weight='balanced'))
scores= cross_val_score(pipe, X, y, cv=5, scoring='accuracy')
print(f'Accuracy:{scores.mean()}\n')

#Section 10 - Threshold Tuning
print('THRESHOLD ANALYSIS')
print('--------------------------------------------------------\n')

logreg1 = LogisticRegression(class_weight='balanced')
thresholds=[0.30, 0.40, 0.50, 0.60, 0.70]
std=StandardScaler()
scaled=std.fit_transform(X_skb)
logreg1.fit(scaled, y_train)
y_pred_prob = logreg1.predict_proba(std.transform(pipe1.transform(X_test)))[:, 1]
for t in thresholds:
    y_pred_new = (y_pred_prob>=t).astype(int)
    print('Threshold:', t)
    print(f'Precision: {metrics.precision_score(y_test,y_pred_new,zero_division=0)}')
    print(f'Recall: {metrics.recall_score(y_test,y_pred_new)}')
    print(f'F1: {metrics.f1_score(y_test,y_pred_new)}\n')
    
# SECTION 11 - CUSTOMER SEGMENTATION
print('\nCUSTOMER SEGMENTATION')
print('--------------------------------------------------------')

# Numerical features used for clustering
cluster_numeric = [
    'tenure_months',
    'monthly_spend',
    'monthly_usage_hours',
    'support_tickets',
    'complaints',
    'satisfaction_score'
]

# Prepare clustering data
si = SimpleImputer(strategy='median')
X_imputed = si.fit_transform(df[cluster_numeric])

std = StandardScaler()
X_scaled = std.fit_transform(X_imputed)

# Find suitable K
print('\nFinding K:')
for k in [2, 3, 4, 5, 6]:
    km = KMeans(n_clusters=k, n_init=10, random_state=4)
    km.fit(X_scaled)
    print(f'K={k} -> Inertia: {km.inertia_:.2f}')

# Select K=4 for this project
kmeans = KMeans(n_clusters=4, n_init=10, random_state=4)
labels = kmeans.fit_predict(X_scaled)

print('\nSelected K Value: 4')

# Add cluster labels
profile_df = df.copy()
profile_df['cluster'] = labels

# Cluster sizes
print('\nCluster Sizes:')
print(profile_df['cluster'].value_counts().sort_index())

# Numerical cluster profiles
print('\nCluster Profiles:')
print(
    profile_df.groupby('cluster')[cluster_numeric]
    .mean()
    .round(2)
)

# Overall averages for comparison
print('\nOverall Averages:')
print(
    profile_df[cluster_numeric]
    .mean()
    .round(2)
)

# Most common plan and contract
print('\nCommon Characteristics:')

for cluster in sorted(profile_df['cluster'].unique()):
    group = profile_df[profile_df['cluster'] == cluster]

    print(f'\nCluster {cluster}')
    print(f'Customers: {len(group):,}')
    print(f'Most Common Plan: {group["plan_type"].mode().iloc[0]}')
    print(f'Most Common Contract: {group["contract_type"].mode().iloc[0]}')
    print(f'Churn Rate: {group["churn"].mean() * 100:.2f}%')