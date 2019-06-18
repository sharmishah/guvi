t1 =input().split()
c=0
for i in t1[0]:
  if t1[1].count(i) > 0:
    print("yes")
    c=c+1
    break
if c==0:
  print("no")
