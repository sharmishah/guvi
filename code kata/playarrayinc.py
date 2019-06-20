K=int(input())
pi=list(map(int,input().split()))
gh=sorted(pi)
wv=[]
for i in range(0,k): wv.append(pi.index(gh[i])+1)
print(*wv)
