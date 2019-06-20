g=int(input())
p=list(map(int,input().split()))
g1=[]
for i in range(0,g):
    s2=0
    for j in range(0,i+1):
        s2=s2+p[j]
    g1.append(s2)
print(*g1)
