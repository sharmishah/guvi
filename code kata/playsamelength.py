N=int(input())
K=[str(i) for i in input().split()]
q=w=[]
for i in range(0,N-1):
    for j in range(i+1,N):
        q=list(K[i])
        w=list(K[j])
        if len(q)>len(w) or (len(q)==len(w)and K[i]>K[j]):
            t=K[i]
            K[i]=K[j]
            K[j]=t
print(*K)
