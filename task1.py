from random import*
x=[2]*12
min_ove=100
max_ove=0
max_ave=0
min_ave=100
print('Monthly Sales: ',end='')
for i in range (len(x)):
    x[i]=randint(10,99)
    print(x[i],end=' ')
print()
print('Quarter 1:',end='')
count=0
max=0
min=100
for i in range (0,3):
    print(x[i],end=' ')
    count=count+x[i]
    if max<x[i]:
        max=x[i]
    if min>x[i]:
        min=x[i]
ave=count/3
if max_ove<max:
    max_ove=max
    a=1
if min_ove>min:
    min_ove=min
    b=1
if max_ave<ave:
    max_ave=ave
    c=1
if min_ave>ave:
    min_ave=ave
    d=1
print(f'Min:{min}',end='')
print(f'Max:{max}',end='')
print(f'Average: {ave}')
count=0
max=0
min=100
print('Quarter 2:',end='')
for i in range (3,6):
    print(x[i],end=' ')
    count=count+x[i]
    if max<x[i]:
        max=x[i]
    if min>x[i]:
        min=x[i]
ave=count/3
if max_ove<max:
    max_ove=max
    a=2
if min_ove>min:
    min_ove=min
    b=2
if max_ave<ave:
    max_ave=ave
    c=2
if min_ave>ave:
    min_ave=ave
    d=2
print(f'Min:{min}',end='')
print(f'   Max:{max}',end='')
print(f'   Average: {ave}')
count=0
max=0
min=100
print('Quarter 3:',end='')
for i in range (6,9):
    print(x[i],end=' ')
    count=count+x[i]
    if max<x[i]:
        max=x[i]
    if min>x[i]:
        min=x[i]
ave=count/3
if max_ove<max:
    max_ove=max
    a=3
if min_ove>min:
    min_ove=min
    b=3
if max_ave<ave:
    max_ave=ave
    c=3
if min_ave>ave:
    min_ave=ave
    d=3
print(f'Min:{min}',end='')
print(f'   Max:{max}',end='')
print(f'   Average: {ave}')
count=0
max=0
min=100
print('Quarter 4:',end='')
for i in range (9,12):
    print(x[i],end=' ')
    count=count+x[i]
    if max<x[i]:
        max=x[i]
    if min>x[i]:
        min=x[i]
ave=count/3
if max_ove<max:
    max_ove=max
    a=4
if min_ove>min:
    min_ove=min
    b=4
if max_ave<ave:
    max_ave=ave
    c=4
if min_ave>ave:
    min_ave=ave
    d=4
print(f'Min:{min}',end='')
print(f'   Max:{max}',end='')
print(f'   Average: {ave}')
print(f'Quarter {b} has minimum sale {min_ove}')
print(f'Quarter {a} has maximum sale {max_ove}')
print(f'Quarter {c} has maximum Average {max_ave}')
print(f'Quarter {d} has mainimum Average {min_ave}')

    
    
    
    


    
    
    
    
