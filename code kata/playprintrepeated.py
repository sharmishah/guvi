S=input() 
J=S[0]
for V in S:
  if(S.count(J)<=S.count(V)):
    J=V
print(J)
