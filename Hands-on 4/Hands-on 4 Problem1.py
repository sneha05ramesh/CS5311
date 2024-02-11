def sorting(res):
    n=len(res)
    for i in range(1,n):
        value=res[i]
        hole=i
        while hole>0 and res[hole-1]>value:
            res[hole]=res[hole-1]
            hole=hole-1
        res[hole]=value
    print(res)
k=int(input("enter the number of arrays: "))
a=[]
res1=[]
res=[]
for i in range (0,k):
    print("enter the array values separated by space")
    a=input()
    res1.append(list(map(int,a.split(" "))))
for j in res1:
    res.extend(j)
sorting(res)