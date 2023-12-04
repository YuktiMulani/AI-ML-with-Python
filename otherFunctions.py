import numpy as np
#===================================indexing==========================
array=np.arange(0,11)
print(array)
print(array[4])
print(array[-2])
#=============================indexing in 2d array====================
variable=np.array([[5,10,15],
                   [20,25,30],
                   [35,40,45]])
print(variable[0,0])
print(variable[2,1])
print(variable[-1,-3])
#===============================slicing==============================
example=np.arange(10,20)
print(example[2:6])
print(example[3::2])
print(example[:7:3])
#==============================slicing 2d array======================
print(variable[2,:])
print(variable[0,:])
print(variable[:,2])
print(variable[:,0])
print(variable[0:2,0:3])
print(variable[0::2,0::2])
#===================assigning value to 1d array=======================
array[4]=4
print (array)
array[0:5]=10
print(array)
array[5:]=20,30,40,50,60,70
print(array)
#===============assigning value to 2d array===========================
variable[1,1]=100
print(variable)
variable[1,0]=100.6#u can only assign int values to an int array if dont it will truncate the decimal and make it int in this case 100.6 will become 100
print(variable)
variable[:,2]=100
print(variable)
variable[0:3,0:3]=100
print(variable)
#=====================fancy indexing on 1d array==========================
indexes=[1,3,5]
print(array[indexes])
x=np.array([1,3,5])
print(array[x])
#======================fancy indexing for 2d array=======================
y=np.zeros((10,10),dtype='int')
row=y.shape[0]
for i in range(row):
    y[i]=i
print(y)
list1=[1,3,5,7]
print(y[list1])
list2=[8,5,2,7,3]
print(y[list2])
