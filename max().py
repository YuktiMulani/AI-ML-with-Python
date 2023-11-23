import numpy as np
# max()-gives the largest element in the array
# argmax()-gives the index of the largest element
array =np.random.randint(10,50,10)
print(array)
print(array.max())
print(array.argmax())
array2=np.random.randint(0,50,(4,3))
print(array2)
print(array2.max())
print(array2.argmax())