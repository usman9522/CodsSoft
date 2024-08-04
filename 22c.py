from random import*
file=open('task3.txt','w')
file.write('5\n')
for i in range (5):
    n=randint(7,10)
    file.write(f'{n}\n')
    for j in range (n):
        a=randint(1,100)
        file.write(f'{a}\n')
file.close()
