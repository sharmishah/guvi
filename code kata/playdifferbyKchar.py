N=list(input().split())
P=0
q = list(N[0])
w = list(N[1])
for i in range(0,min(len(q),len(w))):
    if q[i]!=w[i]: P=P+1
P=P+(len(q)-len(w))
if P==int(N[2]):
  print("yes")
else:
  print("no")
