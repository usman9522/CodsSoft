from random import*
x = [0]*8
print('List 1:',end=' ')
for i in range (len(x)):
    x[i] = randint(10,100)
    print(x[i],end=' ')
print()
y = [0]*8
print('List 2:',end=' ')
for i in range (len(y)):
    y[i] = randint(10,100)
    print(y[i],end=' ')
print()
for i in range (len(x)):
    if x[i] < y[i]:
        x[i] , y[i] = x[i] , y[i]
    if x[i] > y[i]:
        x[i] , y[i] = y[i] , x[i]
print('Smaller:',end='') 
for i in range (len(x)):
    print(x[i],end=' ')
print()
print('Larger:',end='')
for i in range (len(y)):
    print(y[i],end=' ')
print()
