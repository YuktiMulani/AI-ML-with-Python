import numpy as np
x=np.random.rand(5)
print(x)
# [0.5267527  0.84445203 0.56929683 0.30101189 0.75045313]
y=np.random.rand(2,3)
print(y)
# [[0.82948945 0.85681386 0.5200418 ]
#  [0.83817136 0.66797351 0.87581926]]
z=np.random.randn(5)
print(z)
# [-0.71390515  1.14171402 -0.78259821 -0.134559   -1.43215669]
a=np.random.normal(20,5,(4,3))#20 is the mean, 5 is the standard deviation, 4,3 is the shape of the array. so this is a vector 
print(a)
# [[13.07531884 27.15265244 22.94361206]
#  [13.43866811 21.18890297 17.90447267]
#  [18.225509   23.2692641  17.41024897]
#  [27.66949407 22.23166089 19.40179512]]
b=np.random.randint(0,10,(4,4))
print(b)
# [[1 4 3 6]
#  [6 6 2 3]
#  [3 5 2 8]
#  [5 0 3 6]]