import pandas as pd

students = {
    "Name":["Thilak","Rahul","Arun","Priya","Kavin","Divya","Rohan"],
    "Department":["AI","AI","CSE","IT","AI","CSE","IT"],
    "CGPA":[8.98,9.1,7.5,8.4,6.8,9.3,7.9],
    "Attendance":[91,96,75,88,72,94,81]
}

df = pd.DataFrame(students)
dept_group=df.groupby('Department')


print("============================\n STUDENT PERFORMANCE REPORT \n ============================")
print("\ntotal Students:",df['Name'].count())
print('\nDepartments:',df['Department'].nunique())
print('\nHighest CGPA:',df['CGPA'].max())
print('\nLowest CGPA:',df['CGPA'].min())
print('\nAverage Attendance:',df['Attendance'].mean())

print('\n----------------------------\n')
print('Department Statistics')
print('\n\nAI')
print('\nAverage CGPA:',dept_group.get_group('AI')['CGPA'].mean())
print('\nHighest Attendance:',dept_group.get_group('AI')['Attendance'].max())
print('\nStudents:',dept_group.get_group('AI')['Name'].count())

print('\n\nCSE')
print('\nAverage CGPA:',dept_group.get_group('CSE')['CGPA'].mean())
print('\nHighest Attendance:',dept_group.get_group('CSE')['Attendance'].max())
print('\nStudents:',dept_group.get_group('CSE')['Name'].count())

print('\n\nIT')
print('\nAverage CGPA:',dept_group.get_group('IT')['CGPA'].mean())
print('\nHighest Attendance:',dept_group.get_group('IT')['Attendance'].max())
print('\nStudents:',dept_group.get_group('IT')['Name'].count())

print('\n----------------------------\n')
print('\nTop Performer')
print('Name:',df.loc[df['CGPA'].idxmax(), 'Name'])
print('CGPA:',df.loc[df['CGPA'].idxmax(), 'CGPA'])
print('Department:',df.loc[df['CGPA'].idxmax(), 'Department'])