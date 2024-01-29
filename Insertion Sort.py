a=[4,2,8,5]
n=len(a)
for i in range(1,n):
    value=a[i]
    hole=i
    while hole>0 and a[hole-1]>value:
        a[hole]=a[hole-1]
        hole=hole-1
    a[hole]=value
print(a)