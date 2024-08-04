from random import*
x = [0]*10
for i in range (len(x)):
    x[i] = randint(1,5)
print(x)
y = []
for element in x:
    if element not in y:
        y.append(element)
print(y)
for i in range (len(y)):
    print(f'{y[i]} = ',end='')
    for j in range (len(x)):
        if y[i] == x[j]:
            print(j,end=' ')
    print()
