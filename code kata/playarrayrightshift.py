M,N=map(int,input().split())
Z=list(map(int,input().split()))
for L in range(N):
    for K in range(M-1,0,-1):
        Z[K],Z[K-1]=Z[K-1],Z[K]
print(*Z)
