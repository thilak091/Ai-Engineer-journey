import numpy as np

#Challenge 1: Create an Array
arr=np.array([10,20,30,40,50])
print(arr)#printing Array
print(arr.dtype)#Printing type

#Challenge 2:Create a 3x3 Matrix of zeros
zeros=np.zeros((3,3),dtype='int16')
print(zeros)

#Challenge 3:Create 4x4 matrix of Ones
ones=np.ones((4,4),dtype='int16')
print(ones.shape) #shape(r,c)
print(ones.nbytes) #size in total bytes occupied
print(ones.ndim) #dimension

#Challenge 4: Create numbers from one to 20 
arr_20=np.arange(1,21,dtype='int16') #stop is exclusive
print(arr_20[1::2])# start index: till the end: step by 2

#Challenge 5: Create 10 equally spaced Numbers from 1 to 100
arr_100=np.linspace(0,100,num=10,endpoint=False,dtype='int16')#This Make the Most Sense
print(arr_100)