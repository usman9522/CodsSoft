from random import*
x=[7]*12
count=0
count_a=0
print('Length: ',len(x))
for i in range (len(x)):
    x[i]=randint(1000,2000)
    print(x[i],end=' ')
    if i<6:
        count=count+x[i]
    else:
        count_a=count_a+x[i]
print()
print('Sale in Two Halves')
print('First Half: ',count)
print('Second Half: ',count_a)
count1=0
count2=0
count3=0
count4=0
for i in range (0,3):
    count1=count1+x[i]
for i in range (3,6):
    count2=count2+x[i]
for i in range (6,9):
    count3=count3+x[i]
for i in range (9,12):
    count4=count4+x[i]
print(count1)
print(count2)
print(count3)
print(count4)
    
