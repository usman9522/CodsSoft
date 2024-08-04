from random import*
x = [0]*30
pas = 0
fail = 0
sum = 0
y = []
for i in range (len(x)):
    x[i] = randint(1,100)
    print(x[i],end=' ')
    if x[i] > 49:
        pas += 1
        sum += x[i]
    else:
        fail += 1
        y.append(x[i])
ave = sum//pas
print()
print(f'Average: {ave}')
print('Fail Students:')
for i in range (len(y)):
    print(y[i],end=' ')
m = []
n = []
print()
for i in range (len(x)):
    if x[i] > ave:
        m.append(x[i])
    else:
        n.append(x[i])
print('Below Average Students:')
for i in range (len(n)):
    print(n[i],end=' ')
print()
print('Above Average Students:')
for i in range (len(m)):
    print(m[i],end=' ')
    
        
