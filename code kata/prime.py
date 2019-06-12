N=int(input(""))
if(N>1):
  for x in range(2,N):
    if(N%x==0):
      print("no")
    else:
      print("yes")
    break
else:
  print("no")
