from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import pandas as pd

dia=load_diabetes()
X_train , X_test , y_train , y_test = train_test_split(
    dia.data , dia.target , test_size=0.3 , random_state=42
)

linreg = LinearRegression()
linreg.fit(X_train,y_train)

y_pred=linreg.predict(X_test)

mae=metrics.mean_absolute_error(y_test,y_pred)
mse=metrics.mean_squared_error(y_test,y_pred)
rmse=np.sqrt(metrics.mean_squared_error(y_test,y_pred))

#Printing Metris
print('Linear Regression Intercept =',linreg.intercept_)
print('Linear Regression Coefficient: ',linreg.coef_)
print('Mean Absolute Error : ',mae)
print('Mean Squared Error : ',mse)
print('Root Mean Squared Error : ',rmse)
data=np.hstack([y_test.reshape(133,1),y_pred.reshape(133,1)])

#Printing first 10 vlaues of prediction in table
df=pd.DataFrame(data,columns=['True Value','Predicted Value'])
print(df.head(10))