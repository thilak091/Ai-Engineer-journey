from sklearn.datasets import load_iris
import pandas as pd
iris = load_iris()

#Print the dataset keys.
print(iris.keys())

#Print Feature Names
print(iris.feature_names)

#Print Target Names
print(iris.target_names)

#Print Shape of Data
print(iris.data.shape)

#Print Target Shape
print(iris.target.shape)

#print First 10 Flowers
print(iris.data[:10])

#Convert this into dataframe
df=pd.DataFrame(iris.data,columns=iris.feature_names)

#Add Target Column as Target Species Names
df['species']=[iris.target_names[i] for i in iris.target]

#Details
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

#Count flowers
print(df['species'].value_counts())

#Save as CSV
df.to_csv('iris_set.csv',index=False)