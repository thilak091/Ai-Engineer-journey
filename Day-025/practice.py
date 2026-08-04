from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
y=iris.target

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
knn=KNeighborsClassifier(n_neighbors=5)

#Training Model
X_train , X_test, y_train , y_test = train_test_split(X,y,test_size=0.03,random_state=4)
knn.fit(X_train,y_train)
#Splitting 145:5 models for Train:test

#Testing 5 Sample Data
y_pred=knn.predict(X_test)
print(y_pred)
y_names=[]
import numpy as np
for i in np.nditer(y_pred):
    y_names.append(iris.target_names[i])
print(y_names)

#Printing 5 Model Accuracy
from sklearn import metrics
print('Accuracy of model built from Training 145 observations and\n testing with 5 samples is',end=' ')
print(metrics.accuracy_score(y_test,y_pred)*100)