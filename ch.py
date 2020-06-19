def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 
tests=int(input())
for _ in range(tests):
    p,q,r=map(int,input().split())
    a,b,c=map(int,input().split())
    a1=a-p
    b1=b-q
    c1=c-r
    
    if a1 == b1 == c1 == 0:
        print(0)
        continue
    if a1==b1 ==0 or a1 == c1 == 0 or c1==b1==0 or a1==b1==c1:
        print(1)
        continue
    gcd1=find_gcd(a,b)
    gcd2=find_gcd(b,c)
    gcd3=find_gcd(a,c)
    gcd=find_gcd(gcd1,c)
    if gcd ==0:
        print(1)
        continue
    if a//gcd-p==b//gcd-q==c//gcd-r==0:
        print(1)
        continue
    if (gcd1==0 and c1==0) or (gcd2==0 and a1==0) or (gcd3==0 and b1==0):
        print(1)
        continue
    if q!=0 and r!=0 and p!=0:
        if a//p == c//r== b//q and a%p==c%r==b%q==0:
            print(1)
            continue
    if a1==0 and (r!=0 and q!=0):
        if c//r==b//q and c%r==b%q==0:
            print(1)
            continue
    if b1==0 and (r!=0 and p!=0):
        if c//r==a//p and c%r==a%p==0:
            print(1)
            continue
    if c1==0 and (p!=0 and q!=0):
        if a//p==b//q and a%p==b%q==0:
            print(1)
            continue
    

    if gcd2 !=0:

        if (a1==0 and b//gcd2-q==c//gcd2-r==0) :
            print(1)
            continue
        if (a1==0 and b//abs(gcd2)-q==c//abs(gcd2)-r==0) :
            print(1)
            continue
    if gcd3 !=0:
        if  (b1==0 and a//gcd3-p==c//gcd3-r==0):
            print(1)
            continue
        if  (b1==0 and a//abs(gcd3)-p==c//abs(gcd3)-r==0):
            print(1)
            continue
    if gcd1 !=0:
        if (c1==0 and a//gcd1-p==b//gcd1-q==0):
            print(1)
            continue
        if (c1==0 and a//abs(gcd1)-p==b//abs(gcd1)-q==0):
            print(1)
            continue
    if (a1==0 and b1==c1) or (b1==0 and a1==c1) or (c1==0 and a1==b1):
        print(1)
        continue
    if q!=0 and r!=0 and p!=0:
        if a//p == c//r== b//q and a%p==c%r==b%q:
            print(2)
            continue
    if  r!=0 and q!=0:
        if c//r==b//q and c%r==b%q==a1:
            print(2)
            continue
    if r!=0 and p!=0:
        if c//r==a//p and c%r==a%p==b1:
            print(2)
            continue
    if p!=0 and q!=0:
        if a//p==b//q and a%p==b%q==c1:
            print(2)
            continue
    if b1==c1 or c1==a1 or b1==a1:
        print(2)
        continue
    if gcd2==0:
        print(2)
        continue
    if gcd3==0:
        print(2)
        continue
    if gcd1==0:
        print(2)
        continue
    if ( b//gcd2-q==c//gcd2-r==0) or (a//gcd3-p==c//gcd3-r==0) or (a//gcd1-p==b//gcd1-q==0):
        print(2)
        continue
    if ( b//gcd2-q==c//gcd2-r==a1) or (a//gcd3-p==c//gcd3-r==b1) or (a//gcd1-p==b//gcd1-q==c1):
        print(2)
        continue
    if ( b//abs(gcd2)-q==c//abs(gcd2)-r==a1) or (a//abs(gcd3)-p==c//abs(gcd3)-r==b1) or (a//abs(gcd1)-p==b//abs(gcd1)-q==c1):
        print(2)
        continue
   
    if a//gcd-p==b//gcd-q==c//gcd-r:
        print(2)
        continue
    print(b//gcd2-q)
    print(gcd2)
    print(3)

    

