Ko=int(input())
no=list(map(int,input().split()))
lio=[]
for x in range(Ko):
    for i in range(x+1,len(no)):
        if(no[i]==no[x]):
          lio.append(no[x])

if (len(lio)==0):
    print("unique")
else:
    lio.sort()
    li2=set(lio)
    for x in li2:
        print(x,end=" ")
