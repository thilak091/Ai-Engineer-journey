from sklearn.datasets import load_iris
iris=load_iris()
print(iris.data[0:11])
print(iris.feature_names)
print(iris.target_names)

#Normal TTS
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

X_train , X_test , y_train , y_test = train_test_split(
    iris.data , iris.target , test_size=0.3 , random_state=1)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train , y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred))

# 5-Fold CV
from sklearn.model_selection import cross_val_score
knn = KNeighborsClassifier(n_neighbors=5)
scores=cross_val_score(knn , iris.data , iris.target , 
                   cv=5 , scoring='accuracy')
scores.mean()

#For various k 
for k in range(1,12,2):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn, iris.data , iris.target , 
                   cv=5 , scoring='accuracy')
    print(f'k={k}-> {scores.mean()*100:.2f}')

#Best k value
import numpy as np
score=[]
for k in range(1,31):
    knn = KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(knn, iris.data , iris.target , 
                   cv=5 , scoring='accuracy')
    score.append(scores.mean())
best=np.argmax(score)
print('Best K:',best+1)
print('Best Accuracy:',score[best])

