def binary_search(d,j,l,n,ans):
    
    if l <=n :
        x=(l+n)//2
        if d[x] <=j:
            ans=binary_search(d,j,x+1,n,ans)
        elif d[x]>j:
            ans=x
            ans=binary_search(d,j,l,x-1,ans)
    return ans   
    
tests=int(input())
for _ in range(tests):
    n=int(input())
    arr=list(map(int,input().split()))
    d=[]
    for i in arr:
        if d!= []:
            if i >= d[-1]:
                d.append(i)
            else:
                ans=binary_search(d,i,0,len(d)-1,-1)
                d[ans]=i
        else:
            d.append(i)
    print(len(d),end=" ")
    print(*d)

