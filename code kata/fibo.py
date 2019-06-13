M=int(input())
X=0
Y=1
for i in range(0,M):
  print(Y,end=" ")
  Z=X+Y
  X=Y
  Y=Z
