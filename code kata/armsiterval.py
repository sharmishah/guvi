u,v=input().split()
u=int(u)
v=int(v)
for N in range(u,v):
  sums=0
  tem=N
  while tem>0:
    dig=tem%10
    sums+=dig**3
    tem//=10
  if(N==sums):
    print(N,end=' ') 


