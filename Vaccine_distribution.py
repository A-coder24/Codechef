"""Finally, a COVID vaccine is out on the market and the Chefland government has asked you to form a plan to distribute it to the public as soon as possible. There are a total of N people with ages a1,a2,…,aN.

There is only one hospital where vaccination is done and it is only possible to vaccinate up to D people per day. Anyone whose age is ≥80 or ≤9 is considered to be at risk. On each day, you may not vaccinate both a person who is at risk and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and D.
The second line contains N space-separated integers a1,a2,…,aN.
Output
For each test case, print a single line containing one integer ― the smallest required number of days.

Constraints
1≤T≤10
1≤N≤104
1≤D≤105
1≤ai≤100 for each valid i
Subtasks
Subtask #1 (100 points): original constraints

Example Input
2
10 1
10 20 30 40 50 60 90 80 100 1
5 2
9 80 27 72 79
Example Output
10
3
Explanation
Example case 1: We do not need to worry about how the people are grouped, since only one person can be vaccinated in a single day. We require as many days as there are people.

Example case 2: There are two people at risk and three people who are not at risk. One optimal strategy is to vaccinate the two people at risk on day 1 and the remaining three on the next 2 days.

"""
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
    n,d=map(int,input().split())
    arr=sorted(list(map(int,input().split())))
    z=0
    for i in range(n):
        if arr[i]>=80:
            z+=1
        if arr[i]<=9:
            z+=1
    ans=0
    if z%d==0:
        ans+=z//d
    else:
        ans+=z//d+1
        
    if(n-z)%d==0:
        ans+=(n-z)//d
    else:
        ans+=(n-z)//d+1
    print(ans)


    
    
        


    


