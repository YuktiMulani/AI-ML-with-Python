import numpy as np
# numpy array is a data stsructure in python numpy library
# creating array without usinf numoy array
# numpy = numerical python
range(0,5)
list(range(0,5))#[0,1,2,3,4]
list(range(0,5,2))#[0,2,4]
list1=[1,3,5,7,9]
list2=[2,4,6,8,10]
# print(list1*list2)#TypeError: can't multiply sequence by non-int of type 'list'
new_list=[]
for i in range(0,len(list1)):
    new_list.append(list1[i]*list2[i])
print (new_list)
# using numpy
x=np.array([1,3,5,7,9])
y=np.array([2,4,6,8,10])
print(x*y)
# type of elements in an array
variable=[5.8,7,0,6] 
print(type(variable[0]))
new_variable=np.array([5.8,7,0,6])
print(new_variable)
print(type(new_variable[0]))