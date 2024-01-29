def insertion_sort(a):
    for i in range(1,len(a)):
        hole=i
        value=a[i]
        while hole>0 and a[i-1]>value:
            a[hole]=a[hole-1]
            hole=hole-1
        a[hole]=value
    print(a)
y=[]
n = int(input('Enter how many elements you want: '))
for j in range(0,n):
    x=int(input("Enter the elements"))
    y.append(x)
insertion_sort(y)


