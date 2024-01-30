def bubble_sort(a):
    n=len(a)
    for i in range(n):
        flag=0
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                flag=1
        if(flag==0):
            break
    print(a)
y=[]
n = int(input('Enter how many elements you want: '))
for j in range(0,n):
    x=int(input("Enter the elements"))
    y.append(x)
bubble_sort(y)