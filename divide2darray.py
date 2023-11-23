import numpy as np
array= np.arange(20).reshape(5,4)
print(array)
print(np.split(array,[1,3]))
x,y,z=np.split(array,[1,3])
print(x)
print(y)
print(z)
print(np.split(array,[1,3],axis=1))
# hsplit-horizontal split
print(np.hsplit(array,4))
print(np.hsplit(array,[1,3]))
# vsplit-vertical split
print(np.vsplit(array,[1,3]))

