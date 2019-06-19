p=int(input())       
q=list(map(int,input().split()))
i=0
count=1
m=count
r=1
for i in range(p-1):
    if(q[i]==q[i+1]):
        count=count+1
        r=count
    elif(count>m):
        m=count
        r=count
        count=1
print(r) 
