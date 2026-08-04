#Huge Import omg
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import numpy as np

#Creating Model
knn=KNeighborsClassifier(n_neighbors=11)#best k=11 for this

#Loading and Splitting
iris=load_iris()
X=iris.data
y=iris.target

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.3,random_state=4)

#Training and Finding General Accuracy
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)

Gen_acc=metrics.accuracy_score(y_test,y_pred)

#User Value Prediction
a=float(input('Enter Sepal Length(in Cm): '))
b=float(input('Enter Sepal Width(in Cm): '))
c=float(input('Enter Petal Length(in Cm): '))
d=float(input('Enter Petal Width(in Cm): '))

X_new=np.array([a,b,c,d])
y_user=knn.predict(X_new.reshape(1,-1))# it threw error and said to use reshape
print(f'Predicted Flower: {iris.target_names[y_user]}')

print(f'General Model Accuracy(%): {Gen_acc*100 :.2f}')
