import random
def insertion_sort(a):
    for i in range(1,len(a)):
        hole=i
        value=a[i]
        while hole>0 and a[hole-1]>value:
            a[hole]=a[hole-1]
            hole=hole-1
        a[hole]=value
    print(a)
y=[]
n = int(input('Enter how many elements you want: '))
for j in range(0,n):
    x=random.randint(0,1001)
    y.append(x)
insertion_sort(y)


