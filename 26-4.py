from random import*
x = [0]*8
print('List 1:',end=' ')
for i in range (len(x)):
    x[i] = randint(10,100)
    print(x[i],end=' ')
print()
sort = 0
for i in range (len(x)-1):
    if x[i] < x[i+1]:
        sort += 1
if sort == len(x)-1:
    print('List is Sorted')
else:
    print('List is not Sorted')
