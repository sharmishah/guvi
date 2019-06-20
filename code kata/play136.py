nf,kf=map(int,input().split())
lf=[int(x) for x in input().split()]
if kf in lf:
    print("yes",lf.count(k))
else:
    print("no")
