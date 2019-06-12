N=int(input(""))
rev=0
temp=N
while(temp!=0):
  dig=temp%10
  temp=temp/10
  rev=rev*10+dig
if(N==rev):
  print("no")
else:
  print("yes")
  
