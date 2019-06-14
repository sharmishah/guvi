P=int(input())
n=P//2
N=0
for i in range(2,P):
  if(P%i==0):
    N=1
if(N==0):
  print("no")
if(N==1):
  print("yes")
