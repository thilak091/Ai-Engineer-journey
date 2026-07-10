#Day3 of becoming an AI Engineer!
import pandas as pd

students = {
    "Name":["Thilak","Rahul","Arun","Priya","Kavin","Divya","Rohan"],
    "Department":["AI","AI","CSE","IT","AI","CSE","IT"],
    "CGPA":[8.98,9.1,7.5,8.4,6.8,9.3,7.9],
    "Attendance":[91,96,75,88,72,94,81]
}

df = pd.DataFrame(students)

#describe()
print(df.describe())

#Print Unique departments.
print(df["Department"].unique())

#Print Number of unique departments.
print(df["Department"].nunique())

#Which attendance percentage appears most often?
print(df['Attendance'].value_counts())

#Find Which department has the highest average CGPA?
print(df[["Department","CGPA"]].describe())#tried