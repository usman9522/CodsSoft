from random import*
a = [0]*10
for i in range (len(a)):
    a[i] = randint(10,50)
print(a)
print()
for i in range (9,-1,-1):
    print(a[i],end='  ')
