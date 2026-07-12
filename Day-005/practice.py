import pandas as pd
import numpy as np
students = {
    "Name":["Thilak","Rahul","Arun","Priya","Kavin"],
    "CGPA":[8.98,None,7.5,9.2,None],
    "Attendance":[91,88,None,95,80]
}
df=pd.DataFrame(students)

#Find every missing value.
print(df.isna())

#Remove rows with missing values.
print(df.dropna())

#Replace missing CGPA with 0
df['CGPA'].fillna(0, inplace=True)
print(df)

#Replace missing Attendance with the average attendance.(You'll need to think a little.)
avg_att = df['Attendance'].mean()
df['Attendance'].fillna(avg_att, inplace=True)