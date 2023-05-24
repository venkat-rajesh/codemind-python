def max_of_num(array,A,B):
    l=[]
    k=[]
    c=0
    sum=0
    for i in range(A,B+1):
        l.append(i)
    for j in array:
        if j not in l:
            k.append(j)
            c+=1
    if c>0:
        return max(k)
    else:
        return "-1"
n=int(input())
arr=list(map(int,input().split()))
A,B=map(int,input().split())
res=max_of_num(arr,A,B)
print(res)