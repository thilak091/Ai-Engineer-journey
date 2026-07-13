import pandas as pd
students = {
    "Name":["THILAK","rahul","Priya","ARUN","kAvIn"],
    "Department":["AI","AI","IT","CSE","AI"],
    "CGPA":[8.98,9.1,8.4,7.5,6.9]
}
df=pd.DataFrame(students)

#Print column names.
print(df.columns)

#Rename Department to Dept
df.rename(columns={"Department": "Dept"}, inplace=True)

#Convert every student name to uppercase.
df['Name'] = df['Name'].apply(str.upper)

#convert every student name to title case.
df['Name'] = df['Name'].apply(str.title)

'''Suppose Arun's CGPA was entered incorrectly.
Update it from
7.5
↓
8.1  using loc[].'''
filt = (df['Name']=='Arun')
df.loc[filt,'CGPA']= 8.1