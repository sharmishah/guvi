import sys
H,K=map(int,input().split())
v=list(map(int,input().split()))
for i in range(0,H-1):
    for j in range(i+1,H):
        if (v[i]+v[j])==K:
            print("yes")
            sys.exit()
print("no")
