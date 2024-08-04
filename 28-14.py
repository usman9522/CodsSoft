from random import*
a = [[randint(0,9) for i in range (10)]for j in range (10)]
for i in range (10):
    for j in range (10):
        print(a[i][j],end=' ')
    print()
for i in range (10):
    for j in range (10):
        if i == j:
            for k in range (i):
                print(' ',end='')
            print(a[i][j])
    
