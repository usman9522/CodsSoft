from random import*
length=5
x=[0]*length
y=[0]*length
for i in range(length):
    x[i]=randint(1,100)
    y[i]=randint(1,100)
for i in range(length-1):
    for j in range(length-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
        print(x[j],end=' ')
print()
for i in range(length-1):
    for j in range(length-1):
        if y[j]>y[j+1]:
            y[j],y[j+1]=y[j+1],y[j]
        print(y[i],end=' ')
