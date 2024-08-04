from random import*
x = [0]*10
for i in range (len(x)):
    x[i] = randint(10,50)
print(x)
even = 0
odd = 0
a = []
b = []
for i in range (len(x)):
    if x[i]%2 == 0:
        even += 1
        a.append(x[i])
    else:
        odd +=1
        b.append(x[i])
print(even)
print(odd)


if even > odd:
    for i in range (len(b)):
        b[i] += 1
else:
    for i in range (len(a)):
        a[i] -= 1
print(a)
print(b)
z = a+b
for i in range (len(x)):
    print(z[i],end='  ')
