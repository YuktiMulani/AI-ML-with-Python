import numpy as np
array=np.array([1,3,5,50,50,2,4,6])
print(np.split(array,[3,5]))#splitting the rray for frist 3 element and then untill 5th element spearate and the rest of the array separate
x,y,z=np.split(array,[3,5])
print(x)
print(y)
print(z)
print(np.split(array,4))#splitting the rray for frist 3 element and then untill 5th element spearate and the rest of the array separate
# you cannot divide an array containing 8 elements into 5 parts cause python cannot divide in eqaul parts