nn=int(input())
ln=[]
for i in range(nn):
    ln.append(list(map(int,input().split())))
s=1
k=1
j=nn-1
for i in range(nn):
    s=s*ln[i][i]
    k=k*ln[i][j]
    j=j-1
print(s+k)
