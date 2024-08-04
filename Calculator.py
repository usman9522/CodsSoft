print('Basic Calculator to perform Arithmetic Operations')
print()
print('For addition: Enter 1')
print('For subtraction: Enter 2')
print('For multiplication: Enter 3')
print('For Division: Enter 4')
print()
x = int(input('Enter Here:'))
if x == 4:
    a = int(input('Enter Numerator:'))
    b = int(input('Enter Denominator:'))
    print('Result: ',a/b)
if x == 2:
    a = int(input('Enter First Value:'))
    b = int(input('Enter Second value:'))
    print('Result: ',a-b)
if x == 1:
    y = int(input('Enter No. of values to be added:'))
    u = 0
    for i in range (y):
        z = int(input(f'Enetr Value {i+1}:'))
        u += z
    print('Result: ',u)
if x == 3:
    y = int(input('Enter No. of values to be multiplied:'))
    u = 1
    for i in range (y):
        z = int(input(f'Enetr Value {i+1} :'))
        u *= z
    print('Result: ',u)
    
