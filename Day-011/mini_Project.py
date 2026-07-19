import numpy as np

marks = [91, 78, 88, 95, 67, 84, 73, 99, 81, 90]

arr=np.array(marks)

print('=====================================')
print('             NUMPY REPORT')
print('=====================================\n')

print(f'Marks: {arr}\n')

print(f'Highest Mark: {arr.max()}')
print(f'Lowest Mark: {arr.min()}')
print(f'Average Mark: {arr.mean()}')
print(f'Total Mark: {arr.sum()}')
print(f'Number of Students: {arr.size}\n')

print('=====================================')

