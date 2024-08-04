file=open('marks.txt','r')
n=int(file.readline())
for i in range (n):
    y=int(file.readline())
    count=0
    for j in range (4):
        b=int(file.readline())
        count=count+b
    ave=count/4
    if i==0:
        min=ave
        max=ave
        class_max=y
        class_min=y
    elif max<ave:
        max=ave
        class_max=y
    if min>ave:
        min=ave
        class_min=y
print('Max:',max,end=' ')
print('class_max:',class_max)
print('Min:',min,end=' ')
print('class_min:',class_min)

file.close()
    
