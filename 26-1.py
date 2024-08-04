from random import*
x = [0]*8
for i in range (len(x)):
    x[i] = randint(10,100)
    print(x[i],end=' ')
print()
for i in range (len(x)-1):
    if x[i] < x[i+1]:
        print(f'{x[i]},{x[i+1]}')
    
