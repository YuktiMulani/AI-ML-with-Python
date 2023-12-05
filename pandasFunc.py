import numpy as np
import pandas as pd

# datafram with dictionary

df=np.random.randint(10,50,size=6)
print(df)
y=np.random.randint(10,50,size=6)
x=np.random.randint(10,50,size=6)
z=np.random.randint(10,50,size=6)

dic_e={"val1":df,"val2":x,"val3":y,"val4":z}
print(dic_e)

df1=pd.DataFrame(dic_e)
print(df1)

# series with a list
s=pd.Series([10,20,30,40,50])
print(s)
list_data=[2,4,6,8,10]
list_index=["a","b","c","d","e"]

variable=pd.Series(data=list_data,index=list_index,dtype="float")
print(variable)
print(type(variable))
# you cannot give more index than values in the series
# like above yo can create series with dictionary , numpy array as well


# indexing ans slicing series
ex=pd.Series(["+90","+49","+33","+39","+46","+47"],index=["Turkey","Germany","France","Italy","Sweden","Norway"])
print(ex)

# country code of germany
print(ex["Germany"])

print(ex["France":"Sweden"])
print(ex[2:5])
print(ex[2:5:2])
# special indexing
print(ex[["Norway","Turkey"]])

# features of a dataframe
print(df1)
print(df1.head()) #first 5 values default
print(df1.head(3)) 
print(df1.tail(3)) 
# column name and info
print(df1.columns)
print([i for i in df1.columns])
# change column names
df1.columns=["new1","new2","new3","new4"]
print(df1)
# value info
print(df1.values)
print(type(df1.values))
print(type(df1))
print(df1.shape)
print(df1.ndim)
print(df1.size)

# accessing processes of dataframes in pandas
np.random.seed(101)
df2=pd.DataFrame(data=np.random.randn(6,5),index="A B C D E F".split(),columns=["VAL1 VAL2 VAL3 VAL4 VAL5".split()])
print(df2)
print(df2["VAL1"])
print(df2.VAL1)
print(df2["VAL1"].values)
print(df2[["VAL1"]])
print(df2[["VAL1"]]["B":"D"])
print(df2[["VAL1"]][1:4])
# element selecgtion on multiple columns
print(df2[["VAL2","VAL5"]])
var=["VAL3","VAL4"]
print(df2[var])
print(df2["B":"D"])
print(df2[1:4])
print(df2["E":"E"])
print(df2["E":"E"][["VAL2","VAL5"]])

# loc and iloc
array=np.random.randint(10,50,(10,5))
df3=pd.DataFrame(data=array,index="A B C D E F G H I J".split(),columns="VAL1 VAL2 VAL3 VAL4 VAL5".split())

print(df3)
#  loc-used to select elemnets from the dataframe
# operates on index names as well
#  first and last elements are included
print(df3.loc["A":"D"])

# iloc
print(df3.iloc[0:4])
print(df3.loc["C","VAL4"])

print(df3.iloc[2,3])

print(df3.loc["C":"G","VAL3"])
print(df3.loc["C":"G",["VAL3"]])
print(df3.loc["C":"G"][["VAL3"]])

print(df3.iloc[2:7,2])
print(df3.iloc[2:7,[2]])
print(df3.iloc[2:7][["VAL3"]])

print(df3.loc["C":"H","VAL2":"VAL4"])

print(df3.iloc[2:8,1:4].loc["E":"F",["VAL3"]])

# conditional operations
print(df3>20)
print(df3[df3>20])
print(df3["VAL1"]>20)
print(df3[df3["VAL1"]<20])
print(df3[(df3["VAL1"]>20)&(df3["VAL4"]<18)])
print(df3[(df3<35)|(df3["VAL5"]>20)])

print(df3.loc[df3.VAL2>24,["VAL2","VAL3","VAL5"]])

# adding columns to a dataframe
a=np.arange(0,28).reshape(7,4)
df4=pd.DataFrame(data=a,columns=["VAL1","VAL2","VAL3","VAL4"])
df4["VAL1"]+df4["VAL2"] # u can use other matheematical operations as well to create a new column
df4["VAL5"]=df4["VAL1"]+df4["VAL2"]
print(df4)
np.arange(28,35)
df4["VAL6"]=np.arange(28,35)#u can also use a list to create values for a new  column
print(df4)
# u must provide the same number of elements as the no of rows  to create a new column

# Removing rows and columns
print(df4.drop(["VAL3","VAL4"],axis=1))# this does not affect the original structure
print(df4.drop(["VAL3","VAL4"],axis=1,inplace=True))# this will affect the original structure
print(df4)

# removing row elements
print(df4.drop([2,5],axis=0))#this is again temprary and will not affect the datastructure
print(df4.drop([2,5],axis=0, inplace=True))#this will
print(df4)
