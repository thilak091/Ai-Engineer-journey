import pandas as pd
students = {
    "Name":["THILAK","rahul","Priya","ARUN","kAvIn"],
    "Department":["AI","AI","IT","CSE","AI"],
    "CGPA":[8.98,9.1,8.4,7.5,6.9]
}
df=pd.DataFrame(students)

#Change every name to Title Case.
df['Name'] = df['Name'].apply(str.title)

#Rename Department → Dept
df.rename(columns={'Department': 'Dept'}, inplace=True)

#Increase every student's CGPA by 0.1
df['CGPA'] = df['CGPA'].apply(lambda x:x+0.1)

#Which student now has the highest CGPA?
print(df.loc[df['CGPA'].idxmax(),'Name'])

#Print the Updated DataFrame
print(df)