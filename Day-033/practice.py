from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn import metrics

df = pd.read_csv('decision_tree_2d_classification.csv', index_col='sample_id')
X = df.drop(columns=['target'])
y = df['target']

X_train , X_test , y_train , y_test =train_test_split(X , y , test_size = 0.3 , random_state = 1)
depths = range(1,11)
for depth in depths:
    dtc = DecisionTreeClassifier(max_depth = depth)
    dtc.fit(X_train , y_train)
    train_pred = dtc.predict(X_train)
    test_pred = dtc.predict(X_test)
    print('Depth :',depth)
    print(f'Training Accuracy : {metrics.accuracy_score(y_train , train_pred):.2f}%')
    print(f'Testing Accuracy : {metrics.accuracy_score(y_test , test_pred):.2f}%')
    scores = cross_val_score(dtc , X , y , cv = 5 , scoring = 'accuracy')
    print(f'5-Fold validation Accuracy: {scores.mean():.5f}%')
    print('------------------------------------------\n')

dtcg = DecisionTreeClassifier( criterion = 'gini' , random_state = 0)
scoresg = cross_val_score(dtcg , X , y , cv = 5 , scoring = 'accuracy')
print('Gini Decision Tree Accuracy:',scoresg.mean())
dtce = DecisionTreeClassifier( criterion = 'entropy' , random_state = 0)
scorese = cross_val_score(dtce , X , y , cv = 5 , scoring = 'accuracy')
print('Entropy Decision Tree Accuracy:',scorese.mean())

dtcg.fit(X_train , y_train)
labels = ['feature_1' , 'feature_2']
features = dtcg.feature_importances_
for i in [0,1]:
    print(f'{labels[i]} : {features[i]:.2f}')

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(
    n_estimators = 100 ,
    random_state = 42)
rfc.fit(X_train , y_train)
train_pred = rfc.predict(X_train)
print(f'Training Accuracy: {metrics.accuracy_score(y_train , train_pred)*100:.2f}')
y_proba = rfc.predict_proba(X_test)
print('Classification Report:')
print(metrics.classification_report(y_test , rfc.predict(X_test)))
scores = cross_val_score(rfc , X , y , cv = 5 , scoring = 'accuracy')
print('5-Fold Accuracy:',scores.mean())

