a=[2,6,4,8,3]
n=len(a)
for i in range(0,n-1): #elements from 0th position to n-2th position is considered, since last element will be the max and will be in the last position in the end
    minimum=i #consider it as minimum value for now
    for j in range (i+1,n):
        if(a[j]<a[minimum]): #check the rest of the array for element less than current minimum
            minimum=j #if found, assigned as minimum
    temp=a[i]   #minimum element and current element is swapped using temp variable
    a[i]=a[minimum]
    a[minimum]=temp
print(a)

