import numpy as np

#Section-1 Heading
print('=========================================')
print('          STUDENT MARKS ANALYZER')
print('=========================================\n')

#Section-2 DataSet Information
marks = np.array([91, 78, 88, 95, 67, 84, 73, 99, 81, 90])
print('Marks Loaded Successfully')
print(f'Total Students: {marks.size}\n')
print('-----------------------------------------\n')

#Section-3 Overall Statistics
print(f'Highest Marks: {marks.max()}\n')
print(f'Lowest Marks: {marks.min()}\n')
print(f'Average Marks: {marks.mean()}\n')
print(f'Total Marks: {marks.sum()}\n')
print('-----------------------------------------\n')

#Section-4 Above average Students

print(f'students Above Average: {marks[marks > marks.mean()].size}\n')
print('-----------------------------------------\n')

#Section-5 Top Performer
print('-TOP PERFORMER-\n')
print(f'Roll No: {np.argmax(marks)+1}')
print(f'Marks: {marks.max()}\n')
print('-----------------------------------------\n')

#Section 6 — Grade Distribution
print('Grade Distribution\n')
grades=[]
for mark in marks:
    if mark >= 90:
        grades.append('A')
    elif mark >= 80:
        grades.append('B')
    elif mark >= 70:
        grades.append('C')
    elif mark < 70:
        grades.append('D')
    else:
        grades.append(None)




unique , counts =np.unique(grades,return_counts=True)
for grade,count in zip(unique,counts):
    print(f'{grade}: {count}')
print('\n-----------------------------------------\n')

#Section-7 Grace Marks

print('After Grace Marks\n')
new_marks = marks + 5
print(f'New Average: {marks.mean()}')
print(f'New High Marks: {marks.max()}\n')

print('=========================================')
print('      Report generated Successfully')
print('=========================================\n')