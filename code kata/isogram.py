A=input()
A=A.lower()
B=""
for V in A:
  if V not in B:
    B=B+V
if(A==B):
  print("yes")
else:
  print("no")
