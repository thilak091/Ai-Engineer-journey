import pandas as pd
pd.set_option('display.max_columns', None)

#Section 1:Heading
print('====================================================')
print('          AI COLLEGE ANALYTICS DASHBOARD')
print('====================================================\n')

#Section 2:Dataset Information

df=pd.read_csv('student.csv')
print('Dataset Loaded Successfully')

print(f'Rows: {df.shape[0]}')#rows
print(f'Columns: {df.shape[1]}\n')#columns

print(f'Departments: {df["Department"].nunique()}\n')#departments

#Section 3:Overall Statistics
print('====================================================')
print('                 OVERALL STATISTICS')
print('====================================================\n')

print(f'Total Students: {df["ID"].nunique()}')#total students counted with unique student id
print(f'Average CGPA: {df["CGPA"].mean():.2f}')#average cgpa with 2 decimals
print(f'Average Attendance: {df["Attendance"].mean():.2f}%')#average attendance with 2 decimals
placed=df['Placement']=='Yes' # filtering yes to do .sum()
placed_percent=(placed.sum()/df['ID'].nunique())*100 #finding percent
print(f'Placement Percentage: {placed_percent:.2f}%')#placement percentage with 2 decimals
print(f'Highest CGPA: {df["CGPA"].max():.2f}')#highest cgpa with 2 decimals
print(f'Lowest CGPA: {df["CGPA"].min():.2f}\n')#lowest cgpa with 2 decimals

#Section 4:Departmental Statistics
print('====================================================')
print('               DEPARTMENTAL STATISTICS')
print('====================================================\n')

groups=df.groupby('Department')#grouping by department
i=1 #im cooking...
for dept, dept_df in groups: #iterating through groups
    print(f'{i}.{dept} Department:')#mentioning Department name with number
    print(f'Average CGPA: {dept_df["CGPA"].mean():.2f}')# Average CGPA with 2 decimals
    print(f'Average Attendance: {dept_df["Attendance"].mean():.2f}%')# Average Attendance with 2 decimals
    print(f'Highest CGPA: {dept_df["CGPA"].max():.2f}')# Highest CGPA with 2 decimals
    print(f'Student Count: {dept_df["ID"].nunique()}\n')# Student Count
    print('---------------------------------------------------\n')#seperating each department with line(cooking with Seperators)
    i += 1

#Section 5:Top Performer
print('====================================================')
print('                    TOP PERFORMER')
print('====================================================\n')

top_perf=df['CGPA'].idxmax() # top performer is max cgpa 

print(f'Name: {df.loc[top_perf,"Name"]}')#name of top performer
print(f'Department: {df.loc[top_perf,"Department"]}')#Department of top performer
print(f'CGPA: {df.loc[top_perf,"CGPA"]:.2f}')#CGPA of top performer with 2 decimals
print(f'Attendance: {df.loc[top_perf,"Attendance"]:.2f}%\n')#Attendance of top performer with 2 decimals


#Section 6:Placemnt Analysis
print('====================================================')
print('                   PLACEMENT ANALYSIS')
print('====================================================\n')

print(f'Placed Students: {placed.sum()}') #Placed students using sum to count true
print(f'Non Placed Students: {df["ID"].nunique()-placed.sum()}') #Non Placed students using total - sum
print(f'Placement Percent:{placed_percent:.2f}%')# Placement Percent calculated
print('Department Wise Placement Percent:') 
i=1
for dept, dept_df in groups: #iterating through groups
    dept_placed=(dept_df['Placement']=='Yes').sum() #calculating placed Students
    dept_total=dept_df["ID"].nunique()#Calculating total students
    plaaced_percent=(dept_placed/dept_total)*100 #calculating placed Percent
    print(f'{i}.{dept}: {plaaced_percent:.2f}%')#displaying placed Percent
    i+=1

#Section 7:Risk Assesment
print('\n====================================================')
print('                      RISK ASSESMENT')
print('====================================================\n')

df['Risk']=''#creating Risk Column
for index, row in df.iterrows():#iterating through rows

    if row['CGPA'] < 7.0 or row['Attendance'] < 75:#High Risk
        risk = "High"

    elif row['CGPA'] >= 8.5 and row['Attendance'] >= 90:#Medium Risk
        risk = "Low"

    else:#Low Risk
        risk = "Medium"

    df.loc[index, 'Risk'] = risk #assigning Risks
# Displaying 
print(f'High Risk Students:{(df['Risk']=='High').sum()}')
print(f'Medium Risk Students:{(df['Risk']=='Medium').sum()}')
print(f'Low Risk Students:{(df['Risk']=='Low').sum()}\n')

#Section 8: Top 3 Students Sorted by CGPA
print('====================================================')
print('                TOP 3 STUDENTS BY CGPA')
print('====================================================\n')

top_3=df.sort_values(by='CGPA',ascending=False).head(3)# sorting top  3
print(top_3,'\n')

#Section 9: Admission Analysis
print('====================================================')
print('                  ADMISSION ANALYSIS')
print('====================================================\n')


df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
print(f'Students admitted in June: {(df['Admission_Date'].dt.month_name()=='June').sum()}')#print counting june filter
print(f'Students admitted in July: {(df['Admission_Date'].dt.month_name()=='July').sum()}')#print counting july filter
print('Admissions by Month:')
print(df['Admission_Date'].dt.month_name().value_counts(),'\n')# admission by mont if admitted at different dates

#Section 10: Ending
print('====================================================')
print('              REPORT GENERATED SUCCESSFULLY')
print('====================================================\n')

#Bonus 2: Grade Calculation
df['Grade']=''#creating Grade Column
for index, row in df.iterrows():#iterating through rows

    if row['CGPA'] > 9:#A
        Grade ='A'

    elif row['CGPA'] > 8:#B
        Grade = 'B'

    elif row['CGPA'] > 7:#C
        Grade = 'C'

    elif row['CGPA'] > 6:#D
        Grade = 'D'

    elif row['CGPA'] > 5:#E
        Grade = 'E'

    elif row['CGPA'] <5 and row['CGPA'] >0:#U or Fail Grade
        Grade = 'U'

    else: # giving Nan Value for invalid Cases
        Grade = None

    df.loc[index, 'Grade'] = Grade #assigning Grade

df.to_csv('Final.csv',index=False)













