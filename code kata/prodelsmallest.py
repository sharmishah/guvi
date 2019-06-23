from itertools import combinations
xv,yv=map(int,input().split())
gv=len(str(xv))
av=list(combinations(str(xv),gv-yv))
av=(sorted(av))
lv="".join(av[0])
print(lv)
