from sklearn.ensemble import GradientBoostingClassifier , RandomForestClassifier
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn import metrics
import pandas as pd

df = pd.read_csv('2d.csv')
X = df[['feature_1' , 'feature_2']]
y = df['target'] 

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.5 , random_state = 2)

gbc = GradientBoostingClassifier()
gbc.fit(X_train , y_train)

train_pred = gbc.predict(X_train)
test_pred = gbc.predict(X_test)
print('Train predictions:',metrics.accuracy_score(y_train , train_pred))
print('Test predictions:',metrics.accuracy_score(y_test , test_pred))
scores = cross_val_score( gbc , X , y , cv=5 , scoring = 'accuracy' )
print('5-Fold Cross validation Scores:',scores.mean())
print('Classification Report:')
print(metrics.classification_report(y_test , test_pred))


n_values = [10 , 25 , 50 , 100 , 200]
for n in n_values:
    gbc1 = GradientBoostingClassifier(n_estimators = n)
    gbc1.fit(X_train , y_train)

    train_pred = gbc1.predict(X_train)
    test_pred = gbc1.predict(X_test)
    print('For n_estimators =',n)
    print('Train predictions:',metrics.accuracy_score(y_train , train_pred))
    print('Test predictions:',metrics.accuracy_score(y_test , test_pred))
    scores = cross_val_score( gbc1 , X , y , cv=5 , scoring = 'accuracy' )
    print('5-Fold Cross validation Scores:',scores.mean())
    print('-----------------------------------------\n')

learning = [0.01 , 0.05 , 0.1 , 0.2 , 0.5]
for l in learning:
    gbc1 = GradientBoostingClassifier(learning_rate = l)
    scores = cross_val_score( gbc1 , X , y , cv=5 , scoring = 'accuracy' )
    print('For Learning_Rate =',l)
    print('5-Fold Cross validation Scores:',scores.mean())
    print('-----------------------------------------\n')
# for me 0.1 and 0.2 are really good 

rfc = RandomForestClassifier()
gbc = GradientBoostingClassifier()

rfc.fit(X_train , y_train)
gbc.fit(X_train , y_train)

rfc_pred = rfc.predict(X_test)
gbc_pred = gbc.predict(X_test)

print('Model: Random Forest Classsifier')
print('Test Accuracy:',metrics.accuracy_score(y_test , rfc_pred))
rscores = cross_val_score(rfc , X , y , cv =5 , scoring = 'accuracy' )
print('5-Fold Validation Accuracy:',rscores.mean())
print('Classification Report: ')
print(metrics.classification_report(y_test , rfc_pred))
print('-------------------------------------------------')

print('Model: Gradient Boosting Classifier')
print('Test Accuracy:',metrics.accuracy_score(y_test , gbc_pred))
gscores = cross_val_score(gbc , X , y , cv =5 , scoring = 'accuracy' )
print('5-Fold Validation Accuracy:',gscores.mean())
print('Classification Report: ')
print(metrics.classification_report(y_test , gbc_pred))
print('-------------------------------------------------')

