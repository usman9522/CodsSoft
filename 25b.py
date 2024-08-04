from random import*
x=[7]*30
count=0
count_n=0
for i in range (len(x)):
    x[i]=randint(1,100)
    print(x[i],end=' ')
    if x[i]>=50:
        count=count+1
        count_n=count_n+x[i]
ave=count_n/count
print()
print('Average: ',ave)
for i in range (len(x)):
    if x[i]<50:
        print(x[i],end=' ')
print()
for i in range (len(x)):
    if x[i]<ave:
        print(x[i],end=' ')
print()
for i in range (len(x)):
    if x[i]>ave:
        print(x[i],end=' ')
print()
