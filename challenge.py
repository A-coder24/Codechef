t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    ans=[]
    for i in range (n):
        ans.append([0]*n)

    print(1,1,1,n,n)
    x=int(input())
    if x==-1:
        break
    total=x
    
    r1= 1
    r2=1
    c1=1
    c2=1
    while(total>0):
        print(1,r1,c1,r2,c2)
        x=int(input())
        if x==-1:
            break
        ans[r1-1][c1-1]=x

        c1+=1
        c2+=1
        
        if x==1:
            total-=1
        if (c1-1)%n==0 and c1 !=1:
            c1=1
            c2=1
            r1+=1
            r2+=1

    if x==-1:
        break

    print(2)
    for i in ans:
        print(*i)
    x==input()
    if x==-1:
        break
