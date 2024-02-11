def remove_duplicates(a):
    i=0
    while i<len(a)-1:
        j=i+1
        while j<len(a):
            if(a[i]==a[j]):
                a.pop(j)
            else:
                j=j+1
        i=i+1
    print(a)
res=[]
a=input(("Enter the elements of the array separated by space"))
res = list(map(int, a.split())) 
remove_duplicates(res)
