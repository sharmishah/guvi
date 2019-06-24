nv1,pvk=map(int,input().split())
kv=nv1*pvk
sv=bin(pvk)
for  i in range(0,len(sv)):
    if sv[i]=='1':
        print(i+1)
        break
