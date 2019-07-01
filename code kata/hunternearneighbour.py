xx,yy=map(int,input().split())
arr=list(map(int,input().split()))
aa=[]
for i in arr:
    aa.append([abs(i-yy)]+[i])
aa.sort()
aa.pop(0)
for i in aa[:3]:
    print(i[1],end=' ')
