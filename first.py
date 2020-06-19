#n,t=map(int,input().split())
#arr= list(map(int,input().split()))
tests=int(input())
for i in range(tests):
    a,b=map(int,input().split())
    if b*2<=a:
        ans=b
    elif a*2<=b:
        ans=a
    elif a>=b:
        ans=a//2
        b=b-a//2
        a=a%2
        ans+= b//3
        if b>=2 and a>0:
            b-=2
            a-=1
            ans+=1
        a=a%2  
    elif b>a:
        ans=b//2
        a=a-b//2
        b=b%2
        if a>=2 and b>0:
            a-=2
            b-=1
            ans+=1
        ans+=a//3
    print([ans])                                                                                                                                                                             