import math
def prime(ba1):
  x=0
  if ba1 == 2 and ba1 == 3:
    return True
  for i in range(2,int(math.sqrt(ba1))+1):
    if ba1%i==0:
      return False
      x=x+1
      break
  if x==0:
    return True

ab3=int(input())
for i in range(2,100+1):
  if ab3 % i == 0:
    if prime(i):
      print(i,end=' ')
