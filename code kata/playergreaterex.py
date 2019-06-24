pn1,pkk=map(int,input().split())
pl=[int(x) for x in input().split()]
pl.sort()
for i in pl:
    if i>pkk:
        print(i)
        break
