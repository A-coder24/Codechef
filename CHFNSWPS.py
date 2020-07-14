""" chefina and swaps"""
"""Chefina has two sequences A1,A2,…,AN and B1,B2,…,BN. She views two sequences with length N as identical if, after they are sorted in non-decreasing order, the i-th element of one sequence is equal to the i-th element of the other sequence for each i (1≤i≤N).

To impress Chefina, Chef wants to make the sequences identical. He may perform the following operation zero or more times: choose two integers i and j (1≤i,j≤N) and swap Ai with Bj. The cost of each such operation is min(Ai,Bj).

You have to find the minimum total cost with which Chef can make the two sequences identical.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains N space-separated integers B1,B2,…,BN.
Output
For each test case, print a single line containing one integer ― the minimum cost, or −1 if no valid sequence of operations exists.

Constraints
1≤T≤2,000
1≤N≤2⋅105
1≤Ai,Bi≤109 for each valid i
the sum of N over all test cases does not exceed 2⋅106
Subtasks
Subtask #1 (15 points):

T≤20
N≤20
Subtask #2 (85 points): original constraints

Example Input
3
1
1
2
2
1 2
2 1
2
1 1
2 2
Example Output
-1
0
1
Explanation
Example case 1: There is no way to make the sequences identical, so the answer is −1.

Example case 2: The sequence are identical initially, so the answer is 0.

Example case 3: We can swap A1 with B2, which makes the two sequences identical, so the answer is 1."""



tests=int(input())
for _ in range(tests):
    n=int(input())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    d1={}                #count of nos. which are not in d2
    d2={}                #count of nos.which are not in d1
    min1=10000000000
    for i in range(n):
        if arr[i]<min1:
            min1=arr[i]

        if arr[i] not in d1:
            d1[arr[i]]=1
        else:
            d1[arr[i]]+=1
    for i in range(n):
        if brr[i]<min1:
            min1=brr[i]
        if brr[i] in d1:
            d1[brr[i]]-=1
            if d1[brr[i]]==0:
                d1.pop(brr[i])
        elif brr[i] not in d2:
            d2[brr[i]]=1
        else:
            d2[brr[i]]+=1
    
    f=0
    pow1=[]
    for i in d1:
        if d1[i]%2 ==0:
            pow1+=[i]*(d1[i]//2)
        else:
            f=1
            break
    for i in d2:
        if d2[i]%2 ==0:
            pow1+=[i]*(d2[i]//2)
        else:
            f=1
            break


    
    if f==1:
        print(-1)
    else:
        ans=0
        pow1=sorted(pow1)
        pow1=pow1[:len(pow1)//2]
        for i in pow1:
            if 2*min1>=i:
                ans+=i
            else:
                ans+=2*min1
        print(ans)

        


            

            
            




       
       
    
        
        



    
    


