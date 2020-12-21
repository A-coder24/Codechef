"""You are given a sequence A1,A2,…,AN and you have to perform the following operation exactly X times:

Choose two integers i and j such that 1≤i<j≤N.
Choose a non-negative integer p.
Change Ai to Ai⊕2p, and change Aj to Aj⊕2p, where ⊕ denotes bitwise XOR.
Find the lexicographically smallest sequence which can be obtained by performing this operation exactly X times.

A sequence B1,B2,…,BN is said to be lexicographically smaller than a sequence C1,C2,…,CN if there is an index i such that Bi<Ci and for each valid j<i, Bj=Cj.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and X.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing N space-separated integers ― the lexicographically smallest obtainable sequence.

Constraints
1≤T≤10
2≤N≤105
1≤X≤109
1≤Ai≤109 for each valid i
Subtasks
Subtask #1 (30 points): N≤100
Subtask #2 (70 points): original constraints

Example Input
1
3 3
2 2 3
Example Output
0 0 3
"""
import sys
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def printlist(var) : sys.stdout.write(' '.join(map(str, var))+'\n')
t=inp()
for _ in range(t):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))

    
    for i in range(n-1):
        bb=0
        while(arr[i]!=0 and q!=0):
            
        
            b = int(math.log(arr[i], 2)) 
            z=pow(2,b)
            arr[i]=arr[i]^z
            f=0
            for j in range(i+1,n):
                if arr[j]^z<arr[j]:
                
                    f=1
                    arr[j]=arr[j]^z
                    

                    
                if f==1:
                    q-=1
                    break
        
            if f!=1:
                q-=1
                arr[-1]=arr[-1]^z
            if q<=0:
                break
        if q<=0:
            break
    if q>0:
        if n>2 or q%2==0:
            q=0
        else:
    
            arr[-1]=arr[-1]^1
            arr[-2]=arr[-2]^1          
            q=0
    
    print(*arr)




        


        
         


                    




        



    



    
    
        


    


