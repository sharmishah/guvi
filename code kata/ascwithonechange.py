I=int(input())
J=list(map(int,input().split()))
K=J[:]
K.sort()
for V in range(0,len(J)):
  if(J[V]!=K[V]):
    print(V)
    break

