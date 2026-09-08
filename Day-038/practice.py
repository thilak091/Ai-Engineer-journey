'''
Challenge 1
Problem	                Naive Bayes?	Reason
Spam Detection	             Yes	       Because words can be classified easily in naive bayes
House Price Prediction	     No            It is not easy to predict a value using probabilitical models like naive bayes
Disease Classification	     No	           Since it doesnot obey word orders , its riskier to use naive bayes
Document Classification	     Yes           Same Because it can easily find out words that belong to each category and use probability
Customer Segmentation	      Yes	       ex lets say we give what each customer buy , we can easily use porobability and segregate customers

'''

#Challenge 2
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd

df = pd.read_csv("2d.csv")

X = df[['feature_1','feature_2']]
y = df['target']

knn = KNeighborsClassifier()
dtc = DecisionTreeClassifier()
rfc = RandomForestClassifier()
gbc = GradientBoostingClassifier()
gnb = GaussianNB()
print('Model and their Accuracy')
i = 0
models = ["KNN" , "Decision Tree" , "Random Forest" , "Gradient Boosting" , "GaussianNB"]
for model in [knn , dtc , rfc , gbc , gnb]:
    scores = cross_val_score(model , X , y , cv = 5 , scoring = "accuracy")
    print(models[i] , scores.mean())
    i+=1

#Challenge 3
from sklearn.model_selection import train_test_split

#X_train , X_test , y_train , y_test = train_test_split(gnb , X , y , test_size = 0.3)
var_smoothing = [1e-11 , 1e-9 , 1e-7 , 1e-5 , 1e-3]
for v in var_smoothing:
    gnb = GaussianNB(var_smoothing = v)
    scores = cross_val_score(gnb , X , y , cv = 5 , scoring = 'accuracy')
    print('var smoothing:' , v , '== Accuracy:',scores.mean())
    
#Challenge 4
from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer()
texts = [
    "I love this movie",
    "This movie is amazing",
    "I hate this movie",
    "This movie is terrible",
    "Amazing acting and story",
    "Terrible acting and boring story"
]
matrix = count.fit_transform(texts)
arrm = matrix.toarray()
print(arrm)
print(arrm.shape)
print(count.vocabulary_)

#challenge 5
from sklearn.feature_extraction.text import TfidfVectorizer

tfid = TfidfVectorizer()
mat1 = tfid.fit_transform(texts)
arrm1 = mat1.toarray()
print(arrm1)
print(arrm)