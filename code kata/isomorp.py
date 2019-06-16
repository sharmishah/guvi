K,J=map(str,input().split())
le=len(K)
d={}
c=0
for V in range(le):
    if(K[V] not in d.keys()):
        d[K[V]]=J[V]
    else:
        if(d[K[V]]==J[V]):
            continue
        else:
            c=1
            break
if(c==1):
    print("no")
else:
    print("yes")
