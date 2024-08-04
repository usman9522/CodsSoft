from random import*
file1 = open('taskonea.txt' , 'w')
file2 = open('taskoneb.txt' , 'w')
n = 10
file1.write(f'{n}\n')
file2.write(f'{n}\n')
for i in range (n):
    rows = randint(2,6)
    coloumns = randint(2,6)
    file1.write(f'{rows}\n')
    file1.write(f'{coloumns}\n')
    file2.write(f'{rows}\n')
    file2.write(f'{coloumns}\n')
    for j in range (rows*coloumns):
        u = randint(0,9)
        file1.write(f'{u}\n')
    for j in range (rows*coloumns):
        u = randint(0,9)
        file2.write(f'{u}\n')
file1.close()
file2.close()
