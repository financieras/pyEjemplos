l1=['a','b','c']
l2=l1
print("l1: ",l1)
print("l2: ",l2)
l1.append("x")
print("l1: ",l1)
print("l2: ",l2)
print('~'*40) ####################
l1=['a','b','c']
l2=l1[:]            #así se crea un nuevo objeto l2. También vale poner l2=list(l1)
print("l1: ",l1)
print("l2: ",l2)
l1.append("x")
print("l1: ",l1)
print("l2: ",l2)
print('~'*40) ####################
x=[[1,2],[3,4]]
y=x
print("x: ",x)
print("y: ",y)
x[0][0]=88
print("x: ",x)
print("y: ",y)
print('~'*40) ####################
from copy import deepcopy
x=[[1,2],[3,4]]
y=deepcopy(x)
print("x: ",x)
print("y: ",y)
x[0][0]=88
print("x: ",x)
print("y: ",y)