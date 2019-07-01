xrx=int(input())
xx=list(map(int,input().split()))
cx=0
px=[]
qx=[]
for i in range(0,len(xx)):
    for j in range(i+1,len(xx)):
        if xx[i]<xx[j]:
            cx=cx+1
            break
    else:
        px.append(xx[i])        
print(*px)
print(max(xx))
