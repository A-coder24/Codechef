def f():
    return map(int ,input().split())
def lis():
    return list(map(int ,input().split()))
""".........................................."""
from functools import reduce
a=[0]*10
k=int(input())
c=0
s="codeforces"
while reduce(lambda x,y:x*y,a)<k:
	a[c%10]+=1
	c+=1
t=""
 
for i in range(10):
	t+=s[i]*a[i]
print(t)


