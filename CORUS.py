tests=int(input())
for i in range(tests):
    num,q=map(int,input().split())
    s=input()
    one=set(s)
    final=[]
    for k in one:
        final.append(s.count(k))
    final=sorted(final)
    final=final[::-1]
    for j in range(q):
        ans=0
        c=int(input())
        g=0
        while(final[g]>c and g<len(final)):
            ans+=final[g]-c
            g+=1
            if g==len(final):
                break
        print(ans)


        


