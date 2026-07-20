import numpy as np

#Challenge 1: create an Array
arr=np.array([10, 20, 30 ,40 ,50 ,60])

print(arr[0]) #First Element
print(arr[-1]) #Last Element
print(arr[[2,3]]) #Middle 2 Elements

# Challenge 2: Create a 3,3 Array
arr1=np.linspace(10,90,num=9,endpoint=True,dtype='int32').reshape(3,3)
print(arr1[1, : ]) #Entire Second Row
print(arr1[ : ,2]) #Entire 3rd Column
print(arr1[2,2]) #Bottom Right Value

#Challenge 3: Boolean Masking
arr1 = np.arange(1, 11)
print(arr1[arr1%2==0]) #Only Even Numbers
print(arr1[arr1>5]) #Numbers Greater Than 5
print(arr1[arr1%3==0]) #Numbers Divisible by 3

#Challenge 4: BroadCasting
marks = np.array([78,85,91,67,88])
marks +=5
print('Updated Array: ',marks)
print('Average: ',marks.mean())
print('Marks: ',np.max(marks))

#Challenge 5: Statistics
sales = np.array([1200,1500,1800,2200,2000])
print('Total Sales: ',sales.sum()) #Total
print('Average Sales: ',sales.mean()) #Mean
print('Highest: ',sales.max()) #High
print('lowest Sales: ',sales.min()) #Low

new_Sales=sales*1.1 # adding 10 percent( i cant find the most numpy ans)
print('Updated Sales: ',new_Sales.astype('int32')) # converting to int to look pretty

