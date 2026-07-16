students = {
    "Name": [
        "Thilak","Rahul","Priya","Arun","Kavin",
        "Divya","Rohan","Sneha","Vignesh","Ananya",
        "Karthik","Meera"
    ],

    "Department": [
        "AI","AI","IT","CSE","AI",
        "IT","CSE","AI","IT","CSE",
        "AI","IT"
    ],

    "CGPA": [
        8.9,9.2,8.5,7.8,6.9,
        8.1,7.5,9.5,8.3,8.8,
        7.1,9.0
    ],

    "Attendance": [
        92,95,87,81,76,
        90,84,98,89,94,
        78,96
    ],

    "Placement": [
        "Yes","Yes","No","No","No",
        "Yes","No","Yes","Yes","Yes",
        "No","Yes"
    ],

    "Admission_Date": [
        "2024-06-15",
        "2024-06-17",
        "2024-07-02",
        "2024-06-20",
        "2024-07-05",
        "2024-06-18",
        "2024-07-08",
        "2024-06-25",
        "2024-07-10",
        "2024-06-14",
        "2024-07-01",
        "2024-06-28"
    ]
}

import pandas as pd

df = pd.DataFrame(students)

'''Create a pivot table showing:

Department
Average CGPA'''
pivot =pd.pivot_table(df,index="Department",values='CGPA',aggfunc='mean')
print(pivot)

'''Create another pivot table showing:

Department

Average Attendance

Maximum CGPA'''

pivot1 =pd.pivot_table(df,index="Department",values=['Attendance','CGPA'],aggfunc={'Attendance':'mean','CGPA':'max'})
print(pivot1)

'''Challenge 3

Convert Admission_Date into datetime.

Print:

Year
Month
Day Name

(Hint: Use .dt.)'''
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
print(df['Admission_Date'].dt.year)
print(df['Admission_Date'].dt.month_name())
print(df['Admission_Date'].dt.day_name())

'''Save the dataframe.

students.csv

Read it back.

Print:

Shape
First 5 rows
Data types'''
df.to_csv("students.csv", index=False)
df_read = pd.read_csv("students.csv")
print(df_read.shape)
print(df_read.head())
print(df_read.dtypes)