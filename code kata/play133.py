n1,k2=map(int,input().split())
l4=[]
c=0
for i in range(0,n1):
    l4.append(list(map(int,input().split())))
for i in range(0,len(l4)):
    if l4[i][1]==k2:
        c+=1
if c==0:
    print("no")
else:
    print("yes")
