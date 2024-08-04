from random import*
a = [[randint(10,99) for i in range (3)]for j in range (4)]
print(a)
for i in range (4):
    for j in range (3):
        print(a[i][j],end=' ')
print()
for i in range (4):
    count = 0
    for j in range (3):
        print(a[i][j],end=' ')
        count += a[i][j]
    print('=',count)
