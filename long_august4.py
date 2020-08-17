"""Chef has a string S. He also has another string P, called pattern. He wants to find the pattern in S, but that might be impossible. Therefore, he is willing to reorder the characters of S in such a way that P occurs in the resulting string (an anagram of S) as a substring.

Since this problem was too hard for Chef, he decided to ask you, his genius friend, for help. Can you find the lexicographically smallest anagram of S that contains P as substring?

Note: A string B is a substring of a string A if B can be obtained from A by deleting several (possibly none or all) characters from the beginning and several (possibly none or all) characters from the end.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single string S.
The second line contains a single string P.
Output
For each test case, print a single line containing one string ― the smallest anagram of S that contains P.

Constraints
1≤T≤10
1≤|P|≤|S|≤105
S and P contain only lowercase English letters
there is at least one anagram of S that contains P
Subtasks
Subtask #1 (20 points): |S|≤1,000
Subtask #2 (80 points): |S|≤105
Example Input
3
akramkeeanany
aka
supahotboy
bohoty
daehabshatorawy
badawy
Example Output
aaakaeekmnnry
abohotypsu
aabadawyehhorst"""
t=int(input())
for _ in range(t):
    s1=list(input())
    s2=list(input())
    beg=0
    if "\r" in s2:
        s2.remove("\r")
    if "\r" in s1:
        s1.remove("\r")
    s3=s2[::]
    begin=[]
    end=[]
    same=[]
    for i in s1:
        if i in s3 :
            s3.remove(i)
        elif i<s2[0]:
            begin.append(i)
        elif i>s2[0]:
            end.append(i)
        elif i==s2[0] :
            same.append(i)
    begin=sorted(begin)
    end=sorted(end)
    this=begin+same+s2+end
    that=begin+s2+same+end
    this="".join(this)
    that="".join(that)
    print(min(this,that))
