# multi dimensional array with concatenate function
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8])
print(np.concatenate([array1,array2]))
array3=np.arange(1,7).reshape(2,3)
array4=np.array([[7,8,9],[10,11,12]])
print(np.concatenate([array3,array4]))
print(np.concatenate([array3,array4],axis=1))
# you cannot concatenate 2 array of different dimensions 
