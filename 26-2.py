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
        print(y[i],end=' ')
    else:
        print(x[i],end=' ')
