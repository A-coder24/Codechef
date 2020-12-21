from sys import stdin, stdout 
tests=int(input())
def decimalToBinary(n):  
    return bin(n).replace("0b","") 
for i in range(tests):
    x,y,l,r=map(int,input().split())   
    r_binary= decimalToBinary(r) 
    l_binary=decimalToBinary(l) 
    ans1=x|y
    ans=decimalToBinary(ans1)
    sub=len(r_binary)-len(ans)
    if sub>0:
        ans="0"*sub+ans
    else:
        r_binary="0"*abs(sub)+r_binary
    sub1=len(r_binary)-len(l_binary)
    l_binary="0"*sub1+l_binary

    
    if x==0 or y==0 or r==l:
        stdout.write("{}\n".format(l))

    elif r>=ans1 and l<=ans1:
        stdout.write("{}\n".format(ans1))

    else:
        finalmax=0
        finalans=0
        match=1

    
        for i in range(len(r_binary)):

            if r_binary[i]=="1" and match == -1:
                key=r_binary[:i]+"0"+ans[i+1:]
    
            
                key_decimal=int(key,2)
                
                max_binary=(x&key_decimal)*(y&key_decimal)
            
                if max_binary>finalmax:
                    finalmax=max_binary
                    finalans=key_decimal
            
            if l_binary[i] == "0" and match == -1 and ans[i]=="1":
                key=l_binary[:i]+"1"+ans[i+1:]

            
                key_decimal=int(key,2)
                
                max_binary=(x&key_decimal)*(y&key_decimal)
            
                if max_binary>=finalmax:
                    finalmax=max_binary
                    finalans=key_decimal

            
            if r_binary[i] != l_binary[i]:
        
                match=-1

        
        max_binary=(x&r)*(y&r)
        if max_binary>finalmax:
            finalmax=max_binary
            finalans=r
        max_binary=(x&l)*(y&l)
        if max_binary>=finalmax:
            finalmax=max_binary
            finalans=l
                    
            count1=""
            count2=""
        
        stdout.write(str(finalans)+"\n")
                
                
    
    


    

    

