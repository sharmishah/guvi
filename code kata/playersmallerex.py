nf1,kkf=map(int,input().split())
lf=[int(x) for x in input().split()]
mf=0
if kkf in lf:
    print(kkf)
else:
    for i in lf:
        if i>mf and i<kkf:
            mf=i
    print(mf)
