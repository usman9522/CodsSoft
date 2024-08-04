from random import *
x=[]
while (len(x)<=20):
    a=randint(1,100)
    if a not in x:
        x.append(a)
print(x)
for i in range (len(x)-1):
    for j in range (len(x)-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print(x)
print('REMAINING ELEMENTS : ',end='')
for i in range (x[0],x[20]):
    if i not in x:
        print(i,end=' ')
