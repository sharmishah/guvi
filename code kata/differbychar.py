M,N= map(str,input().split())
c=0
for V in range(len(M)):
  if M[V] != N[V]:
    c+= 1
if c== 1:
  print ("yes")
else:
  print ("no")
