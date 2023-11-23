import numpy as np
# reshape-change the dimensions of the array
array=np.arange(1,16) # this is a single dimensional array with values from 1 to 16
print(array)
print(array.reshape((3,5)))
print(array.reshape((1,15)))#this array contains 1 row and 15 columns
print(array.reshape((1,15)).ndim)#this array contains 1 row and 15 columns
print(array.ndim)
print(array.reshape((3,5)).ndim)
# you can only reshape an array whose number of elements fit the shape you are reshaping it into