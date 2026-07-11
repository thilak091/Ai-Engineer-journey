import pandas as pd

students = {
    "Name":["Thilak","Rahul","Arun","Priya","Kavin","Divya","Rohan"],
    "Department":["AI","AI","CSE","IT","AI","CSE","IT"],
    "CGPA":[8.98,9.1,7.5,8.4,6.8,9.3,7.9],
    "Attendance":[91,96,75,88,72,94,81]
}

df = pd.DataFrame(students)
dept_group=df.groupby('Department')
#Print the average CGPA of every department.
print(dept_group['CGPA'].mean())

#Print the maximum attendance of every department.
print(dept_group['Attendance'].max())

#Count how many students each department has
print(dept_group['Name'].count())

#Find the department with the highest average attendance.
print(dept_group['Attendance'].mean().idxmax())

'''Use

agg()

to print

Average CGPA

Highest CGPA

Lowest CGPA

Student count

for every department.'''
print(dept_group['CGPA'].agg(['mean','max','min','count']))