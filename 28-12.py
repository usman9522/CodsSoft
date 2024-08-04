from random import*
x = [0]*10
for i in range (len(x)):
    x[i] = randint(3,7)
    print(x[i],end=' ')
print()
a = 1
for i in range (len(x)):
    count = 0
    for j in range (a):
        print(x[j],end=' ')
        count += x[j]
    print(f'= {count}')
    print()
    a += 1
