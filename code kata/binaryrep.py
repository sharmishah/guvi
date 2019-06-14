M=input()
T=0
for i in range(len(M)):
  if(M[i]!='0' and M[i]!='1'):
    T=1
if(T!=1):
  print("yes")
else:
  print("no")
