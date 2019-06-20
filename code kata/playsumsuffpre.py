import sys
n2=int(input())
pq=list(map(int,input().split()))
if n2==1:
    print(*pq)
    sys.exit()
g3=pq
for i in range(0,n2): pq.append(g3[i])
g3=[]
for i in range(0,n2):
    s=0
    for j in range(i,i+(n2+1)):
        s=s+pq[j]
    g3.append(s)
print(*g3)
