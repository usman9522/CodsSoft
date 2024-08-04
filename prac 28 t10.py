from random import*
l1=[0]*10
for i in range(len(l1)):
    l1[i]=randint(3,7)
    print(l1[i],end=' ')
print()
for j in range(len(l1)):
    for k in range(l1[j]):
        print('*',end='')
    print()
