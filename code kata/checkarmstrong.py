N=int(input(""))
sums=0
tem=N
while tem>0:
  dig=tem%10
  sums+=dig**3
  tem//=10
if(N==sums):
  print("yes") 
else:
  print("no")  

