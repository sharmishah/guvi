S=input()
X=0
for V in range (0,len(S)):
  if S[V].isdigit():
    X=X+1
    break
for V in range(0,len(S)):
  if S[V].isalpha():
    X=X+1
    break
if(X==2):
  print("Yes")
else:
  print("No")

