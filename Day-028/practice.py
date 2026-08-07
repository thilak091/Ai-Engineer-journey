from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris=load_iris()
knn=KNeighborsClassifier(n_neighbors=10)
X=iris.data
y=iris.target
X1 , X2 , y1 , y2 = train_test_split(X , y ,
                    test_size=0.3 , random_state=2)
knn.fit(X1 , y1)
train_class = knn.predict(X1)
test_class = knn.predict(X2)

train_acc=metrics.accuracy_score(y1 , train_class)
test_acc=metrics.accuracy_score(y2 , test_class)
print(train_acc)
print(test_acc)

confusion =metrics.confusion_matrix(y2 , test_class)
print(confusion)
print('Correct Predictions: ',confusion[[0,1,2],[0,1,2]].sum())
#i can see that a species 1 have been misclassified as species 2

#Classification Report
precision , recall , f1 , support = metrics.precision_recall_fscore_support(
    y2 , test_class,average =None)
print('Recall: ',recall)
print('Precision: ',precision)
print('F-1 Score: ',f1)
print('Support: ',support)

#iam doing challenge 5 daily so im skipping

#
