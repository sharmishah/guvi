def hcf(x3,y3):
  if x3 < y3:
    sh = x3
  else:
    sh = y3
  for i in range(1,sh+1):
    if (x3 % i == 0) and ( y3 % i ==0):
      hcf = i
  return hcf

af1 =  int(input())
af2 = list(map(int,input().split()))
x3=af2[0]
for i in range(1,len(af2)):
  x=hcf(x3,af2[i])
print(x3)
