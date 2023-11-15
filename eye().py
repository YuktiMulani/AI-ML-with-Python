import numpy as np
# eye() function produces a unit matrix. It is n*n dimensional matrix whose main diagonal is ones and
#others are zero
x=np.eye(3)
print(x)
#[[1. 0. 0.]
#[0. 1. 0.]
#[0. 0. 1.]]
y=np.eye(3,2)
print(y)
#[[1. 0.]
#  [0. 1.]
#  [0. 0.]]
z=np.eye(3,2,dtype="bool")
print(z)
# [[ True False]
#  [False  True]
#  [False False]]