"""You are given a positive integer N. Consider the sequence S=(1,2,…,N). You should choose two elements of this sequence and swap them.

A swap is nice if there is an integer M (1≤M<N) such that the sum of the first M elements of the resulting sequence is equal to the sum of its last N−M elements. Find the number of nice swaps.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.
Output
For each test case, print a single line containing one integer ― the number of nice swaps.

Constraints
1≤T≤106
1≤N≤109
Subtasks
Subtask #1 (10 points):

T≤10
N≤103
Subtask #2 (30 points):

T≤10
N≤106
Subtask #3 (60 points): original constraints

Example Input
5
1
2
3
4
7
Example Output
0
0
2
2
3
"""
import sys
input = sys.stdin.readline
import operator as op
from functools import reduce

def ncr(n, r):
    if n<r:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom 
    

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
def fact(n):
    x=1
    while(n>0):
        x*=n
        n-=1
    
    return x

t=inp()
for _ in range(t):
    n=inp()
    sum1=n*(n+1)//2
    if sum1 %2!=0:
        print(0)
    else:
        t=(-1+(1+4*sum1)**0.5)/2
        if int(t)!=t:
            t=int(t)
            ans=n-t

        else :
            t=int(t)
            ans=ncr(n-t,2)+ncr(t,2)+n-t
    
            
           
        
        print(ans)











   
    


            
