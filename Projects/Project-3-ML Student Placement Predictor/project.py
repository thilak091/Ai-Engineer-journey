from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer , make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score , train_test_split
from sklearn import metrics
import pandas as pd
import numpy as np

print('============================================================')
print('             AI STUDENT PLACEMENT PREDICTOR')
print('============================================================\n')
print('                   DATASET INFORMATION\n')

df = pd.read_csv('student_placement_dataset.csv')
# print(df.columns)

print(f'Total Students        :{df['student_id'].count()}')
print(f'Total Features        :{df.columns.size-2}')
print(f'Placed Students       :{(df['placement'] == 'Yes').sum()}')
print(f'Not Placed Students   :{(df['placement'] == 'No').sum()}\n')

print(f'Missing Values        :{df.isna().sum().sum()}')
print(f'Duplicate Rows        :{df.duplicated().sum()}\n')

print('------------------------------------------------------------')
print('                    MODEL PERFORMANCE')
print('------------------------------------------------------------\n')

numeric = ['cgpa','projects','python_score', 'aptitude_score', 'communication_score']
categorical = ['gender', 'department', 'internship',]
column_trans = ColumnTransformer([
    ('num' , StandardScaler() , numeric),
    ('cat' , OneHotEncoder(handle_unknown='ignore'),categorical)
])

logreg = LogisticRegression(max_iter=1000)

pipe = make_pipeline(column_trans,logreg)

X = df[['gender', 'department', 'internship', 'cgpa', 'projects',
       'python_score', 'aptitude_score', 'communication_score']]
y = df['placement'].map({'No':0 , 'Yes':1})

X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size=0.3 , random_state=2 , stratify=y
)
pipe.fit(X_train , y_train)
train_pred = pipe.predict(X_train)
test_pred = pipe.predict(X_test)


print('Model                  : Logistic Regression\n')
print(f'Training Accuracy      : {metrics.accuracy_score(y_train , train_pred):.2f}')
print(f'Testing Accuracy       : {metrics.accuracy_score(y_test , test_pred):.2f}\n')

scores = cross_val_score(pipe , X ,y,
                         cv=5 , scoring='accuracy')
print(f'5-Fold CV Accuracies   : {scores}')
print(f'Mean CV Accuracy       : {scores.mean():.2f}')

print('------------------------------------------------------------')
print('                 CLASSIFICATION EVALUATION')
print('------------------------------------------------------------\n')

precision , recall , f1 , support= metrics.precision_recall_fscore_support(
    y_test , test_pred
)
print(f'Precision              : {precision}')
print(f'Recall                 : {recall}')
print(f'F1 Score               : {f1}\n')

print('Classification Report: ')
print(metrics.classification_report(y_test , test_pred))

print('\n------------------------------------------------------------')
print('                    CONFUSION MATRIX')
print('------------------------------------------------------------\n')

print(metrics.confusion_matrix(y_test , test_pred))

print('\n------------------------------------------------------------')
print('                 CUSTOM STUDENT PREDICTION')
print('------------------------------------------------------------\n')

print('Student Profile: \n')

student_data = {
    "Gender": ["Male"],
    "Department": ["AI&DS"],
    "Internship": ["No"],
    "CGPA": [8.42],
    "Projects": [4],
    "Python Score": [86],
    "Aptitude Score": [78],
    "Communication Score": [82]
    
}

for key in student_data:
    print(f'{key} : {student_data[key][0]}')

print('\n------------------------------------------------------------\n')

df_new = pd.DataFrame(student_data)
df_new.columns = ['gender', 'department', 'internship', 'cgpa', 'projects',
       'python_score', 'aptitude_score', 'communication_score']

pipe.fit(X , y)
y_new = pipe.predict(df_new)

print(f'Prediction           : {'PLACEMENT LIKELY' if y_new[0] == 1 else 'NOT READY FOR PLACEMENT'}')
print(f'Probability of Placement : {pipe.predict_proba(df_new)[0][1]*100:.2f}% \n')

print('============================================================')

#Testing Code
# print(df['placement'].value_counts())
# print(df['placement'].value_counts(normalize=True))

# print(metrics.classification_report(
#     y_test,
#     test_pred,
#     target_names=['Not Placed', 'Placed']
# ))

# null_accuracy = y_test.value_counts(normalize=True).max()

# print(f'Null Accuracy: {null_accuracy*100:.2f}%')