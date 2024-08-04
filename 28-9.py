from random import*
x = [0]*20
for i in range (len(x)):
    x[i] = randint(0,9)
    print(x[i],end=' ')
print()
for  i in range (len(x)):
    count = 0
    if i == 0 or i == 1 or i == (len(x)-1) or i == (len(x)-2):
        print(x[i],end=' ')
    else:
        a = x[i-1] + x[i-2] + x[i+1] + x[i+2]
        b = a//4
        print(b,end=' ')

