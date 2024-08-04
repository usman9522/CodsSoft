from random import*
l1=[0]*10
for i in range(len(l1)):
    l1[i]=randint(3,7)
    print(l1[i],end=' ')
print()
i=1
for j in range(len(l1)):
    summ = 0
    for k in range(i):
        print(l1[k], end=' ')
        summ+=l1[k]
    print(f'= {summ}')
    i+=1
