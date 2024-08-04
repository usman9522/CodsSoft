from random import *
x=[0]*10
for i in range (len(x)):
    x[i]=randint(0,100)
y=[x[i] for i in range (len(x))]
print('Original List (X) :',end=' ')
print(x)
print('Duplicate List (Y) :',end=' ')
print(y)
