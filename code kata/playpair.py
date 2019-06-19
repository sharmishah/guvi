h=int(input())
u=list(map(int,input().split()))
s=0
for i in range(0,h-1):
    for j in range(i+1,h):
        if u[i]<u[j]: s=s+1
print(s)
