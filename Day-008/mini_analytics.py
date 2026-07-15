import pandas as pd
df=pd.read_csv('student.csv')

#Beginner

#Display the first 5 rows.
print(df.head())
#Display the last 5 rows.
print(df.tail())
#Find the shape of the dataset.
print(df.shape)
#List all column names.
print(df.columns)
#Check data types.
print(df.dtypes)
#Find missing values.
print(df.isna().sum())


#Intermediate
groups=df.groupby('Department')

#Average CGPA by Department
print(groups['CGPA'].mean())
#Average Attendance by Department.
print(groups['Attendance'].mean())
#Highest CGPA in each Department.
print(groups['CGPA'].max())
#Lowest Attendance in each Department.
print(groups['Attendance'].min())
#Number of students in each Department.
print(groups['Name'].count())
#Count of Male and Female students.
print(df['Gender'].value_counts())
#Number of placed students.
print((df['Placement']=='Yes').sum())


#Filtering

#Students with CGPA > 9.
filt=df['CGPA']>9
print(df.loc[filt])
#Students with Attendance < 75.
filt=df['Attendance']<75
print(df.loc[filt])
#Students with CGPA > 8.5 and Attendance > 90.
filt=(df['CGPA']>8.5) & (df['Attendance']>90)
print(df.loc[filt])
#Students who are not placed.
filt=df['Placement']=='No'
print(df.loc[filt])
#AI department students with CGPA > 8
filt=(df['Department']=='AI') & (df['CGPA']>8)
print(df.loc[filt])

#Sorting

#Top 10 students by CGPA.
print(df.sort_values(by='CGPA',ascending=False).head(10))
#Bottom 5 students by Attendance.
print(df.sort_values(by='Attendance',ascending=False).tail(5))
#Sort by Department and then CGPA (descending).
print(df.sort_values(by=['Department','CGPA'],ascending=[True,False]))


#Advanced
#Placement percentage for each Department.
departments = df.groupby('Department')
for dept, dept_df in departments:
    percentage = ((dept_df["Placement"] == "Yes").sum() / dept_df["Placement"].count()) * 100
    print(dept, ":", percentage)

#Average CGPA of placed vs non-placed students.
Placed_grp=df.groupby('Placement')
print(Placed_grp['CGPA'].mean())

#Which Department has the highest average CGPA?
print(groups['CGPA'].mean().idxmax())

#Which Department has the best attendance?
print(groups['Attendance'].mean().idxmax())

#Risk Assessment
df['Risk']=''
for index, row in df.iterrows():
    if row['CGPA']<7.5 or row['Attendance']<75:
        df.loc[index, 'Risk'] = 'High'
    elif row['CGPA']>7.5 and row['CGPA']<8.5:
        df.loc[index, 'Risk'] = 'Medium'
    elif row['CGPA']>8.5 and row['Attendance']>85:
        df.loc[index, 'Risk'] = 'Low'

    
#Count the number of High, Medium, and Low risk students
print(df['Risk'].value_counts())