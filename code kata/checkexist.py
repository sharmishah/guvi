S,P=map(int,input().split())
D=[]
for V in input().split():
  D.append(int(V))
A=D.count(P)
if(A>0):
  print("yes")
else:
  print("no")
