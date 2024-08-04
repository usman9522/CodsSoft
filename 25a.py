from random import*
x=[7]*10
count=0
print('Length: ',len(x))
for i in range (len(x)):
    x[i]=randint(1,1000)
    print(x[i],end=' ')
    count=count+x[i]
ave=count/len(x)
print('Average: ',ave)
count_g_zero=0
count_l_zero=0
for i in range (len(x)):
    a=x[i]-ave
    #b=round(a,2)
    print(a,end=' ')
    if a>0:
        count_g_zero=count_g_zero+1
    else:
        count_l_zero=count_l_zero+1
print()
print('Count of positive values: ',count_g_zero)
print('Count of negative values: ',count_l_zero)
