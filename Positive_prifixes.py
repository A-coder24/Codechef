"""You are given two positive integers N and K, where K≤N. Find a sequence A1,A2,…,AN such that:

for each valid i, Ai is either i or −i
there are exactly K values of i such that 1≤i≤N and A1+A2+…+Ai>0
If there are multiple solutions, you may print any one of them. It can be proved that at least one solution always exists.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers N and K.
Output
For each test case, print a single line containing N space-separated integers A1,A2,…,AN.

Constraints
1≤T≤1,000
1≤K≤N≤1,000
Subtasks
Subtask #1 (10 points): N≤10
Subtask #2 (90 points): original constraints

Example Input
1
3 3
Example Output
1 2 3"""
# cook your dish here
import sys
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
    n,k=map(int,input().split())
    d=[]
    k=n-k
    for i in range(1,n+1):
        if i%2!=0 and k>0:
            d.append(-1*i)
            k-=1
        else:
            d.append(i)
    
    if k>0:
        for i in range(n-1,-1,-1):
        
            if d[i]%2==0:
                d[i]=-1*d[i]
                k-=1
            if k==0:
                break
    print(*d)


        



    



    
    
        


    


