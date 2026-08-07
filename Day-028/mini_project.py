from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import numpy as np

iris=load_iris()
X=iris.data
y=iris.target

k_range = range(1,16)
accuracy = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn , X , y , 
                            cv=5 , scoring='accuracy')
    accuracy.append(score.mean())

best=np.argmax(accuracy)+1

#Best Model Summary
knn=KNeighborsClassifier(n_neighbors=best)
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.3)
knn.fit(X_train , y_train)
y_pred = knn.predict(X_test)
score = metrics.accuracy_score(y_test , y_pred)
precision , recall , f1 , support = metrics.precision_recall_fscore_support(
    y_test , y_pred
)

print('========= MODEL SUMMARY =========\n')
print('Model: KNN\n')
print(f'Best K: {best}\n')
print(f'Accuracy:{score*100:.2f}\n')#This is the accuracy in tts method, i cant find all the recall , precision and f1 in normal cvs method
print(f'Precision: {precision}\n')
print(f'Recall: {recall}\n')
print(f'F-1 Score: {f1}\n')
print(f'Support: {support}\n')
print('=================================')