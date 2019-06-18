M= int(input())
l = list(map(int,input().split()))
li1 = l[:]
l.sort()
v = 0
for i in range(len(l)):
  if l[i] != li1[i]:
    v = 1
if v == 0:
  print("yes")
else:
  print("no")
