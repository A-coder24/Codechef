"""There is a sequence of positive integers A1,A2,…,AN. You do not know this sequence, but your task is to find the value of A1⊕A2⊕…⊕AN, where ⊕ denotes the bitwise XOR operation.

You may ask up to 20 questions. In each question, you should choose an integer K (1≤K≤2⋅106) and the interactor responds with the value of (A1⊕K)+(A2⊕K)+…+(AN⊕K).

Interaction
First, you should read a line containing a single integer T denoting the number of test cases. The description of interaction for T test cases follows.
For each test case, you should start by reading a line containing a single integer N.
To ask a question, you should print a line containing two space-separated integers 1 and K, where 1≤K≤2⋅106. Then, you must read a line containing a single integer ― the answer to your question or −1 if the question is invalid or you asked more than 20 questions.
Finally, you should print a line containing two space-separated integers 2 and X, where X=A1⊕A2⊕…⊕AN. Then, you must read a line containing a single integer: 1 if your answer was correct or −1 if it was incorrect. If your answer was correct, you should continue solving the remaining test cases.
Note that when you receive an answer −1, you should immediately terminate your program to receive a Wrong Answer verdict; otherwise, you may receive any verdict. Don't forget to flush the output after printing each line!

Constraints
1≤T≤100
1≤N≤103
1≤Ai≤106 for each valid i
Subtasks
Subtask #1 (15 points): Ai≤100 for each valid i
Subtask #2 (85 points): original constraints

Example
You             Grader
                1
                4
1 2
                10
1 5 
                18
2 4
                1
Explanation
Example case 1: The hidden sequence is A=[1,2,3,4].

We ask a question with K=2. The grader responds with A1⊕2+A2⊕2+A3⊕2+A4⊕2=10.
Then, we ask a question with K=5 and the grader responds with A1⊕5+A2⊕5+A3⊕5+A4⊕5=18.
Therefore, A1⊕A2⊕A3⊕A4=4.

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
    s=0
    k=1048576   #2**20
    ans=""
    evodd=0
    while(1):
        print(1,k,flush=True)
        if s==0:
            x=inp()
            sum1=x-1048576*n
            ans+=bin(sum1)[-1]
            if x==-1:
                sys.exit(0)
        else:
            tems=inp()
            if tems==-1:
                sys.exit(0)
    
            if sum1==tems:
                evodd=((n)//2)%2
            elif sum1>tems:
                a=(sum1-tems)//k
                z=(n-a)//2+a
                evodd=z%2
                
            else:
                a=(tems-sum1)//k
                z=(n-a)//2
        
                evodd=z%2
            if evodd==0:
                ans+="0"
            else:
                ans+="1"
        s+=1
        k=2**s
        if k>sum1 or k==1048576:
            break

    print(2,int(ans[::-1],2),flush=True)
    ver=inp()
    if ver==-1:
        sys.exit(0)

    

        
    











   
    


            
