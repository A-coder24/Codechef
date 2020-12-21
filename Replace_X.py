"""You are given an array of N integers A1,A2,…,AN and three more integers X,p, and k.

An operation on the array is defined to be: replace the k-th smallest integer in the array with any integer you want.

Output the minimum number of operations you must perform on the array (possibly 0 operations) to make the p-th smallest element of the array equal to X. If it is impossible to do so output −1.

Note: the k-th smallest number in an array is the k-th number from the left when the array is sorted in non-decreasing order.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains four integers N,X,p,k respectively.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing one integer ― the minimum number of operations you must perform to make X the p-th smallest element or −1 if its impossible to do so.

Constraints
1≤T≤100
1≤p,k≤N
0≤X≤109
The sum of N over all test cases does not exceed 4∗105
0≤Ai≤109 for each valid i
Subtasks
Subtask #1 (10 points): N≤5
Subtask #2 (40 points): The sum of N over all test cases does not exceed 3∗103
Subtask #3 (50 points): Original constraints

Example Input
2
5 4 3 4
4 9 7 0 8
2 25 1 2
100 20
Example Output
1
-1
Explanation
Example case 1:

We can perform one operation in the array. Take the k-th smallest integer of the current array (which is 8 in this case) and replace it with 0. The array then becomes [4,9,7,0,0] which now makes 4 as the 3rd smallest number of the array.
Example case 2:

It is impossible to make 25 as the smallest number of the array."""
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


t=inp()
for i in range(t):
    n,x,p,k=invr()
    arr=sorted(inlt())
    if (k>p and x>arr[p-1]) or (k<p and x<arr[p-1]):
        print(-1)
    else:
        ans=0
        if arr[p-1]==x:
            print(0)
        elif k>p or  (k==p and x<arr[p-1]):
            ans=1
            z=arr[:p-1][::-1]
            for i in z:
                if i>x:
                    ans+=1
            print(ans)
        
        elif k<p  or (k==p and x>arr[p-1]):
            ans=1
            z=arr[p:]
            print()
            for i in z:
                if i <x:
                    ans+=1
            print(ans)

        
                










