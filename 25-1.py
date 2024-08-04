from random import*
x = [0]*10
sum = 0
print(f'Length: {len(x)}')
for i in range (len(x)):
    x[i] = randint(1,100)
    sum += x[i]
    print(x[i],end=' ')
ave = sum//len(x)
print()
print(f'Average: {ave}')
pos = 0
neg = 0
for i in range (len(x)):
    a = ave - x[i]
    print(a,end=' ')
    if a<0:
        neg += 1
    else:
        pos += 1
print()
print(f'Number of Positive: {pos}')
print(f'Number of Negtive: {neg}')
