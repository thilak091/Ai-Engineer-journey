import numpy as np

#Challenge 1- Create this array: 10 20 30 40 50 60 70 80 90 100
arr=np.linspace(10,110,10,endpoint=False,dtype='int16')
print(arr[0:5]) #First 5 Elements
print(arr[-3:]) #Last 3 Elements
print(arr[1::2]) #First 5 Elements

#Challenge 2:Create a 4×5 matrix.
arr1=np.random.randint(1,20,(4,5))
print(arr1)
print(arr1[1,::])#Second Row 
print(arr1[::,3])# 4th Column
print(arr1[3,0])#Bottom Left Value
print(arr1[1:-1,1:-1])#Middle Elements

#Challenge 3: Student Stats
scores = np.array([45,67,81,92,38,74,88,59,96,61])
print(np.where(scores>80)[0]+1) #RollNumbers of students whose score is above 80
print(np.where(scores<40)[0]+1) #RollNumbers of students who Failed
print(np.where((scores<=90) & (scores>=60))[0]+1) #RollNumbers of students who scored between 60 and 90

#Challenge 4: Matrix Problems
A = np.arange(1,10).reshape(3,3)
print(A.T) #Transpose MAatrix
print(A*2)# Multiply by 2
print(A+5) #Add 5
print(A**2) #Squaring Every Element


#Challenge 5: Considering rows as Months and columns as branches
sales = np.array([
    [1200,1500,1800],
    [1400,1600,2100],
    [1700,1900,2500]
])
print(sales.sum(axis=1))#Monthly Total
print(sales.sum(axis=0))#Branch Total
print(sales.max())#Total
print(np.unravel_index(sales.argmax(),(3,3)))# row and column Index of the highest element

