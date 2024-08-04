from random import*
x=[]
while len(x)<=10:
    a=randint(1,15)
    if a not in x:
        x.append(a)
print(x)
        
