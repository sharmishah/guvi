A=input()
A=A.lower()
B=""
for V in A:
  if V not in B:
    B=B+V
if(A==B):
  print("Yes")
else:
  print("No")
