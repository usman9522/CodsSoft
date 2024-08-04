from random import*
x=[0]*10
for i in range(10):
    x[i]=randint(1,100)
    print(x[i],end=' ')
print()
even=0
odd=0
print('even=',end=' ')
for i in range(10):
    if x[i]%2==0:
        print(x[i],end=' ')
        even+=1
print()
print('odd=',end=' ')
for i in range(10):
    if x[i]%2!=0:
        print(x[i],end=' ')
        odd+=1
for i in range(10):
    if even>odd:
        if x[i]%2!=0:
            x[i]+=1
    else:
        if x[i]%2==0:
            x[i]-=1
print(x)
