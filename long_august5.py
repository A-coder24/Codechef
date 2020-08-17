""" chef and wedding arragement"""
"""https://www.codechef.com/AUG20B/problems/CHEFWED"""

"""There are N guests (numbered 1 through N) coming to Chef's wedding. Each guest is part of a family; for each valid i, the i-th guest is part of family Fi. You need to help Chef find an optimal seating arrangement.

Chef may buy a number of tables, which are large enough for any number of guests, but the people sitting at each table must have consecutive numbers ― for any two guests i and j (i<j) sitting at the same table, guests i+1,i+2,…,j−1 must also sit at that table. Chef would have liked to seat all guests at a single table; however, he noticed that two guests i and j are likely to get into an argument if Fi=Fj and they are sitting at the same table.

Each table costs K rupees. Chef defines the inefficiency of a seating arrangement as the total cost of tables plus the number of guests who are likely to get into an argument with another guest. Tell Chef the minimum possible inefficiency which he can achieve.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers F1,F2,…,FN.
Output
For each test case, print a single line containing one integer ― the smallest possible inefficiency.

Constraints
1≤T≤100
1≤N≤1,000
1≤K≤1,000
1≤Fi≤100 for each valid i
The sum of N across test cases is ≤5,000
Subtasks
Subtask #1 (20 points): K=1
Subtask #2 (80 points): original constraints
Example Input
3
5 1
5 1 3 3 3
5 14
1 4 2 4 4
5 2
3 5 4 5 1
Example Output
3
17
4
Explanation
Example case 1: The optimal solution is to use three tables with groups of guests [1,2,3], [4] and [5]. None of the tables have any guests that are likely to get into an argument, so the inefficiency is 3⋅K=3.

Example case 2: The optimal solution is to seat all guests at one table. Then, guests 2, 4 and 5 are likely to get into an argument with each other, so the inefficiency is K+3=17."""









t=int(input())
for _ in range(t):
    n,k= map(int,input().split())
    if k==1 or k==2 or k>=n//2:
        fam=list(map(int,input().split()))
        d=[]
        c=k
        x=k
        dub=[]
        p=0
        for i in range(n):

            if fam[i] in d:
                if fam[i] not in dub:
                    dub.append(fam[i])
                    p+=2
                    two=1
                else:
                    p+=1
                    two=0
                if p >=k:
                    c+=k
                    if two==0:
                        c+=p-1
                    else:
                        c+=p-2
                    p=0
                    d=[]
                    dub=[]

            d.append(fam[i])
        c+=p
        c2=k
        d=[]
        for i in range(n):

            if fam[i] in d:
                c2+=k
                d=[]
            d.append(fam[i])

        fam1=fam[::-1]
        d=[]
        dub=[]
        c1=k
        p=0

        for i in range(n):

            if fam1[i] in d:
                if fam1[i] not in dub:
                    dub.append(fam1[i])
                    p+=2
                    two=1
                else:
                    p+=1
                    two=0
                if p >=k:
                    c1+=k
                    if two==0:
                        c1+=p-1
                    else:
                        c1+=p-2
                    p=0
                    d=[]
                    dub=[]

            d.append(fam1[i])
        c1+=p


        
        for i in set(fam):
            t=fam.count(i)
            if t >1:
                x+=t
        print(min(c,x,c1,c2))

    else:
        fam=list(map(int,input().split()))
        mat=[[0 for _ in range(n)] for _ in range(n)]
        dict1={}
        for i in range(n):
            dict1={}
            for j in range(i,n):
                if j==0:
                    mat[i][j]=0
                else:
                    mat[i][j]=mat[i][j-1]
                if fam[j] in dict1:
                    if dict1[fam[j]]==1:
                        mat[i][j]+=1
                    mat[i][j]+=1
                    dict1[fam[j]]+=1
                else:

                    dict1[fam[j]]=1
        
        
        table=100
        dp=[[0 for _ in range(1001)] for _ in range(101)]
        for i in range(0,n+1):
        
            dp[1][i]=mat[0][i-1]
        for i in range(2,101):
            dp[i][1]=0
        for i in range(2,101):
            for j in range(2,n+1):
                try1=pow(10,18)
                for r in range(1,j):
                    try1=min(try1,dp[i-1][r]+mat[r][j-1])
                dp[i][j]=try1
        ans=pow(10,18)
        for t in range(1,101):
            ans=min(t*k+dp[t][n],ans)
        print(ans)




                
