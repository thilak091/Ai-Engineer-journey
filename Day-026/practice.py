from sklearn.datasets import load_diabetes
import numpy as np
diabetes=load_diabetes()
X=diabetes.data
y=diabetes.target
print(X.size)
print(y.size)
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size=0.2 , random_state=42)

from sklearn.linear_model._base import LinearRegression 
linreg = LinearRegression()
linreg.fit(X_train , y_train)

y_pred = linreg.predict(X_test)
print('True value: ',y_test[:11])
print('Predicted value: ',y_pred[:11])

#Inspection
print(linreg.intercept_)
print(linreg.coef_)

#Evluation Metrics
from sklearn import metrics
mae=metrics.mean_absolute_error(y_test,y_pred)
mse=metrics.mean_squared_error(y_test,y_pred)
rmse=np.sqrt(metrics.mean_squared_error(y_test,y_pred))
print('Mean Absolute Error : ',mae) # 42 its differing by average 42
print('Mean Squared Error : ',mse) # it punishes for Huge Errors
print('Root Mean Squared Error : ',rmse) # INterpretable in target, like 53 off