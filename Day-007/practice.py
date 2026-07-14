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
merged_df = pd.merge(df1, df2, on="ID")#on is used to indicate the column to merge on.
print(merged_df)

#Add one more student only to student_info. Observe what changes
student_info = {
    "ID":[101,102,103,104],
    "Name":["Thilak","Rahul","Priya",'Vinay']
}
df1=pd.DataFrame(student_info)
merged_df=pd.merge(df1,df2)
print(merged_df)

#inner and outer join
inner_join = pd.merge(df1, df2, on="ID", how="inner")
print(inner_join)
outer_join = pd.merge(df1, df2, on="ID", how="outer")
print(outer_join)

#Create another DataFrame Attendance Merge all three.
student_Att = {
    "ID":[101,102,103,104],
    'Attendance':[79.5,84.3,91.6,86.5]
}
df3=pd.DataFrame(student_Att)
three_way=pd.merge(merged_df,df3)
print(three_way)
