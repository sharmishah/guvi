v,ky=map(str,input().split())
v=list(v)
ky=int(ky)
j=-1
for i in range(0,ky+1):
    if str(i) in v: j=j+1
if j==ky: print("yes")
else: print("no")
