ll=list(input().split())
l1e=[]

for i in ll:
  l1e.append(sorted(list(i)))
ope=[]
for i in l1e:
  ope.append("".join(i))
print(*ope)
