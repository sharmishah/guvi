ah = int(input())
bh = []
for i in range(0,ah):
  i = list(input())
  bh.append(i)
cd = zip(*bh)
cd = list(cd)
for i in cd:
  if(i.count(i[0]) == len(i)):
    print(i[0],end = "")
  else:
    break
