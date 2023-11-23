import numpy as np
array=np.array([3,5,1,8,6,2,9])
print(np.sort(array))
array2=np.random.normal(30,10,(4,4))
print(np.sort(array2,axis=0))
print(np.sort(array2,axis=1))
