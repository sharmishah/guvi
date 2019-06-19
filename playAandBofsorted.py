o=int(input())
p=list(map(int,input().split()))
k=list(map(int,input().split()))
y=[]
for i in range(0,o):
    if p[i] in k:
        y.append(p[i])
        y.pop(y.index(p[i]))
print(*y)
