def lcm(x1,y1):
  if x1>y1:
    g1 = x1
  else:
    g1=y1
  while (True):
    if (g1 % x1 == 0) and (g1 % y1 ==0):
      lcm = g1
      break
    g1=g1+1
  return lcm
  
av1 =  int(input())
av2 = list(map(int,input().split()))
x1=av2[0]
for i in range(1,len(av2)):
  x1=lcm(x1,av2[i])
print(x1)
