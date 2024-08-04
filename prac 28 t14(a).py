from random import *
rows = 10
columns = 10
f = [[randint(0,9) for j in range(columns)] for i in range(rows)]
for row in f:
        for elements in row:
            print (elements, end = ' ')
        print ()
v=0
for j in range(len(f)):
     for s in range(v):
         print(' ',end='')
     print(f[j][j])
     v+=1
