nn=int(input())
nl=list(map(int,input().split()))
nl1=[]
#nl2=[]
for i in nl:
    if i!=0:
        nl1.append(i)
for i in nl:
    if i==0:
        nl1.append(i)
print(*nl1)        
