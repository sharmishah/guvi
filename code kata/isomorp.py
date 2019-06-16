K,J=map(str,input().split())
le=len(s1)
d={}
c=0
for V in range(le):
    if(K[V] not in d.keys()):
        d[K[i]]=J[i]
    else:
        if(d[s1[i]]==s2[i]):
            continue
        else:
            c=1
            break
if(c==1):
    print("no")
else:
    print("yes")
