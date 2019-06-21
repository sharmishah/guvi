sd=list(map(str,input().split()))
for i in range(1,len(sd)):
    if i!=len(sd)-1:
        sd[i]=sd[i][::-1]
print(*sd)
