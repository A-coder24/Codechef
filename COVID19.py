tests=int(input())
for i in range(tests):
    num=int(input())
    arr=list(map(int,input().split()))
    j=0
    d=[]
    while(j<num):
        p=1
        if j <num-1:
            while(arr[j+1]-arr[j]<=2):
                p+=1
                j+=1
                if j==num-1:
                    break
        j+=1
        d.append(p)

    print(min(d),max(d))
