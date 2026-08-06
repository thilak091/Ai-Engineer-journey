from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
import pandas as pd

k_range= range(1,21)
param_grid=dict(n_neighbors=k_range)

iris=load_iris()
X=iris.data
y=iris.target

knn=KNeighborsClassifier()
grid=GridSearchCV(knn, param_grid , cv=5 , n_jobs=-1)

grid.fit(X,y)

print("The BEst K Value is:",grid.best_params_['n_neighbors'])

df=pd.DataFrame(grid.cv_results_)
index=df.index + 1
mean_scores = df['mean_test_score']

plt.style.use('fivethirtyeight')

plt.plot(index , mean_scores , linewidth=1.5 , marker='.' , color='tab:cyan')
plt.tight_layout()
plt.show()