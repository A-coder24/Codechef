# cook your dish here
def f():
    return list(map(int,input().split()))
def ii():
    return map(int,input().split())
"""-----------------------------------------"""
t=int(input())
for _ in range(t):
    n,m=ii()
    arr=sorted(f())
    arr1=arr[::]
    arr=list(set(arr))
    
    
    a=0
    d=[]
    for i in range(0,len(arr)):
        if a+1 != arr[i]:
            d+=[a+1]
            break
        a=arr[i]
    if d==[]:
        d.append(arr[-1]+1)
    if m in arr:
        if d==[]:
            print(n-arr1.count(m))

        elif d[0]>m :
            print(n-arr1.count(m))
        else:
            print(-1)

    else:
        if d[0]>m:
            print(n)
        elif d[0]==m:
            print(n)
        else:
            print(-1)


