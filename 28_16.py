from random import*
a = [[randint(0,9) for i in range (10)]for j in range (10)]
for i in range (10):
    for j in range (10):
        print(a[i][j],end=' ')
    print()
print()
for i in range (10):
    for j in range (10):
        if a[i][j] == 0:
            print(i,' ',j)
