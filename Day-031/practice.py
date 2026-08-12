from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

df=pd.read_csv('decision_tree_2d_classification.csv')
tree = DecisionTreeClassifier(random_state=42)
X = df[['feature_1' , 'feature_2']]
y = df['target']
X_train , X_test , y_train , y_test = train_test_split(X , y ,
                test_size = 0.3 )
tree.fit(X_train , y_train)
y_pred = tree.predict(X_test)
print(metrics.accuracy_score(y_test , y_pred))
print(metrics.confusion_matrix(y_test , y_pred))

depths = range(1,15)
for depth in depths: 
    tree=DecisionTreeClassifier(max_depth = depth)
    tree.fit(X_train , y_train)
    
    print(f'Depth = {depth}')
    y_pred = tree.predict(X_train)
    print(f'Training Accuracy = {metrics.accuracy_score(y_train , y_pred)*100:.2f}')
    y_pred1 = tree.predict(X_test)
    print(f'Testing Accuracy = {metrics.accuracy_score(y_test , y_pred1)*100:.2f}')