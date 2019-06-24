def gcd(nnw,mmw):
    x=[]
    for i in range(1,max(nnw,mmw)):
        if nnw%i==0 and mmw%i==0:
            x.append(i)
    ffw=len(x)
    return ffw      
a,b=map(str,input().split())
mmw=len(a)
nnw=len(b)
if gcd(mmw,nnw)==1:
    print("yes")
else:
    print("no")
