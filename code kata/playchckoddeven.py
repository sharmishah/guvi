y = int(input())
aff =list(map(int,input().split()))
l,l1=[],[]
for v in aff:
    if v % 2 == 0:
        l.append(v)
    else:
        l1.append(v)
if len(l) == 1:
    print(l[0])
else:
    print(l1[0])
