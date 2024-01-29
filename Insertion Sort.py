a=[2,1,3,6,3]
for i in range(1,len(a)):
    hole=i
    value=a[i]
    while hole>0 and a[i-1]>value:
        a[hole]=a[hole-1]
        hole=hole-1
    a[hole]=value
print(a)