M,N = map(int,input().split())
c= 0
for V in range(M,N+1):
  if V > 1:
    for H in range(2,V):
      if V % H == 0:
        break
    else:
      c+= 1
print(c)
