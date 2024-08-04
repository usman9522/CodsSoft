from random import*
x = [0]*12
for i in range (len(x)):
    x[i] = randint(1000,2000)
    print(x[i],end=' ')
print()
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
for i in range (len(x)):
    if i < 3:
        sum1 += x[i]
    if i >2 and i < 6:
        sum2 += x[i]
    if i >5 and i < 9:
        sum3 += x[i]
    if i >8 and i < 12:
        sum4 += x[i]
print()
print('Sales in Two Halves')
print()
print(f'Salea in First Half:  {sum1+sum2}')
print(f'Salea in Second Half:  {sum3+sum4}')
print()
print('Sales in Four Quarter')
print()
print(f'Salea in First Quarter:  {sum1}')
print(f'Salea in Second Quaretr:  {sum2}')
print(f'Salea in Third Quarter:  {sum3}')
print(f'Salea in Fourth Quarter:  {sum4}')
