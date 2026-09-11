import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split , cross_val_score

print('==================================================')
print('             AI SPAM MESSAGE DETECTOR')
print('==================================================\n')

# 1.Load and Inspect the Data Set

df = pd.read_csv('text.csv')

print('Dataset Shape:', df.shape)

print('Class Distribution:')
print(df['label'].value_counts())

# 2.Prepare the Data

X = df['text']
y = df['label']

# 3.NLP Pipeline

tfid = TfidfVectorizer()
mnb = MultinomialNB()
pipe_mnb = make_pipeline(tfid,mnb)

# 4.Train Test Split Data

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2,random_state=5,stratify=y )

# 5.Pipe Line Evaluation

print('\n--------------------------------------------------')
print('             PIPE LINE EVALUATION')
print('--------------------------------------------------\n')

pipe_mnb.fit(X_train , y_train)

train_pred = pipe_mnb.predict(X_train)
test_pred = pipe_mnb.predict(X_test)

print(f'Training Accuracy: {metrics.accuracy_score(y_train , train_pred)*100:.2f}\n')
print(f'Testing Accuracy: {metrics.accuracy_score(y_test , test_pred)*100:.2f}\n')

scores = cross_val_score(pipe_mnb , X , y , cv=5 , scoring='accuracy')

print(f'Cross Val Score: {scores.mean()*100:.2f}\n')

print('Classification Report:\n' , metrics.classification_report(y_test , test_pred))

print('Confusion Matrix: ')
print(metrics.confusion_matrix(y_test , test_pred))

# 6.Model Comparison

print('\n--------------------------------------------------')
print('                 MODEL COPMPARISON')
print('--------------------------------------------------\n')

print('Multinomial Naive Bayes:\n')

print(f'Accuracy: {scores.mean()*100:.2f}\n')
print('Classification Report of Multinomial Naive Bayes:\n',
       metrics.classification_report(y_test , test_pred))

logreg = LogisticRegression()
pipe_logreg = make_pipeline(tfid , logreg)
scores = cross_val_score(pipe_logreg , X , y , cv=5 , scoring='accuracy')
pipe_logreg.fit(X_train , y_train)
test_pred = pipe_logreg.predict(X_test)

print(f'Logistic Regression: \n')
print(f'Accuracy: {scores.mean()*100:.2f}\n')
print('Classification Report of Logistic Regression:\n' , 
       metrics.classification_report(y_test , test_pred))

# 7.Custom Message Prediction

print('\n--------------------------------------------------')
print('              CUSTOM MESSAGE PREDICTION')
print('--------------------------------------------------\n')

str = input('Enter the Message to be Predicted:')

print(f'Message: {str}')

pred = pipe_mnb.predict([str])
print(f'Prediction: {pred[0].upper()}')
print(f'Confidence: {pipe_mnb.predict_proba([str])[0].max()*100:.2f}%')

