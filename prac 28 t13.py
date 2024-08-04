from random import*
l1=[0]*10
for i in range(len(l1)):
    l1[i]=randint(3,7)
    print(l1[i],end=' ')
print()
j=0
for j in range(len(l1)-2):
    for k in range(j,j+3):
        print(l1[k],end=' ')
    print()
    j+=1
