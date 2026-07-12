import pandas as pd
import numpy as np
students = {
    "Name":["Thilak","Rahul","Arun","Priya","Kavin"],
    "CGPA":[8.98,None,7.5,9.2,None],
    "Attendance":[91,88,None,95,80]
}
df=pd.DataFrame(students)

print("========== DATA CLEANING REPORT ==========\n")
print('Rows Before Cleaning :')
print(df)
print('\n Missing CGPA:')
print(df['CGPA'].isna())

print('\n Missing Attendance :')
print(df['Attendance'].isna())

print('\n Rows After Cleaning :')
df.dropna(inplace=True)
print(df)

print('\n Average CGPA :')
print(df['CGPA'].mean())

print('\n Average Attendance :')
print(df['Attendance'].mean())

print('\nCleaning Completed Successfully')
print('==========================================')