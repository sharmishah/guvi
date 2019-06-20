e=int(input())
p=list(map(int,input().split()))
p=p[::-1]
yg=[]
for i in range(0,e):
    sh=p[i]
    for j in range(i+1,e):
        sh=sh+p[j]
    yg.append(sh)
print(*yg)
