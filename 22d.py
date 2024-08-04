from random import*
file=open('task4.txt','w')
row=randint(4,8)
col=randint(4,8)
file.write(f'{row}\n{col}\n')
for i in range (row):
    for j in range (col):
        n=randint(1,9)
        file.write(f'{n}\n')
file.close()
            
