aa,bb=map(str,input().split())
l1e=list(set(list(aa)))
l2e=list(set(list(bb)))
l1e.sort()
l2e.sort()
if l1e==l2e:
    print("true")
else:
    print("false")
