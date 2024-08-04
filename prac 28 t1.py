from random import*
length=randint(5,10)
x=[0]*length
for i in range(length):
    x[i]=randint(1,100)
    print(f'{x[i]}',end=' ')
print()
for i in range(length-1,-1,-1):
    print(f'{x[i]}',end=' ')
