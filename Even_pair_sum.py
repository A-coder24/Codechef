"""Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers A and B.
Output
For each test case, print a single line containing one integer ― the number of valid pairs.

Constraints
1≤T≤1,000
1≤A,B≤109
Subtasks
Subtask #1 (10 points): A,B≤10
Subtask #2 (10 points): A,B≤1,000
Subtask #3 (80 points): original constraints

Example Input
4
1 1
2 3
4 6
8 9
Example Output
1
3
12
36
"""
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
    a,b=map(int,input().split())
    if a%2==0:
        even=a//2
        odd=a//2
    else:
        even=a//2
        odd=(a+1)//2

    
    if b%2==0:
        even1=b//2
        odd1=b//2
    else:
        even1=b//2
        odd1=(b+1)//2
    print(even*even1+odd*odd1)



    
    
        


    


# cook your dish here
