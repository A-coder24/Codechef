Vivek was quite bored with the lockdown, so he came up with an interesting task. He successfully completed this task and now, he would like you to solve it.

You are given two strings A and B, each with length N. Let's index the characters in each string from 0 ― for each i (0≤i<N), the i+1-th characters of A and B are denoted by Ai and Bi respectively. You should convert A to B by performing operations of the following type:

Choose a subset S of the set {0,1,…,N−1}.
Let c be the alphabetically smallest character among Ax for all x∈S.
For each x∈S, replace Ax by c.
You should find the smallest necessary number of operations or report that it is impossible to convert A to B. If it is possible, you also need to find one way to convert A to B using this smallest number of operations. If there are multiple solutions, you may find any one.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a single string A.
The third line contains a single string B.
Output
For each test case:

If it is impossible to convert A to B, print a single line containing the integer −1.
Otherwise, first, print a line containing a single integer K ― the minimum number of operations.
Then, print K lines describing the operations. Each of these lines should contain a positive integer Z, followed by a space and Z pairwise distinct space-separated integers from the set {0,1,…,N−1} ― the elements of S.
Constraints
1≤T≤20
1≤N≤103
|A|=|B|=N
A and B contain only lowercase English letters
Subtasks
Subtask #1 (30 points): B contains only characters 'a' and 'b'

Subtask #2 (70 points): original constraints

Example Input
3
5
abcab
aabab
3
aaa
aab
2
de
cd
Example Output
2
3 1 2 4
3 0 1 3
-1
-1
Explanation
Example case 1:

First, we can choose S=(1,2,4), so the character c is 'b' and the string A after this operation is "abbab".
Then, we choose S=(0,1,3), so c is 'a', and A becomes "aabab".
There is no way to convert A to B in only one operation.
Example case 2: We can see that it is impossible to convert A to B since c is always 'a'.

Example case 3: We can see again that it is impossible to convert A to B since c cannot be 'c'.





tests=int(input())
for _ in range(tests):
    n=int(input())
    a=input()
    aa=[]
   
    b=input()

    d={}

    a1=set(a)
    b1=set(b)
    x=0
    if (a1 | b1) != a1:
        print(-1)
        continue
    dd={}
    for i in range(n):
        if b[i] != a[i]:
            if ord(b[i])>ord(a[i]):
                x=1
                break
            if b[i] in d:
                d[b[i]].append(i)
            else:
                d[b[i]]=[i]
                
   

                

    if x==1:
        print(-1)
        continue
    z=sorted(d,reverse=True)
    print(len(d))
    for i in z:
        print(len(d[i])+1,end=" ")
        print(*d[i],a.index(i))


        

