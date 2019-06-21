a6,b6=map(int,input().split())
r6=1
g6=1
for i in range(1,a6+1):
    r6=r6*i
for i in range(1,b6+1):
    g6=g6*i
print(r6//g6)
