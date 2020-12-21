from sys import stdin, stdout
tests=int(input())
for i in range(tests):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    no_of_odd_Transpositions=0
    ListOf_ODD_ListsOfTranspositions=[]
    ListOf_EVEN_ListsOfTranspositions=[]
    for i in range(0,n):
        ListOfTranspositions=[]
        while(arr[i] != i+1) :

        #the element currently standing on position i should go to position a[i]
            ListOfTranspositions.append([i+1,arr[i]]) #add the transposition from i to a[i]
            temp=arr[i]
            arr[i]=arr[arr[i]-1]
            arr[temp-1]=temp
    
        if ListOfTranspositions!=[]:
            if len(ListOfTranspositions)%2 != 0:
                no_of_odd_Transpositions+=1
                ListOf_ODD_ListsOfTranspositions+=ListOfTranspositions
            else:
                ListOf_EVEN_ListsOfTranspositions+=ListOfTranspositions
   
    ans=[]
    if no_of_odd_Transpositions%2 !=0:
        print(-1)
    else:
        for r in range(0,len(ListOf_EVEN_ListsOfTranspositions),2):
            ans.append("{} {} {}\n".format(ListOf_EVEN_ListsOfTranspositions[r][0],ListOf_EVEN_ListsOfTranspositions[r][1],ListOf_EVEN_ListsOfTranspositions[r+1][1]))
        for r in range(0,len(ListOf_ODD_ListsOfTranspositions),2):
            if ListOf_ODD_ListsOfTranspositions[r+1][0] == ListOf_ODD_ListsOfTranspositions[r][0]:
                ans.append("{} {} {}\n".format(ListOf_ODD_ListsOfTranspositions[r][0],ListOf_ODD_ListsOfTranspositions[r][1],ListOf_ODD_ListsOfTranspositions[r+1][1]))
            else:
                ans.append("{} {} {}\n".format(ListOf_ODD_ListsOfTranspositions[r][0],ListOf_ODD_ListsOfTranspositions[r][1],ListOf_ODD_ListsOfTranspositions[r+1][1]))
                ans.append("{} {} {}\n".format(ListOf_ODD_ListsOfTranspositions[r+1][0],ListOf_ODD_ListsOfTranspositions[r+1][1],ListOf_ODD_ListsOfTranspositions[r][0]))
        if k >= len(ans):
            print(len(ans))
            for i in ans:
                stdout.write(i) 
        else:
            print(-1)



        





