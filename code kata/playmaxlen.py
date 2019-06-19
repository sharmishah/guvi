m=int(input())
o=1
v=[]
l=list(map(int,input().split()))
for i in range(0,m-1):
    if(l[i]<l[i+1]):
        o=o+1
    else:
        c.append(d)
        o=1
v.append(o)
print(max(v))
