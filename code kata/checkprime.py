T=int(input(""))
if(T>1):
  for C in range(2,T):
    if(T%C==0):
      print("no")
      break
  else:
      print("yes")
    
else:
  print("no")
