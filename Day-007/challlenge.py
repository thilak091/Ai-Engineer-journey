import pandas as pd
#Create two DataFrames.
student_info = {
    "ID":[101,102,103],
    "Name":["Thilak","Rahul","Priya"]
}
df1=pd.DataFrame(student_info)

student_marks = {
    "ID":[101,102,103],
    "CGPA":[8.98,9.1,8.6]
}
df2=pd.DataFrame(student_marks)
#Merge them using ID.
merged_df = pd.merge(df1, df2, on="ID")

student_Att = {
    "ID":[101,102,103],
    'Attendance':[79.5,84.3,91.6]
}
df3=pd.DataFrame(student_Att)
three_way=pd.merge(merged_df,df3)

#Who has the highest CGPA?
print('Student with Highest CGPA:', three_way.loc[three_way['CGPA'].idxmax()])

#Who has the highest attendance?
print('Student with Highest Attendance:', three_way.loc[three_way['Attendance'].idxmax()])

#Average CGPA
print('The Average CGPA is:',three_way['CGPA'].mean())

#Average Attendance
print('The Average Attendance is:',three_way['Attendance'].mean())

#Print final merged DataFrame.
print(three_way)