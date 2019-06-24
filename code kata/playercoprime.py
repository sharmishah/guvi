def gcd(nn,mm):
    x=[]
    for i in range(1,max(nn,mm)):
        if nn%i==0 and mm%i==0:
            x.append(i)
    ff=len(x)
    return ff      
a,b=map(str,input().split())
mm=len(a)
nn=len(b)
if gcd(mm,nn)==1:
    print("yes")
else:
    print("no")
