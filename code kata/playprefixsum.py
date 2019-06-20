nu=int(input())
lu=[int(x) for x in input().split()]
sp=[]
for i in range(nu):
    tc=lu[:i+1]
    if sum(tc)%2==0:
        sp.append(str(sum(tc)))
    else:
        sp.append(str(lu[i]))
print(" ".join(sp))
