from random import *
rows = 10
columns = 10
f = [[randint(0,9) for j in range(columns)] for i in range(rows)]
for row in f:
        for elements in row:
            print (elements, end = ' ')
        print ()
for j in range(len(f)):
    for k in range(len(f)):
        if f[j][k]==0:
            print(j, k)
