from random import*
def main():
    length = randint(5,15)
    x = [0]*length
    for i in range (length):
        x[i] = randint(0,100)
        print(x[i],end=' ')
    print()
    count=0
    for i in range (len(x)-1):
        if x[i]<x[i+1]:
            count+=1
    if count == (len(x)-1):
        print('List is sorted')
    else:
        print('List not sorted')

main()
