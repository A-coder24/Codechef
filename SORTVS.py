tests=int(input())
for  i in range(tests):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    d=[]
    t=0
    for j in range(m):
        d.append(list(map(int,input().split())))
    r=1
    arrpos=[*enumerate(arr)]
    print(arrpos)
    arrpos.sort(key=lambda it:it[1])
    print(arrpos)
    visited = {k:False for k in range(n)} 
    ans = 0
    for i in range(n): 
        if visited[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
        if cycle_size > 0: 
            ans += (cycle_size - 1)
    print(ans)