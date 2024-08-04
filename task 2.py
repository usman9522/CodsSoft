from random import *
x=[0]*10
s=0
for i in range (len(x)):
    x[i]=randint(1,100)
    print(x[i],end=' ')
    s=s+x[i]
print()
print(f'SUM OF ALL THE ELEMENTS OF THE ARRAY : {s}')
