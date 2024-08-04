file=open('marks.txt','r')
file1=open('marks567.txt','w')
n=int(file.readline())
file1.write(f'{n}\n')
for i in range (n):
    a=int(file.readline())
    file1.write(f'{a}\n')
    for j in range (4):
        b=int(file.readline())
        if j<3:
            file1.write(f'{b} ')
        else:
            file1.write(f'{b}\n')        
file.close()
file1.close()
        
        
