axx=input().split()
kk=int(axx[1])
c=0
ax=list(map(int,input().split()))
for i in range(0,len(ax)):
    for j in range(i+1,len(ax)):
        if ax[i]+ax[j]==kk:
            c=1
            break
if c==1:
    print('YES')
else:
    print('NO')
