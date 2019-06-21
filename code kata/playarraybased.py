ne=int(input())
le=[int(x) for x in input().split()]
we=[int(c) for c in input().split()]
s=sorted(we)
be=[]
for i in s:
    a=we.index(i)
    be.append(le[a])
print(*be)
