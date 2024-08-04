from random import*
x = [randint(0,9) for i in range(20)]
print(x)
for i in range(16):
    avg = 0
    avg = (x[i] + x[i+1] + x[i+3] + x[i+4]) // 4
    x[i+2] = avg
print(x)
