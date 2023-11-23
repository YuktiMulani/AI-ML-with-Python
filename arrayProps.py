import numpy as np
# ndim-gives the number of dimensions
# shape-gives us the size of the info of the array
# size-total number of elements
# dtype-return the data type

matrix=np.random.randint(10,50,(5,4))
print(matrix)
print(matrix.ndim)
print(matrix.shape)
print(matrix.size)
print(matrix.dtype)


