hg=int(input())
hl=list(map(int,input().split()))
hs=[]
for i in hl:
    if(i==hl.index(i)):
        hs.append(i)
print(*(sorted(hs)))
if(len(hs)==0):
    print(-1)
