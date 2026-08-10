import pandas as pd
df = pd.read_csv('student.csv')
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())
print(df['placement'].value_counts())
#Categorical - gender , department , internship , placement
#Numerical - everything except categorical 
#Target - Placement after encoded

df_new = pd.get_dummies(df , 
    columns = ['gender', 'department','internship','placement'])
#Easier to find categorical data by checking the header of the column instead of asking the
#attributes manually and searching for the data ourself
df_new.columns

X = df[['gender', 'department', 'cgpa', 'internship', 'projects',
       'python_score', 'aptitude_score', 'communication_score']]
y = df['placement'].map({'No': 0, 'Yes': 1})

from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

categorical_columns = [
    'gender',
    'department',
    'internship'
]

numerical_columns = [
    'cgpa',
    'projects',
    'python_score',
    'aptitude_score',
    'communication_score'
]

column_trans = ColumnTransformer([
    ('num', StandardScaler(), numerical_columns),
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
])

logreg = LogisticRegression(max_iter=1000)

pipe = make_pipeline(column_trans , logreg)

X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size = 0.375 , random_state = 1)

pipe.fit(X_train , y_train)

print(pipe.predict(X_test))
print(y_test)

#CrossVal Score
from sklearn.model_selection import cross_val_score
cvs = cross_val_score(pipe , X , y ,
                      cv = 5 , scoring = 'accuracy')
print(cvs)
print(cvs.mean())

new_student = pd.DataFrame({
    'gender': ['Male'],
    'department': ['AI&DS'],
    'internship': ['No'],
    'cgpa': [8.42],
    'projects': [4],
    'python_score': [86],
    'aptitude_score': [78],
    'communication_score': [82]
})
pred = pipe.predict(new_student)
probability = pipe.predict_proba(new_student)[0][1]#this is because it has probability of both 0 and 1 as an indivisual array sp we acces the first array 2nd column to get the probability of it being a 1
print(f'Placement Prediction: {'Yes' if pred[0]==1 else 'No'}')
print(f'Placement Probability: {probability*100:.2f}')